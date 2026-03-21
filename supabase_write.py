#!/usr/bin/env python3
"""Shared Supabase write utility for all agents."""
import json, urllib.request, sys

SUPABASE_URL = "https://efoaenvzrsvhlrriftdx.supabase.co"
ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVmb2FlbnZ6cnN2aGxycmlmdGR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM1NjczNTgsImV4cCI6MjA4OTE0MzM1OH0.k7XslO-8Kjf58oAQDRFMSai57x5GhzN2jDhESQocfSI"

def write(table, data):
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    payload = json.dumps(data).encode()
    req = urllib.request.Request(
        url, payload,
        {'apikey': ANON_KEY, 'Authorization': f'Bearer {ANON_KEY}',
         'Content-Type': 'application/json'},
        method='POST'
    )
    try:
        r = urllib.request.urlopen(req)
        return {'status': r.status, 'ok': True}
    except Exception as e:
        return {'status': 0, 'ok': False, 'error': str(e)}

def patch(table, id, data):
    url = f"{SUPABASE_URL}/rest/v1/{table}?id=eq.{id}"
    payload = json.dumps(data).encode()
    req = urllib.request.Request(
        url, payload,
        {'apikey': ANON_KEY, 'Authorization': f'Bearer {ANON_KEY}',
         'Content-Type': 'application/json',
         'Prefer': 'return=minimal'},
        method='PATCH'
    )
    try:
        r = urllib.request.urlopen(req)
        return {'status': r.status, 'ok': True}
    except Exception as e:
        return {'status': 0, 'ok': False, 'error': str(e)}

def read(table, filters=None, limit=10):
    url = f"{SUPABASE_URL}/rest/v1/{table}?order=created_at.desc&limit={limit}"
    if filters:
        for k, v in filters.items():
            url += f"&{k}=eq.{v}"
    req = urllib.request.Request(
        url,
        headers={'apikey': ANON_KEY, 'Authorization': f'Bearer {ANON_KEY}'}
    )
    try:
        r = urllib.request.urlopen(req)
        return json.loads(r.read())
    except Exception as e:
        return []

if __name__ == "__main__":
    print("Supabase write utility loaded. Import and use write(), patch(), read()")
