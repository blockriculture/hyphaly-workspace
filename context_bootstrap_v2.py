"""
Context bootstrap v2 for Hyphaly SDK.
Loads agent memory context from agent_memory table on session start.
Replaces context_bootstrap.py with lightweight, always-current approach.
"""

import json
import urllib.request
from datetime import datetime
from typing import Dict, List, Any, Optional

# Supabase credentials from BOOT.md
SUPABASE_URL = "https://efoaenvzrsvhlrriftdx.supabase.co"
ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVmb2FlbnZ6cnN2aGxycmlmdGR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM1NjczNTgsImV4cCI6MjA4OTE0MzM1OH0.k7XslO-8Kjf58oAQDRFMSai57x5GhzN2jDhESQocfSI"


def bootstrap(agent_id: str) -> Dict[str, Any]:
    """
    Load agent memory context from agent_memory table.
    
    Args:
        agent_id: The agent identifier
    
    Returns:
        Dict with agent, recent_memories, last_synthesis, memory_count, bootstrapped_at, status
    """
    result = {
        'agent': agent_id,
        'recent_memories': [],
        'last_synthesis': None,
        'memory_count': 0,
        'bootstrapped_at': datetime.utcnow().isoformat() + 'Z',
        'status': 'ok'
    }
    
    try:
        # Query recent memories (micro and synthesis)
        url = f"{SUPABASE_URL}/rest/v1/agent_memory"
        headers = {
            'apikey': ANON_KEY,
            'Authorization': f'Bearer {ANON_KEY}',
            'Accept': 'application/json'
        }
        query_params = [
            f'agent=eq.{agent_id}',
            f'type=in.(micro,synthesis)',
            f'order=created_at.desc',
            f'limit=10'
        ]
        query_string = '&'.join(query_params)
        full_url = f"{url}?{query_string}"
        
        req = urllib.request.Request(full_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                if isinstance(data, list):
                    result['recent_memories'] = [
                        {
                            'entry': entry.get('entry', ''),
                            'created_at': entry.get('created_at'),
                            'type': entry.get('type')
                        }
                        for entry in data
                    ]
                    result['memory_count'] = len(data)
                else:
                    result['status'] = 'error'
                    result['error'] = 'Unexpected response format'
            else:
                result['status'] = 'error'
                result['error'] = f'HTTP {response.status}'
    except urllib.error.HTTPError as e:
        # Table may not exist
        result['status'] = 'error'
        result['error'] = f'Table not found or access denied: {e.code} {e.reason}'
    except Exception as e:
        result['status'] = 'error'
        result['error'] = str(e)
    
    # If we got recent memories, also query for latest synthesis
    if result['status'] == 'ok' and result['memory_count'] > 0:
        try:
            url = f"{SUPABASE_URL}/rest/v1/agent_memory"
            headers = {
                'apikey': ANON_KEY,
                'Authorization': f'Bearer {ANON_KEY}',
                'Accept': 'application/json'
            }
            query_params = [
                f'agent=eq.{agent_id}',
                f'type=eq.synthesis',
                f'order=created_at.desc',
                f'limit=1'
            ]
            query_string = '&'.join(query_params)
            full_url = f"{url}?{query_string}"
            
            req = urllib.request.Request(full_url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode())
                    if isinstance(data, list) and len(data) > 0:
                        result['last_synthesis'] = data[0].get('entry')
        except Exception:
            # If synthesis query fails, leave as None
            pass
    
    # Set status based on memory count
    if result['status'] == 'ok':
        if result['memory_count'] == 0:
            result['status'] = 'empty'
    
    return result


def format_for_prompt(bootstrap_result: Dict[str, Any]) -> str:
    """
    Format bootstrap result for agent prompt injection.
    
    Args:
        bootstrap_result: Dict from bootstrap()
    
    Returns:
        Formatted string for prompt
    """
    agent = bootstrap_result.get('agent', 'unknown')
    bootstrapped_at = bootstrap_result.get('bootstrapped_at', '')
    last_synthesis = bootstrap_result.get('last_synthesis')
    memory_count = bootstrap_result.get('memory_count', 0)
    recent_memories = bootstrap_result.get('recent_memories', [])
    
    lines = []
    lines.append(f"MEMORY CONTEXT — {agent} — {bootstrapped_at}")
    lines.append(f"Last synthesis: {last_synthesis or 'None'}")
    lines.append(f"Recent activity ({memory_count} entries):")
    
    for mem in recent_memories:
        entry_text = mem.get('entry', '').strip()
        if entry_text:
            lines.append(f"- {entry_text}")
    
    return '\n'.join(lines)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        agent = sys.argv[1]
        result = bootstrap(agent)
        print(f"Bootstrap result: {json.dumps(result, indent=2)}")
        print("\nFormatted for prompt:")
        print(format_for_prompt(result))
    else:
        print("Usage: python context_bootstrap_v2.py <agent_id>")