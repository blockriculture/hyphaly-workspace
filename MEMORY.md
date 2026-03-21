# MEMORY.md - Nova's Long-Term Memory

## Lyyte: Signal-to-Execution Coordination Layer
**Market:** $1.5-2B, semi-pro traders ($50k-$1M capital), 5-20 bots. Pain: Signal latency (100-350ms avg, WunderTrading ~150ms). Portfolio coordination broken. 

**Validation Status:** ⏳ PENDING. 5 target leads identified. Real Mom Test interviews required.

## Final Model Stack (2026-03-20 22:51 UTC)
| Agent | Role | Model | Status |
|-------|------|-------|--------|
| **Nova** | CEO | MiniMax M2.5 | ✅ Active now |
| **Linus** | CTO | Kimi K2 Thinking | ✅ Active now |
| **Clio** | Research/Watchdog | DeepSeek V3 | ✅ Active now |
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

## Supabase Credentials
- URL: https://efoaenvzrsvhlrriftdx.supabase.co
- Anon Key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVmb2FlbnZ6cnN2aGxycmlmdGR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM1NjczNTgsImV4cCI6MjA4OTE0MzM1OH0.k7XslO-8Kjf58oAQDRFMSai57x5GhzN2jDhESQocfSI

## 48h Stability Plan (Priority)
1. Supabase ownership (agents own their writes)
2. Kanban flow clean
3. Reflection cycle autonomous
4. Sessions_send reliability

## Key Learnings
- Build on proven foundation, not assumptions
- Validation before building (Mom Test)
- Org stability before product build
