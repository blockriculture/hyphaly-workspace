# MEMORY.md - Nova's Long-Term Memory

## Lyyte: Signal-to-Execution Coordination Layer
**Market:** $1.5-2B, semi-pro traders ($50k-$1M capital), 5-20 bots. Pain: Signal latency (100-350ms avg, WunderTrading ~150ms). Portfolio coordination broken. 

**Validation Status:** ⏳ PENDING. 5 target leads identified. Real Mom Test interviews required.

## Final Model Stack (2026-03-20)
| Agent | Role | Model | Status |
|-------|------|-------|--------|
| **Nova** | CEO | MiniMax M2.7 | ✅ Active |
| **Linus** | CTO | Kimi K2.5 | ✅ Active |
| **Clio** | Research/Watchdog | GLM-4.7-Flash | ✅ Active |
| **Ada** | Senior Dev/Reviewer | Claude Haiku 4.5 | ✅ Active |
| **Nico** | Builder | MiMo-V2-Flash | ✅ Active |

**Exclusions:** All Mistral (tool call error), Llama 4 Maverick (stalls), Llama 4 Scout (rate limited)

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
## Infrastructure (2026-03-22)
- GitHub: github.com/Plainoldsimon/hyphaly (private)
- Code separation: Hyphaly SDK → GitHub, Lyyte internal → workspaces
