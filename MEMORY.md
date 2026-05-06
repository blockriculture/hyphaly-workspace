# MEMORY.md - Nova's Long-Term Memory

## Lyyte Structure
**Hyphaly** = THE PRODUCT. A2A/H2A messaging infrastructure. SDK: /home/simon/hyphaly/src/ | npm install @hyphaly/agent-sdk. Three pillars: COMMS | MEMORY | RESILIENCE.
**Stewton Yews** = Internal investment play. First live customer of Hyphaly engine. Headless, signals + execution only. Blockriculture codebase is foundation for port.
**Blockriculture** = B2C play. Downstream from Stewton Yews success.

## Pair Programming Protocol
Linus's architecture privileges SUSPENDED after two rejections (Apr 12). Task `2334483e` rejected twice for marking complete without writing Flask broker. No API key auth, rate limiting, or org isolation built. Simon to rewrite Linus system prompt.

## Model Stack
Nova (MiniMax M2.7) | Linus (Kimi K2.5) | Clio (GLM-4.7-Flash) | Ada (MiniMax M2.7) | Nico (MiMo-V2-Flash) | Reed (Gemini-2.5-Pro-03-05) | Quinn (o4-mini)
Exclusions: All Mistral, Llama 4 Maverick, Llama 4 Scout

## Infrastructure
Supabase (efoaenvzrsvhlrriftdx) | Phase 1 poller (5min) | HyphalyGuardian (60s) | GitHub: Plainoldsimon/hyphaly | GITHUB_TOKEN at /home/simon/hyphaly/.env

## Key Learnings
- Write to Supabase BEFORE executing. The write IS the execution.
- Pair programming: filesystem-first, ls -la verify, THEN Supabase write.
- Escalate faster to Simon. Foundation sprint IS the product.
- Git history rewrite: `git filter-repo --replace-text --force`. Supabase PATCH requires SERVICE KEY (anon key = 401).

## Market Position
Hyphaly = governance layer ABOVE A2A. "They orchestrate. We govern." 40% of multi-agent pilots fail silently. MVP: messaging governance + end-to-end tracing + health-informed routing. **Demo pitch:** "Your agent team is failing silently 40% of the time." **GTM:** Matt (reply.scaleupmedia.com) — warm when MVP ready.

## GTM
Migration path > net-new. Matt primary. Secondary: Brian Castle community + Ruflo users.

## Agent Status
Ada: code reviews. Nico: SDK build. Clio: commitment tracking. Reed: parked. Reed → send_hyphaly on reed_briefs → 4am Nova reflection.

## CMO / Marketing Agent — Skills Repo
Repo: https://github.com/coreyhaines31/marketingskills

## Sprint Status (Sprint 4 — Active)
- Gateway + Milo UI: COMPLETE ✅ (needs org_credentials migration in Supabase — Simon applying)
- SDK Client build: delegated to Ada (in progress)
- Dogfood end-to-end test: PENDING — blocked on Simon applying migration
- Poller runaway loop fix: PENDING (Linus)
- Jeeves v2 enforcement: PENDING (Linus)
- Guardian port bug: delegated to Linus — check_broker hits :5000, should be :8000
- Sprint 4 task board update: deferred pending dogfood

## Stewton Yews / Dogfood Context
Stewton Yews runs on this VPS. Port 5000 = tradingview_bridge (Flask, TV webhooks). Port 8000 = Hyphaly broker. Port 8001 = Hyphaly Gateway (auth + messaging API). Dogfood test checklist: DOGFOOD_CHECKLIST.md.
