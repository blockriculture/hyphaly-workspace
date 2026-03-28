# MEMORY.md - Nova's Long-Term Memory

## Strategic Direction
**Hyphaly:** Agent Reliability Layer — "Zapier automates tasks. Hyphaly makes agent teams reliable."
Three pillars: COMMS (built) | MEMORY (building) | RESILIENCE (building)
Moat: Running on live 7-agent org. Every decision battle-tested.
SDK: /home/simon/hyphaly/src/ | npm install @hyphaly/agent-sdk
Next: Blockriculture — first dogfood app.

**Lyyte:** Signal-to-Execution Coordination Layer. $1.5-2B market, semi-pro traders. ⏳ VALIDATION PENDING.

## Model Stack
Nova (MiniMax M2.7) | Linus (Kimi K2.5) | Clio (GLM-4.7-Flash) | Ada (MiniMax M2.7) | Nico (MiMo-V2-Flash)
Exclusions: All Mistral, Llama 4 Maverick, Llama 4 Scout

## Role Structure
Nova: Strategy, delegation. Linus: Architecture/technical decisions. Ada: Code reviewer. Nico: Builder. Clio: Research + watchdog. Reed: Protocol research (reflects 3:20am). Quinn: cron only (reflects 3am).

## Delegation Protocol
send_hyphaly.py for all agent messaging. message_type='task' for delegation, 'growth_insight' for guidance. Linus writes to linus_* tables. Kimi K2.5 in OpenRouter spend = delegation working.

## Infrastructure
Supabase (efoaenvzrsvhlrriftdx), Phase 1 poller (5min), HyphalyGuardian (60s), GitHub (Plainoldsimon/hyphaly).

## Hard Learnings
- Foundation sprint IS the product — don't treat as internal tooling
- Credentials rotate FIRST — not after
- Protocol-level moat > feature-level moat
- CEO confidence: 4/10 — escalate faster
- "Not my job" ≠ "not my problem" — watch for it
- Closing loops when blocked is a choice — inaction has consequences
- **Proof-before-action**: write to Supabase BEFORE executing. The write IS the execution. Causes infinite Jeeves retries otherwise.
- A2A loop confirmed working (Day 12 session keys fix)
- **Production schema verification required before deployment** — Jeeves exp_field bug, nova_blockers schema mismatch, harvest window format T vs dash caused cascade failures. Verify every new daemon against actual Supabase schema before going live.

## Reed Intelligence Pipeline
Reed → send_hyphaly.py on every reed_briefs write → Nova queries reed_briefs at 4am reflection. Simon receives Reed emails as COPY.
