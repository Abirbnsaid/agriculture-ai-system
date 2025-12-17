import random
import math

WINDOW = 5
history = []

def generate_temperature(t):
    return 22 + 3 * math.sin(t / 10) + random.uniform(-0.5, 0.5)

def inject_anomaly(value, t):
    if t == 20:
        return value + 25
    if 30 <= t <= 40:
        return 25
    if t == 50:
        return -15
    return value

def rolling_detect(temp):
    history.append(temp)

    if len(history) < WINDOW:
        return "⏳ LEARNING"

    avg = sum(history[-WINDOW:]) / WINDOW

    if abs(temp - avg) > 8:
        return "❌ ANOMALY"

    return "✅ NORMAL"

print("🚀 Rolling anomaly detection started")

for t in range(60):
    temp = generate_temperature(t)
    temp = inject_anomaly(temp, t)

    status = rolling_detect(temp)

    print(f"t={t:02d} | temperature={temp:.2f} | {status}")

print("✅ Detection finished")
