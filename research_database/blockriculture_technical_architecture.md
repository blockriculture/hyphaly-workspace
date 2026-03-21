# Blockriculture: Technical Architecture & Latency Deep-Dive
**Prepared for:** MVP Development Sprint  
**Date:** 2026-03-18  
**Audience:** Engineering, Product Leadership

---

## Executive Summary

To win in the "coordination layer" space, Blockriculture must offer:
1. **Latency measurement & transparency** (core differentiator)
2. **Multi-signal fusion engine** (medium-term moat)
3. **Portfolio-level risk orchestration** (long-term moat)
4. **MEV protection layer** (moonshot; 6-12 months out)

This document outlines the technical approach for MVP (phases 1-2).

---

## Part 1: Latency Measurement & Transparency

### 1.1 Signal Latency Pipeline

```
[Signal Generation]
    ↓ (0.5-5ms)
[Transmission to Blockriculture]
    ↓ (varies: <50ms webhook, 200-500ms Telegram)
[Ingestion & Parsing]
    ↓ (5-20ms)
[Validation & Deduplication]
    ↓ (2-10ms)
[Decision Logic (Rule Evaluation)]
    ↓ (10-50ms)
[Portfolio Risk Check]
    ↓ (20-100ms: depends on portfolio complexity)
[Order Generation]
    ↓ (1-5ms)
[Serialization & Authentication]
    ↓ (1-5ms)
[Exchange API Call]
    ↓ (20-100ms network + 10-50ms exchange queueing)
[Order Placement in Blockchain/Exchange]
    ↓ (depends on target: <1ms for CEX order book, 5-30s for on-chain DEX)
[User Notification]
    ↓ (1-5ms)
[Total: 100-350ms typical; 80-150ms optimized]
```

### 1.2 Latency Measurement Architecture

**Requirement:** Measure each stage independently, in real-time, with millisecond precision.

#### Approach 1: Server-Side Instrumentation (MVP)
```python
# Pseudocode for latency tracking

class SignalProcessor:
    def process_signal(self, signal_data):
        timestamps = {}
        
        # Stage 1: Ingestion
        timestamps['ingestion_start'] = time.time_ns()
        raw_signal = self.parse_webhook(signal_data)
        timestamps['ingestion_end'] = time.time_ns()
        
        # Stage 2: Validation
        timestamps['validation_start'] = time.time_ns()
        validated = self.validate_signal(raw_signal)
        timestamps['validation_end'] = time.time_ns()
        
        # Stage 3: Deduplication
        timestamps['dedup_start'] = time.time_ns()
        is_duplicate = self.check_duplicate(validated)
        timestamps['dedup_end'] = time.time_ns()
        
        # Stage 4: Decision Logic
        timestamps['decision_start'] = time.time_ns()
        decision = self.evaluate_rules(validated)
        timestamps['decision_end'] = time.time_ns()
        
        # Stage 5: Risk Check
        timestamps['risk_check_start'] = time.time_ns()
        risk_ok = self.portfolio_risk_check(decision)
        timestamps['risk_check_end'] = time.time_ns()
        
        # Stage 6: Order Generation
        timestamps['order_gen_start'] = time.time_ns()
        order = self.generate_order(decision)
        timestamps['order_gen_end'] = time.time_ns()
        
        # Stage 7: Exchange API Call
        timestamps['exchange_start'] = time.time_ns()
        result = self.send_to_exchange(order)
        timestamps['exchange_end'] = time.time_ns()
        
        # Calculate latencies
        latencies = {
            'ingestion_ms': (timestamps['ingestion_end'] - timestamps['ingestion_start']) / 1_000_000,
            'validation_ms': (timestamps['validation_end'] - timestamps['validation_start']) / 1_000_000,
            'dedup_ms': (timestamps['dedup_end'] - timestamps['dedup_start']) / 1_000_000,
            'decision_ms': (timestamps['decision_end'] - timestamps['decision_start']) / 1_000_000,
            'risk_check_ms': (timestamps['risk_check_end'] - timestamps['risk_check_start']) / 1_000_000,
            'order_gen_ms': (timestamps['order_gen_end'] - timestamps['order_gen_start']) / 1_000_000,
            'exchange_ms': (timestamps['exchange_end'] - timestamps['exchange_start']) / 1_000_000,
            'total_ms': (timestamps['exchange_end'] - timestamps['ingestion_start']) / 1_000_000,
        }
        
        # Log to database for analytics
        self.log_latency(signal_id, latencies, result)
        
        return result, latencies
```

**Pros:**
- Accurate to millisecond (ns precision)
- Real-time measurement on every signal
- No external dependencies

**Cons:**
- Doesn't capture client-side latency (browser → webhook endpoint)
- Doesn't capture network jitter

#### Approach 2: End-to-End Tracing (Medium-term)
Add client-side beacon + server-side tracing for full visibility:

```python
# Client-side (e.g., TradingView alert sends additional metadata)
# POST /webhook with header: X-Signal-Time: <unix_ns>

# Server-side processing
def process_signal_with_e2e_tracing(self, signal_data, headers):
    server_ingestion_time = time.time_ns()
    client_emit_time = int(headers.get('X-Signal-Time', 0))
    
    network_latency = (server_ingestion_time - client_emit_time) / 1_000_000
    # Continue with processing...
    
    # Log: network_latency (50-100ms typical)
```

### 1.3 Dashboard Requirements

**What traders see in real-time:**

1. **Latency by signal source:**
   - TradingView webhook: avg 150ms, p99 250ms
   - Telegram bot: avg 450ms, p99 800ms
   - On-chain listener: avg 8,000ms, p99 15,000ms

2. **Latency by stage (waterfall):**
   ```
   Total: 145ms
   ├─ Network transmission: 65ms (45%)
   ├─ Ingestion & parsing: 15ms (10%)
   ├─ Risk check: 35ms (24%)
   ├─ Decision logic: 12ms (8%)
   ├─ Order generation: 8ms (6%)
   └─ Exchange API: 10ms (7%)
   ```

3. **Latency trends:**
   - Hourly average latency (identify performance degradation)
   - P50, P95, P99 distribution
   - Latency vs. profitability scatter plot

4. **Competitive benchmarking (if enabled):**
   - Blockriculture vs. industry average
   - Rankings: fastest bot platforms

---

## Part 2: Multi-Signal Fusion Engine

### 2.1 Problem Statement

Traders often receive conflicting signals:
- **TradingView:** "Buy BTC/USDT"
- **Telegram signal provider:** "Sell BTC/USDT"
- **On-chain listener:** "Neutral; whale movement detected"

Current platforms force manual conflict resolution. Blockriculture automates this.

### 2.2 Fusion Strategy

#### Input: Signal metadata
```json
{
  "signal_id": "tv_001_20260318_100500",
  "source": "tradingview",
  "pair": "BTC/USDT",
  "action": "BUY",
  "confidence": 0.85,
  "timestamp": 1710761100000,
  "metadata": {
    "indicator": "RSI > 70",
    "timeframe": "1h",
    "user_rating": 0.92,
    "historical_accuracy": 0.78
  }
}
```

#### Scoring model (v1)
```python
def calculate_signal_score(signal):
    # Base confidence from signal source
    base_score = signal['confidence']  # 0-1
    
    # Adjust for source credibility
    source_weights = {
        'tradingview': 1.0,
        'telegram': 0.7,
        'on_chain': 0.8,
        'glassnode': 0.9,
    }
    weighted_score = base_score * source_weights.get(signal['source'], 0.5)
    
    # Boost for high user rating (if available)
    if 'user_rating' in signal['metadata']:
        rating_boost = signal['metadata']['user_rating'] * 0.1
        weighted_score = min(1.0, weighted_score + rating_boost)
    
    # Penalty for conflicting signals within N minutes
    conflicting_signals = self.find_conflicting_signals(
        pair=signal['pair'],
        window_minutes=5
    )
    if conflicting_signals:
        conflict_penalty = 0.1 * len(conflicting_signals)
        weighted_score = max(0.0, weighted_score - conflict_penalty)
    
    return weighted_score

def fuse_signals(signals_for_pair):
    """
    Given multiple signals for same pair, return unified action.
    """
    scores = {sig['source']: calculate_signal_score(sig) for sig in signals_for_pair}
    
    # Weighted vote
    buy_score = sum(s for src, s in scores.items() if signals_for_pair[src]['action'] == 'BUY')
    sell_score = sum(s for src, s in scores.items() if signals_for_pair[src]['action'] == 'SELL')
    
    if abs(buy_score - sell_score) < 0.2:
        # Conflicting signals; recommend neutral
        return {'action': 'HOLD', 'confidence': 0.0, 'reason': 'conflicting_signals'}
    
    final_action = 'BUY' if buy_score > sell_score else 'SELL'
    confidence = max(buy_score, sell_score) / (buy_score + sell_score + 0.001)
    
    return {
        'action': final_action,
        'confidence': confidence,
        'breakdown': scores,
        'timestamp': time.time()
    }
```

#### Output
```json
{
  "pair": "BTC/USDT",
  "fused_action": "BUY",
  "fused_confidence": 0.82,
  "reason": "2/3 signals bullish; on-chain neutral",
  "breakdown": {
    "tradingview": 0.85,
    "telegram": -0.65,
    "on_chain": 0.00
  },
  "recommendation": "Execute with 20% position size (confidence < 0.9)"
}
```

### 2.3 Implementation Phases

**Phase 1 (MVP):** Simple weighted voting (score calculation above)  
**Phase 2:** Add user reputation learning (traders who score high get higher source weight)  
**Phase 3:** ML-based fusion (time-series prediction model; which combination historically performs best?)

---

## Part 3: Portfolio-Level Risk Orchestration

### 3.1 Problem

Trader runs 20 bots across BTC, ETH, XRP:
- **Bot 1:** 50% leverage short BTC
- **Bot 2:** 30% leverage long ETH
- **Bot 3:** 20% leverage long XRP
- **Total notional exposure:** 120% (leverage + concentration)
- **Correlation risk:** If BTC falls 10%, ALL three likely fall → cascade liquidation

**Current solution:** Manual spreadsheet (error-prone)

### 3.2 Solution: Portfolio Risk Engine

```python
class PortfolioRiskEngine:
    def __init__(self):
        self.bots = {}  # bot_id → bot_config
        self.positions = {}  # bot_id → [position_list]
        self.correlation_matrix = {}  # pair_x, pair_y → correlation
    
    def calculate_portfolio_risk(self):
        """
        Calculate real-time portfolio exposure.
        """
        # 1. Aggregate positions
        total_exposure = self.aggregate_positions()
        
        # 2. Calculate concentration risk
        concentration = self.calculate_concentration(total_exposure)
        
        # 3. Calculate correlation risk
        correlation_risk = self.calculate_correlation_risk(total_exposure)
        
        # 4. Calculate leverage risk
        leverage_risk = self.calculate_leverage_risk(total_exposure)
        
        return {
            'total_notional': total_exposure['notional_usd'],
            'concentration_score': concentration,  # 0-1
            'correlation_risk': correlation_risk,  # 0-1
            'leverage_ratio': leverage_risk,  # 1.0 = no leverage
            'risk_level': self.risk_level_bucket(concentration, correlation_risk, leverage_risk),
        }
    
    def aggregate_positions(self):
        """
        Sum all bot positions by pair.
        """
        by_pair = {}
        for bot_id, positions in self.positions.items():
            for pos in positions:
                pair = pos['pair']
                if pair not in by_pair:
                    by_pair[pair] = {'long': 0, 'short': 0, 'notional': 0}
                
                notional = pos['size'] * pos['current_price']
                if pos['side'] == 'LONG':
                    by_pair[pair]['long'] += notional
                else:
                    by_pair[pair]['short'] += notional
                by_pair[pair]['notional'] += notional
        
        return by_pair
    
    def calculate_concentration(self, by_pair):
        """
        Concentration = max_pair_exposure / total_exposure
        0.3 = 30% of portfolio in single pair (warning threshold)
        0.5 = 50% of portfolio in single pair (critical)
        """
        total_notional = sum(p['notional'] for p in by_pair.values())
        max_pair = max(p['notional'] for p in by_pair.values())
        return max_pair / total_notional if total_notional > 0 else 0
    
    def calculate_correlation_risk(self, by_pair):
        """
        If trader is long BTC and short ETH, but correlation = 0.95,
        that's high risk.
        """
        risk_score = 0
        pairs = list(by_pair.keys())
        for i, pair1 in enumerate(pairs):
            for pair2 in pairs[i+1:]:
                correlation = self.correlation_matrix.get((pair1, pair2), 0.7)
                exposure1 = by_pair[pair1]['notional']
                exposure2 = by_pair[pair2]['notional']
                
                # If opposite sides and high correlation: risk
                is_opposite = (by_pair[pair1]['long'] > 0 and by_pair[pair2]['short'] > 0) or \
                              (by_pair[pair1]['short'] > 0 and by_pair[pair2]['long'] > 0)
                if is_opposite and correlation > 0.7:
                    risk_score += (correlation - 0.7) * (exposure1 + exposure2) / 100
        
        return min(1.0, risk_score)
    
    def recommend_risk_mitigation(self, portfolio_risk):
        """
        Given portfolio risk, recommend actions.
        """
        recommendations = []
        
        if portfolio_risk['concentration_score'] > 0.4:
            recommendations.append({
                'type': 'concentration',
                'severity': 'warning',
                'action': 'Reduce position in top pair by 30%',
                'expected_risk_reduction': 0.15
            })
        
        if portfolio_risk['correlation_risk'] > 0.6:
            recommendations.append({
                'type': 'correlation',
                'severity': 'critical',
                'action': 'Hedge BTC with short position or liquidate conflicting bot',
                'expected_risk_reduction': 0.25
            })
        
        if portfolio_risk['leverage_ratio'] > 1.5:
            recommendations.append({
                'type': 'leverage',
                'severity': 'critical',
                'action': 'Reduce leverage; liquidate 2-3 smallest positions',
                'expected_risk_reduction': 0.20
            })
        
        return recommendations
```

### 3.3 UI/UX for Risk Dashboard

```
┌─────────────────────────────────────────┐
│  PORTFOLIO RISK SUMMARY                 │
├─────────────────────────────────────────┤
│ Total Notional:        $250,000         │
│ Leverage Ratio:        1.3x (OK)        │
│ Concentration Score:   0.42 (WARNING)   │
│ Correlation Risk:      0.35 (OK)        │
├─────────────────────────────────────────┤
│ Risk Recommendations:                    │
│  ⚠️  Top pair (BTC) = 42% of portfolio  │
│      → Reduce by 30% to lower risk      │
│  ✓ No correlation red flags             │
└─────────────────────────────────────────┘

By Pair Exposure:
├─ BTC/USDT:  $105,000 (42%)
│   ├─ Bot A (long 50): $75,000
│   └─ Bot B (short 30): $30,000 (hedge)
├─ ETH/USDT:  $75,000 (30%)
│   └─ Bot C (long 50): $75,000
└─ XRP/USDT:  $70,000 (28%)
    └─ Bot D (long 50): $70,000
```

---

## Part 4: Exchange API Abstraction Layer

### 4.1 Requirement
Single Blockriculture API for all exchanges; hide rate limits, throttling, API differences.

### 4.2 Architecture
```
┌──────────────────────────────────────┐
│  User Code (Blockriculture SDK)      │
│  bc.order.market_buy('BTC/USDT', 1)  │
└──────────┬───────────────────────────┘
           │
    ┌──────▼──────────────────┐
    │  Blockriculture Router  │
    │  - Select exchange      │
    │  - Check rate limits    │
    │  - Route to adapter     │
    └──────┬───────────────────┘
           │
    ┌──────▼─────────────────────────────┐
    │  Exchange Adapters (Abstraction)   │
    ├────────────────────────────────────┤
    │  Binance Adapter                   │
    │  Kraken Adapter                    │
    │  Coinbase Adapter                  │
    │  Bybit Adapter                     │
    │  ... (add more)                    │
    └──────┬─────────────────────────────┘
           │
    ┌──────▼──────────────────┐
    │  Native Exchange APIs   │
    │  (Binance, Kraken, etc) │
    └───────────────────────────┘
```

### 4.3 Rate Limit Management
```python
class RateLimitManager:
    def __init__(self):
        self.limits = {
            'binance': {'orders_per_min': 1200, 'api_calls_per_sec': 10},
            'kraken': {'api_calls_per_sec': 15},
            'coinbase': {'api_calls_per_sec': 5},
        }
        self.usage = {}  # exchange → [timestamps of recent calls]
    
    def can_execute(self, exchange, call_type):
        """
        Check if we can make the call without hitting rate limits.
        """
        limit = self.limits[exchange][call_type]
        recent = self.usage.get(exchange, [])
        
        # Trim old timestamps
        recent = [t for t in recent if time.time() - t < 60]
        
        if len(recent) >= limit:
            return False
        
        return True
    
    def wait_if_needed(self, exchange, call_type):
        """
        Block until we can safely make the call.
        """
        while not self.can_execute(exchange, call_type):
            time.sleep(0.1)
        
        self.usage.setdefault(exchange, []).append(time.time())
```

---

## Part 5: On-Chain Signal Processing (Phase 3, Stretch Goal)

### 5.1 Challenge
On-chain events (whale movement, liquidation, contract deploy) generate opportunities, but blockchain latency is 5-30s (block time + confirmation).

### 5.2 Solution: Private Node + MEV Bundle

```python
class OnChainListener:
    def __init__(self, chain='ethereum'):
        self.provider = self.connect_to_private_node(chain)
        self.mempool_subscription = {}
    
    def listen_to_mempool(self, contract_filter):
        """
        Listen to mempool (unconfirmed transactions).
        Can act 5-10s faster than waiting for block confirmation.
        """
        def on_pending_txn(txn):
            if self.matches_filter(txn, contract_filter):
                latency = time.time() - (txn['timestamp'] / 1000)
                self.emit_signal(txn, latency_ms=latency*1000)
        
        self.provider.on('pending', on_pending_txn)
    
    def submit_mev_bundle(self, trades, block_height):
        """
        Submit bundle to block builder (Flashbots, MEV-Relay).
        Guarantees inclusion in block; minimizes front-run risk.
        """
        bundle = {
            'version': 'v0.1',
            'inclusion': {'block': block_height},
            'body': [
                {'hash': tx['hash']} for tx in trades
            ],
            'privacy': {'hints': ['calldata', 'function_selector']}
        }
        
        result = self.bundle_relay.submit_bundle(bundle)
        return result  # Contains block number, inclusion status
```

---

## Part 6: MVP Tech Stack Recommendation

### Backend
- **Language:** Python 3.11+ or Go (latency-critical)
- **Web framework:** FastAPI (Python) or Gin (Go)
- **Async runtime:** asyncio (Python) or goroutines (Go)
- **Database:** PostgreSQL (primary), Redis (cache, rate limiting)
- **Message queue:** Kafka or RabbitMQ (signal processing)
- **Monitoring:** Prometheus + Grafana (latency metrics)

### Frontend
- **Framework:** React or Vue
- **Charting:** Recharts or Lightweight Charts (latency waterfall visualization)
- **Real-time updates:** WebSocket (latency dashboard)
- **State management:** Redux or Pinia

### Deployment
- **Containerization:** Docker
- **Orchestration:** Kubernetes or Docker Compose (MVP)
- **Cloud:** AWS (us-east-1 for low latency) or GCP

### Key Dependencies
```
# Python
fastapi==0.104.0
asyncio-contextmanager==1.0.0
redis==5.0.0
psycopg2-binary==2.9.0
ccxt==3.0.0  # Exchange abstraction
pydantic==2.5.0  # Data validation
python-dateutil==2.8.0
```

---

## Part 7: Success Metrics (MVP)

| Metric | Target | Timeline |
|--------|--------|----------|
| **Latency (P50)** | <150ms TradingView | Month 1 |
| **Latency (P99)** | <250ms TradingView | Month 1 |
| **Uptime** | 99.5% | Month 2 |
| **Signal ingestion rate** | 1,000+ signals/sec | Month 2 |
| **Free tier users** | 500+ | Month 3 |
| **Pro tier users** | 50+ | Month 3 |
| **Fusion accuracy** | 80%+ signals fused without conflict | Month 3 |
| **Portfolio risk precision** | ±5% error vs. manual calculation | Month 2 |

---

## Conclusion

Blockriculture's technical moat is built on:
1. **Real-time latency measurement** (differentiator; hard to copy)
2. **Multi-signal fusion engine** (medium barrier; ML moat later)
3. **Portfolio risk coordination** (high complexity; defensible)
4. **On-chain integration** (moonshot; high technical barrier)

MVP should focus on #1 and #2; #3 by month 6; #4 as stretch goal.

