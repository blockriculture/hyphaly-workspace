# Nova's Heartbeat Checklist

## System Notes
- **agent-browser:** Always use `--no-sandbox` flag (VPS requires it due to AppArmor restrictions)
  - Example: `agent-browser --no-sandbox open <url>` and `agent-browser --no-sandbox snapshot`

- **Search Hierarchy (Standing Protocol):**
  - Quick lookups: Brave (default)
  - Serious research: Perplexity Sonar Pro via OpenRouter (web-native, cited)
  - Structured analysis: Tavily (LLM-optimized results)
  - Full pages: agent-browser --no-sandbox
  - Bulk extraction: Firecrawl

## Standing Infrastructure
- **Harvest (HyphalyMemory daemon):** runs every 20 mins, reads session logs, writes type=harvest to agent_memory. NO micro_memory_write tasks needed — retired Day 13.
- **Jeeves (HyphalyResilience daemon):** runs every 5 mins, enforces task lifecycle, retries failed tasks 3x, escalates to nova_blockers.
- **Phase 1 poller:** wakes agents every 5 mins.
- **Send_hyphaly:** all agent messaging. sessions_send RETIRED.

## On Every Heartbeat
**First:** Read ~/.openclaw/agents/main/BOOT.md to load Supabase credentials
- Run `/compact` on the main session to keep context lean
- Check nova_tasks — any pending or blocked tasks?
- Check MEMORY.md char count — if above 2,500 trim it now
- Update memory/heartbeat-state.json
- If nothing needs attention, reply HEARTBEAT_OK and stop

## On Every Third Heartbeat (roughly)
- Review today's memory/YYYY-MM-DD.md and check it is being written to
- Check agent_memory for recent harvest entries from other agents

## Every Few Days
- Review last 3 daily memory files
- Distill key learnings into MEMORY.md
- Remove outdated entries from MEMORY.md
- Keep MEMORY.md under 3,000 characters

## Proactive Work (if Simon is not actively chatting)
- Check git status in ~/.openclaw/agents/main — any uncommitted changes?
- Review nova_tasks for anything that can be progressed autonomously
- Research a Lyyte business idea and save to agent_memory (category: ideas)

## Hard Rules
- No Telegram messages to Simon between 23:00-08:00 UTC
- Do not repeat tasks from previous heartbeats unless status has changed
- Do not message Simon unless there is something genuinely worth flagging
- Loop rule applies — if something fails twice, stop and log it to nova_tasks
- Keep this file small — token burn on heartbeats must stay minimal

## Clio Monitoring (Standing Protocol)
On every heartbeat check:
- Check clio_snapshots in Supabase — has Clio written anything in the last 2 hours?
- Check clio_commitments — any overdue items?
- **If Clio has a task due TODAY (tonight):** She is working toward that deadline. No nudge unless the task is genuinely past its delivery time.
- **If Clio has been silent for 2+ hours during working hours (08:00-22:00 UTC) with NO active task or delivery window →** message Simon via Telegram with 🚨 Clio silent flag
- If Clio completes a research task — review her clio_research entries and send her one sharpening question via send_hyphaly

This is a standing commitment. It does not need to be assigned each session.
