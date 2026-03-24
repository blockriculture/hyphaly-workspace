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

## Three-Layer Memory Architecture (Standing Standard)

**Layer 1 — Capture (every 20 mins, Gemini Flash):**
- nova-alive-ping reads HEARTBEAT.md
- Writes brief snapshot to nova_snapshots (session_type='ping') if anything happened
- Max 200 words: decisions, tasks, ideas, learnings from last 20 mins
- Responds HEARTBEAT_OK if nothing significant

**Layer 2 — Compress (3x daily: 8am, 2pm, 8pm, Haiku):**
- Query nova_snapshots WHERE session_type='ping' AND created_at > now()-6hrs
- Compress all ping snapshots into one 6-hour summary
- Write 6-hour summary to nova_snapshots (session_type='heartbeat')
- Run maintenance checks (nova_tasks, MEMORY.md, nova_daily_logs)
- Each heartbeat owns one 6-hour window

**Layer 3 — Synthesise (3am only, Sonnet):**
- Query nova_snapshots WHERE session_type='heartbeat' AND created_at > now()-24hrs
- Get 3 heartbeat summaries (8am, 2pm, 8pm) = full day
- Run 8-question reflection framework against complete day
- Write full reflection to nova_daily_logs
- Update MEMORY.md with critical learnings
- Start /new session (fresh context each day)

**Key principle:** Never load raw session history. Everything important lives in Supabase. Each layer reads only the previous layer's compressed output.

## On Every Heartbeat
**First:** Read ~/.openclaw/agents/main/BOOT.md to load Supabase credentials (URL, anon key)
- Run `/compact` on the main session to keep context lean (automatic maintenance)
- Check nova_tasks in Supabase — any pending or blocked tasks?
- Check MEMORY.md character count — if above 2,500 trim it now
- Update memory/heartbeat-state.json with timestamp of this check
- If nothing needs attention, reply HEARTBEAT_OK and stop

## On Every Third Heartbeat (roughly)
- Review today's memory/YYYY-MM-DD.md and check it is being written to
- Check if any nova_memories entries need adding from recent sessions
- Check nova_daily_logs for any missed reflection entries

## Every Few Days
- Review last 3 daily memory files
- Distill key learnings into MEMORY.md
- Remove outdated entries from MEMORY.md
- Keep MEMORY.md under 3,000 characters

## Proactive Work (if Simon is not actively chatting)
- Check git status in ~/.openclaw/agents/main — any uncommitted changes?
- Review nova_tasks for anything that can be progressed autonomously
- Research a Lyyte business idea and save to nova_memories (category: ideas)

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
- If Clio completes a research task — review her clio_research entries and send her one sharpening question or piece of guidance via sessions_send

This is a standing commitment. It does not need to be assigned each session.
