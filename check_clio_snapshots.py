#!/usr/bin/env python3
"""
Check if Clio has written to clio_snapshots in the last N hours.
Returns JSON with result and the most recent snapshot timestamp.
Always queries Supabase directly — no caching.
"""
import sys
import json
import urllib.request
from datetime import datetime, timezone, timedelta

# Supabase configuration
SUPABASE_URL = "https://efoaenvzrsvhlrriftdx.supabase.co"
ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVmb2FlbnZ6cnN2aGxycmlmdGR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM1NjczNTgsImV4cCI6MjA4OTE0MzM1OH0.k7XslO-8Kjf58oAQDRFMSai57x5GhzN2jDhESQocfSI"

def check_clio_snapshots(hours: int = 2):
    """
    Query clio_snapshots for entries in the last N hours.
    Returns a dict with:
    - has_entries: bool (True if any entries found)
    - hours_since_last: float (hours since last snapshot, or None if never)
    - last_snapshot_time: str (ISO timestamp of last snapshot, or None)
    - count_recent: int (number of entries in the last N hours)
    - count_total: int (total entries in table)
    """
    # Get current time in UTC
    now = datetime.now(timezone.utc)
    cutoff_time = now - timedelta(hours=hours)

    # Query for recent snapshots
    url = f"{SUPABASE_URL}/rest/v1/clio_snapshots?select=created_at&order=created_at.desc&limit=100"
    headers = {
        "apikey": ANON_KEY,
        "Authorization": f"Bearer {ANON_KEY}",
        "Content-Type": "application/json"
    }

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            snapshots = json.loads(response.read().decode())
    except Exception as e:
        return {
            "error": str(e),
            "has_entries": False,
            "hours_since_last": None,
            "last_snapshot_time": None,
            "count_recent": 0,
            "count_total": 0
        }

    count_total = len(snapshots)

    # Filter snapshots within the last N hours
    recent_snapshots = []
    last_snapshot_time = None
    hours_since_last = None

    for snapshot in snapshots:
        created_at_str = snapshot.get('created_at', '')
        if not created_at_str:
            continue

        # Parse the timestamp (Supabase returns ISO format with Z)
        try:
            if created_at_str.endswith('Z'):
                created_at = datetime.fromisoformat(created_at_str.replace('Z', '+00:00'))
            else:
                created_at = datetime.fromisoformat(created_at_str)

            if created_at > cutoff_time:
                recent_snapshots.append(created_at_str)

            # Track the most recent snapshot
            if last_snapshot_time is None:
                last_snapshot_time = created_at_str
                hours_since_last = (now - created_at).total_seconds() / 3600

        except Exception as e:
            # Skip malformed timestamps
            continue

    return {
        "has_entries": len(recent_snapshots) > 0,
        "hours_since_last": hours_since_last,
        "last_snapshot_time": last_snapshot_time,
        "count_recent": len(recent_snapshots),
        "count_total": count_total,
        "query_time_utc": now.isoformat().replace('+00:00', 'Z'),
        "cutoff_time_utc": cutoff_time.isoformat().replace('+00:00', 'Z')
    }

if __name__ == "__main__":
    # Allow command-line argument for hours (default: 2)
    hours = 2
    if len(sys.argv) > 1:
        try:
            hours = int(sys.argv[1])
        except ValueError:
            print(f"Invalid hours argument: {sys.argv[1]}", file=sys.stderr)
            sys.exit(1)

    result = check_clio_snapshots(hours)
    print(json.dumps(result, indent=2))

    # Exit with non-zero if no recent entries found (useful for scripts)
    if not result.get("has_entries", False) and not result.get("error"):
        sys.exit(1)
