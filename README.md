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
