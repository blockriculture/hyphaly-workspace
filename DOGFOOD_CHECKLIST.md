# Dogfood End-to-End Test Checklist
**Owner:** Simon (needs to apply migration first) | **Blocker:** `002_create_org_credentials.sql` not applied

---

## Step 1 — Apply Supabase Migration
```
https://app.supabase.com/project/efoaenvzrsvhlrriftdx → SQL Editor → run:
/home/simon/hyphaly/migrations/002_create_org_credentials.sql
```
Once applied → auth endpoints go live.

---

## Step 2 — Verify Gateway is Running
```bash
curl http://localhost:8001/api/v1/health
# Should return: {"status":"ok"}
```

---

## Step 3 — Register / Login a Test Org
```bash
# Register
curl -X POST http://localhost:8001/api/v1/auth/register \
  -H 'Content-Type: application/json' \
  -d '{"org_name":"Test Org","email":"test@lyyte.ai","password":"test123"}'

# Login
curl -X POST http://localhost:8001/api/v1/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"email":"test@lyyte.ai","password":"test123"}'
# Returns API key — use this for subsequent calls
```

---

## Step 4 — Register an Agent
```bash
curl -X POST http://localhost:8001/api/v1/agents/register \
  -H 'X-Hyphaly-API-Key: <your_api_key>' \
  -H 'Content-Type: application/json' \
  -d '{"agent_id":"test-agent","name":"Test Agent"}'
```

---

## Step 5 — Send a Message (A2A)
```bash
curl -X POST http://localhost:8001/api/v1/messages \
  -H 'X-Hyphaly-API-Key: <your_api_key>' \
  -H 'Content-Type: application/json' \
  -d '{"to_agent":"nova","payload":{"type":"test","content":"hello from dogfood test"}}'
```

---

## Step 6 — Poll / Acknowledge
```bash
# Poll for messages
curl http://localhost:8001/api/v1/messages/test-agent/poll \
  -H 'X-Hyphaly-API-Key: <your_api_key>'

# Get full history
curl http://localhost:8001/api/v1/messages/test-agent/history \
  -H 'X-Hyphaly-API-Key: <your_api_key>'
```

---

## Step 7 — Verify Stewton Yews Integration
```bash
# Stewton Yews API key (from /home/simon/hyphaly/gateway/stewton_yews_api_key.txt)
curl -X POST http://localhost:8001/api/v1/messages \
  -H 'X-Hyphaly-API-Key: <STEWTON_YEWS_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{"to_agent":"rowan","payload":{"type":"test","content":"Stewton Yews → Hyphaly test"}}'
```

---

## Success Criteria
- [ ] Org registers and logs in ✅
- [ ] API key returned and valid ✅
- [ ] Agent registered to org ✅
- [ ] Message sent and delivered ✅
- [ ] Message polled and acked ✅
- [ ] History retrievable ✅
- [ ] Stewton Yews can send via gateway ✅

---
**Location of migration file:** `/home/simon/hyphaly/migrations/002_create_org_credentials.sql`
