import time
import random
import math
import requests

API_URL = "http://127.0.0.1:8000/api/sensors/"
PLOT_ID = 1
INTERVAL = 5

print("🚀 Sensor simulation started")

t = 0
while True:
    temperature = 20 + 5 * math.sin(t / 10) + random.uniform(-1, 1)
    humidity = 60 + 10 * math.sin(t / 15) + random.uniform(-2, 2)
    soil = 40 + random.uniform(-3, 3)

    for sensor_type, value in [
        ("temperature", temperature),
        ("humidity", humidity),
        ("soil_moisture", soil),
    ]:
        payload = {
            "plot_id": PLOT_ID,
            "sensor_type": sensor_type,
            "value": round(value, 2),
        }

        r = requests.post(API_URL, json=payload)
        if r.status_code == 201:
            print(f"✅ {sensor_type}: {value:.2f}")
        else:
            print(f"❌ {sensor_type}", r.status_code, r.text)

    t += 1
    time.sleep(INTERVAL)
