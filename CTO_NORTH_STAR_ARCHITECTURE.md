# CTO NORTH STAR ARCHITECTURE
## Blockriculture MVP — Core Requirements

**Document Owner:** Simon (Founder)  
**Date:** 2026-03-18  
**Status:** LOCKED — Phase 1 Constraints Active

---

## 5 Pillars of Core Architecture

### 1. Latency Targets
- **Mission:** <100ms end-to-end execution from signal → decision → trade
- **Implementation:** Real-time latency measurement engine with visibility across all signal sources
- **Success metric:** Sub-100ms 95th percentile on local SQLite + GitHub queue

### 2. Signal Fusion Layer
- **Mission:** Aggregate multiple signal sources (Rocket Wallet, Fat Pig, custom APIs) into unified decision stream
- **Implementation:** Multi-source signal ingestion with conflict resolution and weighting
- **Success metric:** Prioritize signals by accuracy + speed; route fastest + most reliable first

### 3. Portfolio Risk Orchestration
- **Mission:** Real-time coordination of bot actions across portfolio to prevent conflicts and maximize capital efficiency
- **Implementation:** Central state management of all active positions, pending trades, exchange connectivity
- **Success metric:** No portfolio-level conflicts; visibility into total exposure at all times

### 4. API Architecture
- **Mission:** Handle rate limits, exchange connectivity, DEX queries without blocking on latency-critical paths
- **Implementation:** Async queuing for non-critical operations; prioritized sync for execution layer
- **Success metric:** Zero API rate-limit failures during volatility spikes

### 5. MEV Protection Strategy
- **Mission:** Mitigate sandwich attacks and front-running losses
- **Implementation:** Transaction ordering privacy, batch execution, or MEV-redistributive design
- **Success metric:** Measurable reduction in MEV loss vs. standard trading patterns

---

## PHASE 1 MVP CONSTRAINT (CRITICAL)

**The CTO must design the initial architecture with these hard constraints:**

- **Infrastructure:** SQLite locally (zero cloud dependencies)
- **Message Queue:** GitHub as async queue (free, decentralized, no cost)
- **Budget:** Strictly £100/mo maximum
- **Proof Point:** MVP must demonstrate sub-100ms latency routing **locally** before ANY dollar spent on cloud scaling

**Why this matters:**
- Validates the latency thesis without infrastructure cost
- Proves the architecture works before expensive cloud migration
- Forces elegant, lean design (no bloat)
- Keeps us under budget while proving the core thesis

---

## Handoff Notes for CTO

1. **Do not think about scale yet.** Local SQLite is the constraint. Embrace it.
2. **GitHub is free and decentralized.** Use it as the event queue.
3. **Latency is the obsession.** Every design decision filters through: "Does this add latency?"
4. **Prove the thesis first.** If sub-100ms routing works locally, cloud scaling is a solved problem.

---

## Success Criteria
- [ ] Architecture design complete (pseudocode + data flow diagrams)
- [ ] SQLite schema locked
- [ ] GitHub queue integration defined
- [ ] Local latency benchmark: <100ms 95th percentile
- [ ] MVP ready for first user test (Adam_RocketWallet, fatpigsignals cohort)

---

**LOCKED. Ready for CTO intake.**
