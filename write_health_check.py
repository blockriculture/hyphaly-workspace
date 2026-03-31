#!/usr/bin/env python3
"""
Write infrastructure health check to Supabase linus_infra table
"""
import os
import json
import subprocess
import datetime
from urllib.request import Request, urlopen
from urllib.error import URLError

# Configuration
SUPABASE_URL = "https://efoaenvzrsvhlrriftdx.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")  # Should be set from environment
TABLE = "linus_infra"

def get_system_status():
    """Gather current system status"""
    try:
        # Get uptime
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = int(float(f.read().split()[0]))
        
        # Get load average
        with open('/proc/loadavg', 'r') as f:
            load_avg = f.read().split()[:3]
        
        # Get memory info
        with open('/proc/meminfo', 'r') as f:
            meminfo = {}
            for line in f:
                key, value = line.split(':')
                meminfo[key.strip()] = int(value.split()[0])
        
        mem_used = (meminfo['MemTotal'] - meminfo['MemAvailable']) / 1024 / 1024  # GB
        mem_total = meminfo['MemTotal'] / 1024 / 1024  # GB
        
        # Get disk info
        disk_out = subprocess.check_output(['df', '-h', '/']).decode().split('\n')[1].split()
        disk_used_pct = int(disk_out[4].rstrip('%'))
        
        # Check if firewall is enabled
        try:
            ufw_status = subprocess.check_output(['sudo', 'ufw', 'status'], stderr=subprocess.DEVNULL).decode().strip()
            firewall_enabled = 'active' in ufw_status.lower()
        except:
            firewall_enabled = False
        
        # Check if fail2ban is installed
        fail2ban_running = False
        try:
            result = subprocess.check_output(['systemctl', 'is-active', 'fail2ban'], stderr=subprocess.DEVNULL).decode().strip()
            fail2ban_running = result == 'active'
        except:
            fail2ban_running = False
        
        # Check nova service status
        try:
            nova_status = subprocess.check_output(['systemctl', 'is-active', 'nova'], stderr=subprocess.DEVNULL).decode().strip()
            nova_active = nova_status == 'active'
        except:
            nova_active = False
        
        return {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "uptime_seconds": uptime_seconds,
            "load_average": float(load_avg[0]),
            "memory_used_gb": round(mem_used, 2),
            "memory_total_gb": round(mem_total, 2),
            "disk_used_percent": disk_used_pct,
            "firewall_enabled": firewall_enabled,
            "fail2ban_running": fail2ban_running,
            "nova_service_active": nova_active,
            "status": "operational" if nova_active else "degraded"
        }
    except Exception as e:
        return {"error": str(e), "status": "error"}

def write_to_supabase(data):
    """Write health check data to Supabase"""
    if not SUPABASE_KEY:
        print("ERROR: SUPABASE_KEY not set")
        return False
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    url = f"{SUPABASE_URL}/rest/v1/{TABLE}"
    
    try:
        request = Request(
            url,
            data=json.dumps(data).encode('utf-8'),
            headers=headers,
            method='POST'
        )
        with urlopen(request) as response:
            if response.status in [201, 204]:
                print(f"✓ Successfully wrote health check to {TABLE}")
                return True
            else:
                print(f"✗ Failed: HTTP {response.status}")
                return False
    except URLError as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    status = get_system_status()
    
    # Add metadata
    status["check_id"] = f"health_check_{datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"
    status["assessed_by"] = "linus_health_check"
    
    print("\n=== INFRASTRUCTURE HEALTH CHECK ===")
    print(json.dumps(status, indent=2))
    
    # Try to write to Supabase
    print("\nAttempting to write to Supabase...")
    write_to_supabase(status)
