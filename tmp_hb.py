import subprocess, json

result = subprocess.run(['python3', '/home/simon/.openclaw/workspace/supabase_read.py', 'nova_tasks'], capture_output=True, text=True)
data = json.loads(result.stdout)
for t in data:
    if 'clio silent' in t.get('task','').lower():
        print(t.get('created_at',''), t.get('status'), t.get('task','')[:80])
