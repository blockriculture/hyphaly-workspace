import subprocess, json
result = subprocess.run(['python3', '/home/simon/.openclaw/workspace/supabase_read.py', 'nova_tasks'], capture_output=True, text=True)
tasks = json.loads(result.stdout)
open_tasks = [t for t in tasks if t.get('status') == 'open']
print(f'Open tasks: {len(open_tasks)}')
for t in open_tasks:
    print(f'  - {t.get("task","")[:100]} [{t.get("priority","?")}]')
