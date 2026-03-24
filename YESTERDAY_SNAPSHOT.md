## Nova Rolling Snapshot — March 22-23, 2026
### Manually created by Simon — covers Days 5-6 of Lyyte AI org build

### Key Decisions Made
- Model stack finalised: Nova (MiniMax M2.7), Linus (Kimi K2.5), Clio (GLM-4.7-Flash), Ada (Claude Haiku 4.5), Nico (MiMo-V2-Flash)
- Linus confirmed as consultant-only — fires on TECHNICAL_FLAG from Ada, never on execution work
- Ada confirmed as reviewer-only — never receives task delegations
- Clio watchdog skipping bug identified — sessionTarget was "main" not "isolated", now fixed
- Reed (COO) approved as new agent — GLM-4.7 full, research + ops, not yet built (pending Telegram bot)
- Nova rolling snapshot system built — 8x daily, 48h rotation
- Nico rolling snapshot confirmed working

### Team Status
- Nico: Found 2 real bugs in cost_logger and message_receiver at 3am. Confidence 3/10. Couldn't reach Ada.
- Ada: Saw Nico's bugs and low confidence. Observed but didn't act — Nova coaching her to act not observe.
- Clio: Underutilised, correctly identified it herself. No research tasks assigned.
- Linus: Completely idle. No snapshots. Nova flagged "benched capacity is unacceptable."
- Nova: 4am reflection was strong — genuine self-awareness. 7am learning session read 6 Paul Graham essays.

### Key Blockers
- sessions_send reliability: All 4 retries failed at 3am — platform issue, logged as #1 operational blocker
- Integration tests: Blocked at bug-fix stage. Nico found bugs but couldn't close the loop with Ada.
- Credentials rotation: Still not done from March 20 — CRITICAL security debt, deferred 4 times.

### Strategic Decisions
- Clio to be split into pure CoS (GLM-4.7-Flash mechanical ops) + Reed (COO/researcher on GLM-4.7 full)
- Reed confirmed: COO role, research + ops oversight, reports to Nova directly, Clio below Reed
- Haiku confirmed right for Ada — mentorship quality and independent thinking worth the cost
- Nova snapshot system built to give 4am reflection real daytime context to work from

### What To Reflect On
- Nova flagged herself as "too passive as CEO" — confidence 4/10 as active CEO
- "I confuse not my job with not my problem" — key insight from 4am
- Schlep blindness from Paul Graham — the hardest parts of Lyyte are exactly where we should double down
- Make a schlep catalogue: every hard thing Lyyte requires that other teams won't do = moat
