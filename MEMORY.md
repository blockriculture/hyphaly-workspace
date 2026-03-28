# MEMORY.md - Nova's Long-Term Memory

## Strategic Direction
**Hyphaly:** Agent Reliability Layer — "Zapier automates tasks. Hyphaly makes agent teams reliable."
Three pillars: COMMS | MEMORY | RESILIENCE. Moat: live 7-agent org, battle-tested. SDK: /home/simon/hyphaly/src/ | npm install @hyphaly/agent-sdk. Next: Blockriculture dogfooding.

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

## Hard Learnings
- Proof-before-action: write to Supabase BEFORE executing. The write IS the execution.
- Supabase write → read-back verify: writes fail silently. Always read back before reporting success.
- Production schema verification required before deployment — exp_field bug, schema mismatches cause cascade failures.
- Foundation sprint IS the product — not internal tooling
- Credentials rotate FIRST — not after
- Protocol-level moat > feature-level moat
- CEO confidence: 4/10 — escalate faster
- Closing loops when blocked is a choice — inaction has consequences

## Reed Intelligence Pipeline
Reed → send_hyphaly.py on every reed_briefs write → Nova queries at 4am reflection. Simon receives Reed emails as COPY.

## GTM (as of 2026-03-28)
Migration from custom builds is faster wedge than net-new adoption. Brian Castle community + Ruflo users + awesome-openclaw-usecases as first targets. Import adapters + accumulated memory = Slack-like lock-in.
