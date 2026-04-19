import urllib.request, json

anon_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVmb2FlbnZ6cnN2aGxycmlmdGR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM1NjczNTgsImV4cCI6MjA4OTE0MzM1OH0.k7XslO-8Kjf58oAQDRFMSai57x5GhzN2jDhESQocfSI'

# Step 2: Write to nova_daily_logs
logs_payload = {
    'session_type': 'reflection',
    'workspace_id': 'lyyte',
    'log_date': '2026-04-17',
    'attempted': 'Sprint 1 Friday wrap: reviewed open tasks, assessed poller runaway loop fix and Jeeves quality gate — both rolled to Sprint 2. Sent Friday status to Simon. Ran sprint recap prep for Sunday.',
    'what_worked': 'Sprint cadence and verify-before-reporting protocol kept task state clean. Linus delivered Guardian v2.0 spec on time — verified on disk.',
    'what_failed': 'Poller runaway loop fix not completed — complexity underestimated, rolled to Sprint 2. Also Jeeves quality gate deferred.',
    'do_differently': 'Scope complex tasks with explicit sub-step breakdown before dispatching. Roll risk earlier.',
    'simon_should_know': 'Foundation Sprint 1 ended with 2 items rolling to Sprint 2. No production incidents. Org held 3 days clean — goal met. Sunday recap will flag blockers and learnings.'
}

req = urllib.request.Request(
    'https://efoaenvzrsvhlrriftdx.supabase.co/rest/v1/nova_daily_logs',
    data=json.dumps(logs_payload).encode(),
    headers={'apikey': anon_key, 'Authorization': f'Bearer {anon_key}', 'Content-Type': 'application/json', 'Prefer': 'return=representation'},
    method='POST'
)
r = urllib.request.urlopen(req)
print('nova_daily_logs status:', r.status)
resp = json.loads(r.read().decode())
print('id:', resp[0]['id'] if resp else 'no id')

# Step 3: Write to agent_memory
mem_payload = {
    'agent': 'nova',
    'type': 'synthesis',
    'workspace_id': 'lyyte',
    'entry': 'Operational proximity scales as team grows — not away from it. The temptation to delegate fully as agents increase is the same trap as scaling management layers. Founder mode means staying close to what can break. Guardian v2.0 proved clean spec + tight escalation beats good intentions.',
    'window': '2026-04-18-04'
}

req2 = urllib.request.Request(
    'https://efoaenvzrsvhlrriftdx.supabase.co/rest/v1/agent_memory',
    data=json.dumps(mem_payload).encode(),
    headers={'apikey': anon_key, 'Authorization': f'Bearer {anon_key}', 'Content-Type': 'application/json', 'Prefer': 'return=representation'},
    method='POST'
)
r2 = urllib.request.urlopen(req2)
print('agent_memory status:', r2.status)
resp2 = json.loads(r2.read().decode())
print('id:', resp2[0]['id'] if resp2 else 'no id')