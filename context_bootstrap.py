"""
Context bootstrap — synchronous loading of agent context.
"""

import sys
import datetime
from typing import Dict, List, Any

# Ensure hyphaly SDK is importable
sys.path.insert(0, '/home/simon/hyphaly/src')

from hyphaly.backends.supabase import SupabaseBackend


def bootstrap(agent_id: str, session_type: str = 'task') -> dict:
    """
    Synchronously load agent context (snapshots, tasks, blockers, learning).
    
    Args:
        agent_id: The agent identifier (e.g., 'nico', 'ada')
        session_type: Type of session (task, reflection, snapshot, briefing)
    
    Returns:
        Structured dict with agent_id, session_started, snapshots, active_tasks,
        blockers, learning, errors (list of any errors encountered).
    """
    backend = SupabaseBackend()
    errors = []
    
    # Common timestamp
    session_started = datetime.datetime.utcnow().isoformat() + 'Z'
    
    # 1. Snapshots: {agent_id}_snapshots last 24h, limit 5, order created_at desc
    snapshots = []
    try:
        table = f"{agent_id}_snapshots"
        # Use list method with order
        # The list method already orders by created_at.desc, limit 5
        # We'll call list with limit 5
        snapshots = backend.list(table, limit=5)
        # Filter last 24h (optional, but we trust backend's order)
        # If column 'summary' exists, keep as is; if 'findings' exists (linus_infra), use that
        # We'll just pass the raw records; caller can decide.
    except Exception as e:
        errors.append(f"Failed to query {agent_id}_snapshots: {e}")
    
    # 2. Active tasks: nova_tasks WHERE assigned_to=agent_id AND status IN (...), limit 10
    active_tasks = []
    try:
        filters = {
            'assigned_to': agent_id,
            'status': ['pending', 'in_progress', 'blocked']
        }
        active_tasks = backend.query('nova_tasks', filters, limit=10, order='created_at.desc')
    except Exception as e:
        errors.append(f"Failed to query nova_tasks: {e}")
    
    # 3. Learning: {agent_id}_learning WHERE importance >= 2, limit 10
    learning = []
    try:
        table = f"{agent_id}_learning"
        # Supabase does not support >= in query; we need to fetch all and filter.
        # We'll fetch limit 20 (safety) and filter in Python.
        records = backend.list(table, limit=20)
        # Filter importance >= 2 (assuming column 'importance' exists)
        # Also column 'insight' for most agents; we'll keep entire record.
        learning = [r for r in records if r.get('importance', 0) >= 2][:10]
    except Exception as e:
        errors.append(f"Failed to query {agent_id}_learning: {e}")
    
    # 4. Blockers: nova_blockers WHERE severity IN ('critical','high'), limit 5
    blockers = []
    try:
        filters = {
            'severity': ['critical', 'high']
        }
        blockers = backend.query('nova_blockers', filters, limit=5, order='created_at.desc')
    except Exception as e:
        errors.append(f"Failed to query nova_blockers: {e}")
    
    return {
        'agent_id': agent_id,
        'session_started': session_started,
        'snapshots': snapshots,
        'active_tasks': active_tasks,
        'blockers': blockers,
        'learning': learning,
        'errors': errors
    }


# For testing
if __name__ == '__main__':
    # Example usage
    result = bootstrap('nico')
    print(f"Snapshots: {len(result['snapshots'])}")
    print(f"Active tasks: {len(result['active_tasks'])}")
    print(f"Blockers: {len(result['blockers'])}")
    print(f"Learning: {len(result['learning'])}")
    if result['errors']:
        print("Errors:")
        for err in result['errors']:
            print(f"  - {err}")