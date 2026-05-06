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
- Git history rewrite: `git filter-repo --replace-text <patterns.txt> --force` cleans secrets. Re-add origin remote after. Force push.
- Supabase PATCH/UPDATE requires SERVICE KEY — anon key gets 401. Always use service key for patches.

## Market Position (Updated 2026-04-14)
Build BESIDE A2A — Hyphaly is the enterprise governance layer ABOVE A2A. "They orchestrate. We govern." Clio confirmed: no existing tools address A2A message governance. 40% of multi-agent pilots fail within 6 months. MVP: bidirectional messaging governance + end-to-end tracing + health-informed routing. **Demo pitch:** "Your agent team is failing silently 40% of the time." **GTM:** Matt (reply.scaleupmedia.com) — warm when MVP ready. clio_research: aa129c3c

## GTM
Migration path > net-new adoption. Matt (reply.scaleupmedia.com) — warm outreach when MVP ready. Secondary: Brian Castle community + Ruflo users + awesome-openclaw-usecases.

## Agent Status
Ada: active, doing code reviews + daily reflections. Nico: active, Memory Curator build. Clio: active, commitment tracking + inbox digest (last 08:03 UTC today). Reed: parked pending customer signal. Reed → send_hyphaly on reed_briefs writes → 4am Nova reflection.

## CMO / Marketing Agent — Skills Repo
Repo: https://github.com/coreyhaines31/marketingskills

## Sprint Status (Sprint 4 — Active)
- Linus: Hyphaly Gateway build + deploy — COMPLETE ✅
- Milo: Blockriculture UI readiness assessment — COMPLETE ✅
- Nico: Hyphaly SDK Client build — delegated to Ada (in progress)
- Dogfood: End-to-end test with Stewton Yews — PENDING (needs Simon)
- Linus: Poller runaway loop fix — PENDING
- Linus: Jeeves v2 enforcement — PENDING
- Nova: Sprint 4 task board update — PENDING (me)
