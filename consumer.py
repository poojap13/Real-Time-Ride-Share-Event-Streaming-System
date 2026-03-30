import json
import time
from kafka import KafkaConsumer

TOPIC = "driver_gps"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="traffic_service",
)

def traffic_status(speed_kmh: int) -> str:
    if speed_kmh < 25:
        return "HIGH_CONGESTION"
    if speed_kmh < 50:
        return "MODERATE_TRAFFIC"
    return "LOW_TRAFFIC"

print(f"✅ Consumer started. Listening to topic: {TOPIC}")

for msg in consumer:
    data = msg.value
    status = traffic_status(data["speed_kmh"])

    out = {
        "driver_id": data["driver_id"],
        "zone": data["zone"],
        "traffic_status": status,
        "processed_at": time.time(),
    }

    print("Processed:", out)
