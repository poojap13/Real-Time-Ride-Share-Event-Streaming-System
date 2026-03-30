# Real-Time Driver GPS Streaming Pipeline

This project simulates a ride-share system using Apache Kafka.

## Architecture
Producer (Python) → Kafka → Consumer (Python)

## Features
- Real-time GPS event streaming
- Kafka-based asynchronous processing
- Fault-tolerant message handling
- Docker-based setup

## How to Run

### 1. Start Kafka
docker compose up -d

### 2. Run Producer
python producer.py

### 3. Run Consumer
python consumer.py

---

### Example Event

```json
{
  "driver_id": "driver_3",
  "latitude": 44.65,
  "longitude": -63.57,
  "timestamp": "2026-03-30T12:00:00"
}
```

---
### What I Learned
How Kafka decouples producer and consumer
Basics of event-driven architecture
How real-time streaming systems differ from request-response systems

