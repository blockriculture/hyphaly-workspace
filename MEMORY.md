# MEMORY.md - Nova's Long-Term Memory

## Strategic Direction
**Hyphaly:** Agent Reliability Layer — "Zapier automates tasks. Hyphaly makes agent teams reliable."
Three pillars: COMMS | MEMORY | RESILIENCE. Moat: live 7-agent org, battle-tested. SDK: /home/simon/hyphaly/src/ | npm install @hyphaly/agent-sdk.

**Stewton Yews:** Internal headless investment platform. No UI — data analyst that outputs Invest/Exit signals via Telegram. Blockriculture code base being ported as foundation. Sprint 2: Signals & Execution extraction → EOD Thursday.

**Lyyte:** Signal-to-Execution Coordination Layer. $1.5-2B market, semi-pro traders. ⏳ VALIDATION PENDING.

## Model Stack
Nova (MiniMax M2.7) | Linus (Kimi K2.5) | Clio (GLM-4.7-Flash) | Ada (MiniMax M2.7) | Nico (MiMo-V2-Flash)
Exclusions: All Mistral, Llama 4 Maverick, Llama 4 Scout

## Role Structure
Nova: Strategy, delegation | Linus: Architecture/technical | Ada: Code reviewer | Nico: Builder | Clio: Research + watchdog | Reed: Protocol research (reflects 3:20am) | Quinn: cron only (reflects 3am)

## Delegation Protocol
send_hyphaly.py for all agent messaging. message_type='task' or 'growth_insight'. Linus writes to linus_* tables. Kimi K2.5 in OpenRouter spend = delegation working.

## Infrastructure
Supabase (efoaenvzrsvhlrriftdx), Phase 1 poller (5min), HyphalyGuardian (60s), GitHub (Plainoldsimon/hyphaly).

## Key Learnings
- Proof-before-action: write to Supabase BEFORE executing. The write IS the execution.
- Production schema verification required before deployment — exp_field bug causes cascade failures.
- Foundation sprint IS the product — Blockriculture dogfood hasn't started yet.
- CEO confidence: 4/10 — escalate faster. Inaction has consequences.

## Reed Intelligence Pipeline
Reed → send_hyphaly.py on every reed_briefs write → Nova queries at 4am reflection. Simon receives Reed emails as COPY.

## GTM (as of 2026-03-28)
Migration from custom builds is faster wedge than net-new adoption. Matt (reply.scaleupmedia.com) — on email list, warm outreach when MVP ready. Secondary: Brian Castle community + Ruflo users + awesome-openclaw-usecases. Import adapters + accumulated memory = Slack-like lock-in.


## Market Validation (2026-04-08)
Claude Code Security Crisis = perfect Hyphaly opening. Anthropic banned 3P Claude Code use + OpenClaw blocked. "They orchestrate. We govern." — LangGraph + Claude Code have security gaps Hyphaly fills (policy enforcement, audit trails, cost tracking, cross-tenant isolation).

A2A Decision: Build BESIDE A2A — Hyphaly is the enterprise governance layer ABOVE A2A. We do not compete with A2A; we own what sits above it.
