import sys,json

# nova_tasks
data = json.load(sys.stdin)
open_tasks = [d for d in data if d['status'] in ('open','pending','in_progress')]
print('Open tasks:', len(open_tasks))
for t in open_tasks:
    print(' ', t['id'][:8], t['task'][:60])
