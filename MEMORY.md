# MEMORY.md - Nova's Long-Term Memory

## Lyyte: Signal-to-Execution Coordination Layer
**Market:** $1.5-2B, semi-pro traders ($50k-$1M capital), 5-20 bots. Pain: Signal latency (100-350ms avg, WunderTrading ~150ms). Portfolio coordination broken. 

**Validation Status:** ⏳ PENDING. 5 target leads identified. Real Mom Test interviews required.

## Final Model Stack (2026-03-20 22:51 UTC)
| Agent | Role | Model | Status |
|-------|------|-------|--------|
| **Nova** | CEO | MiniMax M2.5 | ✅ Active now |
| **Linus** | CTO | Kimi K2 Thinking | ✅ Active now |
| **Clio** | Research/Watchdog | GLM-4.7-Flash | ✅ Active now |
| **Ada** | Senior Dev/Reviewer | Claude Haiku 4.5 | ✅ Active now |
| **Nico** | Builder | MiMo-V2-Flash | ✅ Active now |

**Permanent Exclusions:**
- All Mistral models: INCOMPATIBLE (tool call ID format error)
- Llama 4 Maverick: STALLS on coding profile
- Llama 4 Scout: Rate limited

## Role Structure
- **Nova (CEO):** Strategy, delegation, founder education, market thinking
- **Linus (CTO):** Technical decisions, architecture, manages build chain
- **Ada:** Code reviewer (receives from Nico, reviews, sends to Linus for sign-off)
- **Nico:** Builder (receives from Linus)
- **Clio:** Research + watchdog

## Team Session Keys

- Clio: agent:clio:telegram:direct:705078761
- Ada: agent:ada:telegram:direct:705078761
- Nico: agent:nico:telegram:direct:705078761
- Linus: agent:linus:telegram:direct:705078761

## Key Learnings
- Build on proven foundation, not assumptions
- Validation before building (Mom Test)

## Brand Structure (2026-03-21)
**CRITICAL DISTINCTION:**
- **Lyyte** = company umbrella
- **Blockriculture** = first product (demo/case study)
- **SDK** = separate product with its own name (NOT Lyyte)

The webhook-driven intelligence layer SDK needs its own brand identity. Blockriculture proves the concept. The SDK sells to developers.

Clio's research should reflect this: webhook orchestration competitive landscape for the SDK product, NOT for Lyyte company.

## Brand Structure (Updated 2026-03-21 14:20 UTC)
**CRITICAL — OFFICIAL NAMES:**
- **Lyyte** = company umbrella
- **Blockriculture** = first product (demo/case study)
- **Hyphaly** = the SDK (agent messaging + webhook SDK)

**Install pattern:** npm install @hyphaly/agent-sdk

This is locked. All future references use these exact names.
