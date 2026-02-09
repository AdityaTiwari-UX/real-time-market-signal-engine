
# System Architecture – Real-Time Market Signal Engine

## Overview
This system is designed to ingest live (or simulated) stock market data, analyze short-term market behavior, and generate explainable trading alerts with low latency.

The architecture follows a modular, streaming-first design to ensure scalability, interpretability, and real-world usability.

---

## High-Level Data Flow

Market Data  
→ Ingestion Layer  
→ Feature Engineering  
→ Signal Detection  
→ Prediction Models  
→ Alert Engine  
→ Explainability Layer  

---

## Core Components

### 1. Data Ingestion (`src/ingestion`)
Responsible for:
- Streaming live or simulated stock price and volume data
- Handling timestamps, ordering, and missing data
- Maintaining rolling time windows for real-time analysis

This layer is designed to be easily replaceable (e.g., simulated data → WebSocket → Kafka).

---

### 2. Feature Engineering (`src/features`)
Responsible for:
- Computing technical indicators (SMA, EMA, RSI, MACD)
- Rolling statistical features (mean, volatility, z-score)
- Volume-based indicators and price-volume relationships

This layer transforms raw market data into meaningful signals for downstream components.

---

### 3. Signal Detection (`src/signals`)
Responsible for:
- Detecting price breakouts and breakdowns
- Identifying unusual volume activity
- Monitoring volatility expansion and regime shifts

Signals are primarily rule-based and statistical to ensure interpretability and fast reaction time.

---

### 4. Prediction Models (`src/models`)
Responsible for:
- Short-term trend prediction (5–30 minute horizon)
- Directional forecasting rather than exact price prediction
- Providing confidence scores for predicted movements

Both statistical (ARIMA) and machine-learning models (XGBoost) are supported.

---

### 5. Alert Engine (`src/alerts`)
Responsible for:
- Combining signals and model predictions
- Assigning confidence scores to alerts
- Enforcing cooldown logic to prevent alert flooding

Alerts are generated only when multiple conditions align.

---

### 6. Explainability Layer (`src/explainability`)
Responsible for:
- Explaining why an alert was triggered
- Highlighting key contributing features
- Providing human-readable reasoning alongside alerts

Interpretability is a core design requirement, not an afterthought.

---

## Design Principles

- **Low Latency:** Rolling windows and streaming-first logic
- **Explainability:** Every alert must be explainable
- **Modularity:** Each component can evolve independently
- **Production Readiness:** Clean separation of concerns

---

## Future Extensions
- Real-time dashboards
- Model drift detection
- News and event-aware signals
- Scalable streaming via Kafka
