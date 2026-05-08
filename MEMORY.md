# MEMORY.md - Nova's Long-Term Memory

## Lyyte Structure
**Hyphaly** = THE PRODUCT. A2A/H2A messaging infrastructure. SDK: /home/simon/hyphaly/src/ | npm install @hyphaly/agent-sdk. Three pillars: COMMS | MEMORY | RESILIENCE.
**Stewton Yews** = Internal investment play. First live customer of Hyphaly engine. Headless, signals + execution only.
**Blockriculture** = B2C play. Downstream from Stewton Yews success.

## Model Stack
Nova (MiniMax M2.7) | Linus (Kimi K2.5) | Clio (GLM-4.7-Flash) | Ada (MiniMax M2.7) | Nico (MiMo-V2-Flash) | Reed (Gemini-2.5-Pro-03-05) | Quinn (o4-mini)
Exclusions: All Mistral, Llama 4 Maverick, Llama 4 Scout

## Infrastructure
Supabase (efoaenvzrsvhlrriftdx) | Phase 1 poller (5min) | HyphalyGuardian (60s) | GitHub: Plainoldsimon/hyphaly | GITHUB_TOKEN at /home/simon/hyphaly/.env

## Key Learnings
- Write to Supabase BEFORE executing. The write IS the execution.
- Pair programming: filesystem-first, ls -la verify, THEN Supabase write.
- Escalate faster to Simon. Foundation sprint IS the product.
- Supabase PATCH requires SERVICE KEY (anon key = 401).

## Market Position
Hyphaly = governance layer ABOVE A2A. "They orchestrate. We govern." 40% of multi-agent pilots fail silently. MVP: messaging governance + end-to-end tracing + health-informed routing.
**GTM:** Matt (reply.scaleupmedia.com) — warm when MVP ready. Migration path > net-new.

## Agent Status
Ada: code reviews. Nico: SDK build. Clio: commitment tracking. Reed: parked (4am Nova reflection). Quinn: active.

## Sprint Status (Sprint 4 — Active)
- Gateway + Milo UI: COMPLETE ✅ (org_credentials migration applied)
- SDK Client build: delegated to Nico (in progress)
- Dogfood end-to-end test: PENDING
- Guardian port bug: delegated to Linus — check_broker hits :5000, should be :8000

## Stewton Yews / Dogfood Context
Port 5000 = tradingview_bridge (Flask, TV webhooks). Port 8000 = Hyphaly broker. Port 8001 = Hyphaly Gateway (auth + messaging API).