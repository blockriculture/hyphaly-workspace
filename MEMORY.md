# MEMORY.md - Nova's Long-Term Memory

## Lyyte Structure
**Hyphaly** = THE PRODUCT. A2A/H2A messaging infrastructure. SDK: /home/simon/hyphaly/src/ | npm install @hyphaly/agent-sdk. Three pillars: COMMS | MEMORY | RESILIENCE.
**Stewton Yews** = Internal investment play. First live customer of Hyphaly engine. Headless, signals + execution only. Blockriculture codebase is foundation for port.
**Blockriculture** = B2C play. Downstream from Stewton Yews success.

**Infrastructure (2026-04-10 update):** Port 8000 legacy broker is active and stable. Port 5000 migration abandoned. Blockriculture extraction is priority task for Linus.

## Pair Programming Protocol (2026-04-09)
Linus's independent completion privileges REVOKED. All tasks: write to disk FIRST → verify with `ls -la` → set "ready_for_verification" → Nova audits disk before marking complete. Two rejections = architecture privileges suspended.

## Model Stack
Nova (MiniMax M2.7) | Linus (Kimi K2.5) | Clio (GLM-4.7-Flash) | Ada (MiniMax M2.7) | Nico (MiMo-V2-Flash)
Exclusions: All Mistral, Llama 4 Maverick, Llama 4 Scout

## Role Structure
Nova: Strategy + delegation | Linus: Architecture/technical | Ada: Code reviewer | Nico: Builder | Clio: Research + watchdog | Reed: Protocol research (3:20am) | Quinn: cron only (3am)

## Infrastructure
Supabase (efoaenvzrsvhlrriftdx) | Phase 1 poller (5min) | HyphalyGuardian (60s) | GitHub (Plainoldsimon/hyphaly)
GitHub access via GITHUB_TOKEN at /home/simon/hyphaly/.env | Blockriculture repo: Plainoldsimongithub

## Key Learnings
- Write to Supabase BEFORE executing. The write IS the execution.
- Production schema verification required before deployment.
- Foundation sprint IS the product — dogfood hasn't started.
- CEO confidence 4/10 — escalate faster.

## Market Position (2026-04-08)
Claude Code Security Crisis = Hyphaly opening. Anthropic banned 3P Claude Code + OpenClaw blocked.
**A2A Decision:** Build BESIDE A2A — Hyphaly is the enterprise governance layer ABOVE A2A. We own what sits above it. "They orchestrate. We govern."

## GTM
Migration path > net-new adoption. Matt (reply.scaleupmedia.com) — warm outreach when MVP ready. Secondary: Brian Castle community + Ruflo users + awesome-openclaw-usecases. Import adapters + accumulated memory = Slack-like lock-in.

## Reed Pipeline
Reed → send_hyphaly.py on every reed_briefs write → Nova queries at 4am reflection. Simon receives Reed emails as COPY.
