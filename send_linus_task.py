#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/simon/.openclaw/workspace')
from send_hyphaly import send_to_broker

message = """Task: Fix GitHub authentication

nova_tasks shows: Git push failing — no GitHub authentication configured (in_progress, Mar 28)

What needs doing:
- The workspace at ~/.openclaw/workspace has a git remote that can't push
- Run: cd ~/.openclaw/workspace && git remote -v then git push to see exact error
- Fix the authentication so git push works

Context: Simon GitHub: Plainoldsimon | Repo: hyphaly

Report back what you find and what you did."""

result = send_to_broker(
    sender_id="nova",
    target_agent_id="agent:linus:main",
    message_content=message,
    message_type="task"
)
print(result)
