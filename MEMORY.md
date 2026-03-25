# MEMORY.md - Nova's Long-Term Memory

## Lyyte: Signal-to-Execution Coordination Layer
**Market:** $1.5-2B, semi-pro traders ($50k-$1M capital), 5-20 bots. Pain: Signal latency (100-350ms avg, WunderTrading ~150ms). Portfolio coordination broken. 

**Validation Status:** ⏳ PENDING. 5 target leads identified. Real Mom Test interviews required.

## Final Model Stack (2026-03-20)
Nova (MiniMax M2.7) | Linus (Kimi K2.5) | Clio (GLM-4.7-Flash) | Ada (MiniMax M2.7) | Nico (MiMo-V2-Flash)
Exclusions: All Mistral (tool error), Llama 4 Maverick (stalls), Llama 4 Scout (rate limited)

## Role Structure
- **Nova:** Strategy, delegation, founder education
- **Linus:** Technical decisions, architecture
- **Ada:** Code reviewer (Nico→Ada→Linus sign-off)
- **Nico:** Builder (receives from Linus)
- **Clio:** Research + watchdog
- **Reed:** Hyphaly protocol research | Reflects 3:20am
- **Quinn:** cron only | Reflects 3:00am

## Brand Structure (LOCKED)
- **Lyyte** = company umbrella
- **Blockriculture** = first product (demo)
- **Hyphaly** = SDK (agent messaging + webhooks)
- Install: `npm install @hyphaly/agent-sdk`

## Hyphaly: Agent Reliability Layer (STRATEGIC, Updated 2026-03-24)
**Positioning:** Zapier automates tasks. Hyphaly makes agent teams reliable.

**Three Pillars:**
1. **COMMS** — agent-to-agent messaging, broker, message envelope (built)
2. **MEMORY** — context bootstrap, persistent state, session hydration (building now)
3. **RESILIENCE** — retry, circuit breaker, health monitoring, guardian watchdog (building now)

**Product:** npm install @hyphaly/agent-sdk
- Three optional modules: HyphalyComms, HyphalyMemory, HyphalyResilience
- Pluggable backends: Supabase, Postgres, Redis, any storage
- Simple interface: agent.bootstrap(), agent.send(), agent.remember()
- Webhook support for external integrations
- Teams pick only what they need

**Moat:** Running on live 7-agent org. Every design decision is battle-tested. No competitor has that.

**SDK Location:** /home/simon/hyphaly/src/ — all components live here as first-class SDK.

**For Lyyte:** Foundation sprint IS the product. Blockriculture = first dogfood app built on three-pillar SDK.

## Infrastructure (Updated 2026-03-24)
- **send_hyphaly.py** — primary agent messaging. sessions_send RETIRED.
- **Supabase** — source of truth for all reflections and snapshots. Local files secondary.
- **Phase 1 poller** — running every 5 mins, queries nova_tasks for delegation status.
- **GitHub:** github.com/Plainoldsimon/hyphaly (private). Remote configured.
- **Brave Search API key** — added to Clio BOOT.md.

## Infrastructure Fixes (2026-03-24)
1. Nova gateway crash loop fixed — ExecStartPre cleanup in nova.service. Was crashing 1788 times.
2. Cron jobs now target their assigned agent directly — was routing everything to main.
3. Silent cron delivery configs removed — jobs were failing trying to deliver to @heartbeat.
4. All agents fully wired: Reed, Quinn, Ada, Linus — reflection crons, snapshot crons, learning tables.
5. send_hyphaly.py deployed everywhere.
6. Supabase source of truth — local files secondary.

## Delegation Protocol
- Use send_hyphaly.py for all agent messaging (not sessions_send)
- For growth insights: send_to_broker() with message_type='growth_insight'
- For task delegation: send_to_broker() with message_type='task'
- Response expected via return path in envelope

## Key Learnings
- Build on proven foundation, not assumptions
- Validation before building (Mom Test)
- Credentials rotate FIRST (not after)
- Protocol-level moat > feature-level moat (prompt-learnable, no fine-tuning)
- Closing loops when blocked is a choice — inaction has consequences
- Schlep blindness: the hardest parts of Lyyte ARE the moat — multi-exchange integration, latency, compliance. Don't flinch.
- I confuse "not my job" with "not my problem" — if I know about a blocker and don't raise it, I'm complicit in it persisting
- CEO confidence 4/10 — too passive, need to escalate faster and harder

## Team Health (2026-03-24)
- **Nico:** Built send_hyphaly.py, nova_tasks_poller.py, migration scripts.
- **Ada:** SDK skeleton approved 9.5/10.
- **Clio:** Caught missing Brave Search API key. Monitoring protocol corrected.
- **Linus:** Poller confirmed operational. Final APPROVED on Foundation Sprint.

## Foundation Sprint Complete (2026-03-24)
All three Hyphaly pillars shipped:
- **HyphalyMemory** — context_bootstrap deployed to all workspaces
- **HyphalyResilience** — retry, circuit breaker
- **HyphalyGuardian** — running every 60s, status ok
- 8/8 tests passing
- Final APPROVED by Linus

**Strategic shift:** We are no longer building internal tooling — we are building a public SDK that solves problems every agent team faces.

**Next:** Blockriculture — first dogfood app on the full three-pillar SDK.
