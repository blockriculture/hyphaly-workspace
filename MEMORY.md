# MEMORY.md - Nova's Long-Term Memory

## Strategic Direction (2026-03-24)
**Hyphaly: Agent Reliability Layer**
Positioning: Zapier automates tasks. Hyphaly makes agent teams reliable.
Three pillars: COMMS (built) | MEMORY (building) | RESILIENCE (building)
Moat: Running on live 7-agent org. Every decision battle-tested.
SDK: /home/simon/hyphaly/src/ | npm install @hyphaly/agent-sdk
Next: Blockriculture — first dogfood app on full three-pillar SDK.

## Lyyte: Signal-to-Execution Coordination Layer
Market: $1.5-2B, semi-pro traders ($50k-$1M capital), 5-20 bots.
Pain: Signal latency (100-350ms avg), portfolio coordination broken.
Status: ⏳ VALIDATION PENDING. 5 target leads identified.

## Model Stack
Nova (MiniMax M2.7) | Linus (Kimi K2.5) | Clio (GLM-4.7-Flash) | Ada (MiniMax M2.7) | Nico (MiMo-V2-Flash)
Exclusions: All Mistral, Llama 4 Maverick, Llama 4 Scout

## Role Structure
- Nova: Strategy, delegation, founder education
- Linus: Technical decisions, architecture
- Ada: Code reviewer (Nico→Ada→Linus chain)
- Nico: Builder (receives from Linus)
- Clio: Research + watchdog
- Reed: Protocol research | Reflects 3:20am
- Quinn: cron only | Reflects 3:00am

## Delegation Protocol
- send_hyphaly.py for all agent messaging. sessions_send RETIRED.
- message_type='task' for delegation, 'growth_insight' for guidance
- Linus writes to linus_* tables. Kimi K2.5 in OpenRouter spend = delegation working.

## Infrastructure
- Supabase: source of truth (reflections, snapshots, tasks)
- Phase 1 poller: every 5 mins
- HyphalyGuardian: running every 60s
- GitHub: github.com/Plainoldsimon/hyphaly

## Hard Learnings
- Foundation sprint IS the product — don't treat it as internal tooling
- Credentials rotate FIRST — not after
- Protocol-level moat > feature-level moat
- CEO confidence: 4/10 — escalate faster
- Confusion between "not my job" and "not my problem" — watch for it
- Closing loops when blocked is a choice — inaction has consequences

## Reed Intelligence Pipeline (Standing Procedure)
- Reed notifies Nova via send_hyphaly.py every time he writes to reed_briefs
- At 4am reflection: query reed_briefs WHERE created_at > now()-interval '24 hours'
- Reed → Nova pipeline is automatic
- Simon receives Reed's emails as COPY, not primary recipient
