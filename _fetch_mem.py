import urllib.request, json

url = 'https://efoaenvzrsvhlrriftdx.supabase.co/rest/v1/agent_memory?agent=eq.nova&type=in.(micro,synthesis)&order=created_at.desc&limit=8'
headers = {
    'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVmb2FlbnZ6cnN2aGxycmlmdGR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM1NjczNTgsImV4cCI6MjA4OTE0MzM1OH0.k7XslO-8Kjf58oAQDRFMSai57x5GhzN2jDhESQocfSI',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVmb2FlbnZ6cnN2aGxycmlmdGR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM1NjczNTgsImV4cCI6MjA4OTE0MzM1OH0.k7XslO-8Kjf58oAQDRFMSai57x5GhzN2jDhESQocfSI'
}
r = urllib.request.urlopen(urllib.request.Request(url, headers=headers))
data = json.loads(r.read().decode())
for entry in data:
    print(entry.get('entry', entry.get('content', ''))[:120])
    print('---')