import sys, json, urllib.request

if len(sys.argv) != 2:
    print("Usage: python3 supabase_read.py <table>")
    sys.exit(1)

table = sys.argv[1]
url = f"https://efoaenvzrsvhlrriftdx.supabase.co/rest/v1/{table}?select=*"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVmb2FlbnZ6cnN2aGxycmlmdGR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM1NjczNTgsImV4cCI6MjA4OTE0MzM1OH0.k7XslO-8Kjf58oAQDRFMSai57x5GhzN2jDhESQocfSI"

req = urllib.request.Request(url, headers={'apikey': key, 'Authorization': 'Bearer ' + key})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print(json.dumps(data, indent=2))
except Exception as e:
    print(f"Error: {e}")
