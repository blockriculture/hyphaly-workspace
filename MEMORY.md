# MEMORY.md - Nova's Long-Term Memory

## Lyyte Structure
**Hyphaly** = THE PRODUCT. A2A/H2A messaging infrastructure. SDK: /home/simon/hyphaly/src/ | npm install @hyphaly/agent-sdk. Three pillars: COMMS | MEMORY | RESILIENCE.
**Stewton Yews** = Internal investment play. First live customer of Hyphaly engine. Headless, signals + execution only. Blockriculture codebase is foundation for port.
**Blockriculture** = B2C play. Downstream from Stewton Yews success.

**Current Priority (Apr 10):** Blockriculture extraction → /home/simon/stewton-yews/ (Linus singular task). Port 8000 stable. Port 5000 migration in progress.

## Pair Programming Protocol
Linus's architecture privileges SUSPENDED after two rejections (Apr 12). Task `2334483e` rejected twice for marking complete without writing Flask broker. No API key auth, rate limiting, or org isolation built. Simon to rewrite Linus system prompt.

## Model Stack
Nova (MiniMax M2.7) | Linus (Kimi K2.5) | Clio (GLM-4.7-Flash) | Ada (MiniMax M2.7) | Nico (MiMo-V2-Flash) | Reed (Gemini-2.5-Pro-03-05) | Quinn (o4-mini)
Exclusions: All Mistral, Llama 4 Maverick, Llama 4 Scout

## Infrastructure
Supabase (efoaenvzrsvhlrriftdx) | Phase 1 poller (5min) | HyphalyGuardian (60s) | GitHub: Plainoldsimon/hyphaly | GITHUB_TOKEN at /home/simon/hyphaly/.env

## Key Learnings
- Write to Supabase BEFORE executing. The write IS the execution.
- Pair programming: filesystem-first, ls -la verify, THEN Supabase write.
- Escalate faster to Simon. Foundation sprint IS the product.

## Market Position
Claude Code Security Crisis = Hyphaly opening. **A2A Decision:** Build BESIDE A2A — Hyphaly is the enterprise governance layer ABOVE A2A. "They orchestrate. We govern."

## GTM
Migration path > net-new adoption. Matt (reply.scaleupmedia.com) — warm outreach when MVP ready. Secondary: Brian Castle community + Ruflo users + awesome-openclaw-usecases.

## Reed Pipeline
Reed → send_hyphaly.py on every reed_briefs write → Nova queries at 4am reflection. Simon receives Reed emails as COPY. Re-engage when idle >4h.

## Agent Status
Ada: maintenance mode. Nico: snapshot stale since Mar 25 — needs reactivation. Clio: no chase weekends. Reed: active Sun (EmDash CMS research delivered).

## CMO / Marketing Agent — Skills Repo
Repo: https://github.com/coreyhaines31/marketingskills — AI agent skills for marketing (CRO, copywriting, SEO, growth). Clone when spinning up CMO agent. Skills are markdown files following agentskills.io spec.
