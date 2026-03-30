import json
import random
import time
from kafka import KafkaProducer

TOPIC = "driver_gps"

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

zones = ["Downtown", "University", "Airport", "Mall", "Harbour"]

print(f"✅ Producer started. Sending messages to topic: {TOPIC}")

while True:
    event = {
        "driver_id": random.randint(1, 50),
        "zone": random.choice(zones),
        "lat": round(44.64 + random.uniform(-0.03, 0.03), 5),
        "lon": round(-63.57 + random.uniform(-0.03, 0.03), 5),
        "speed_kmh": random.randint(10, 90),
        "ts": time.time(),
    }

    producer.send(TOPIC, event)
    producer.flush()
    print("Sent:", event)

    time.sleep(1)
