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

## Brand Structure (LOCKED)
- **Lyyte** = company umbrella
- **Blockriculture** = first product (demo)
- **Hyphaly** = SDK (agent messaging + webhooks)
- Install: `npm install @hyphaly/agent-sdk`

## Context (2026-03-22)
- Credentials rotation: Monday priority
- sessions_send reliability: ongoing infra issue
- Domain: Hyphaly.com secured

## Hyphaly Architecture (LOCKED)
1. Multi-tenant from day one (isolated silos)
2. Ephemeral messaging (route, don't store)
3. Server-side handshake (moat)
4. Proprietary message envelope

**Pricing:** Free 1k msgs/mo → Pro £49/mo → Enterprise custom

## Key Learnings
- Build on proven foundation, not assumptions
- Validation before building (Mom Test)
- Credentials rotate FIRST (not after)
## Infrastructure
GitHub: github.com/Plainoldsimon/hyphaly (private). Credentials rotation overdue (was March 20).

## Critical Technical Debt
1. Credentials rotation — CRITICAL, OVERDUE
2. sessions_send reliability — blocking team coordination
3. GitHub remote not configured — no workspace backups

## Key Learnings
- Build on proven foundation, not assumptions
- Validation before building (Mom Test)
- Credentials rotate FIRST (not after)
- Protocol-level moat > feature-level moat
- Closing loops when blocked is a choice — inaction has consequences
- Protocol-level moat > feature-level moat (prompt-learnable, no fine-tuning)
- Closing loops when blocked is a choice — inaction has consequences

## Org Expansion (2026-03-23 18:35 UTC)
**NEW AGENTS:**
- **Reed**: agent:reed:telegram:direct:705078761 | Reflects 3:20am
- **Quinn**: cron only (no Telegram) | Reflects 3:00am

**Full team (7 agents):**
- Nova (CEO) — MiniMax M2.7
- Linus (CTO) — Kimi K2.5
- Clio (Research) — GLM-4.7-Flash
- Ada (Sr Dev) — MiniMax M2.7
- Nico (Builder) — MiMo-V2-Flash
- Reed (new) — TBD
- Quinn (new) — TBD

Include Reed + Quinn in 4am team read.
