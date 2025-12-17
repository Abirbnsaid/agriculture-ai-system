import random
import math
import time

INTERVAL = 1  # secondes
DURATION = 60  # durée de la simulation

def normal_temperature(t):
    return 22 + 3 * math.sin(t / 10) + random.uniform(-0.5, 0.5)

def inject_anomaly(value, anomaly_type):
    if anomaly_type == "spike":
        return value + random.uniform(20, 30)
    elif anomaly_type == "stuck":
        return 25
    elif anomaly_type == "impossible":
        return random.uniform(-20, -5)
    return value

print("🚀 Starting anomaly injection simulation")

for t in range(DURATION):
    temp = normal_temperature(t)

    # Choix aléatoire d’anomalie
    if t == 20:
        temp = inject_anomaly(temp, "spike")
        label = "🔥 SPIKE"
    elif 30 <= t <= 40:
        temp = inject_anomaly(temp, "stuck")
        label = "🧱 STUCK"
    elif t == 50:
        temp = inject_anomaly(temp, "impossible")
        label = "❌ IMPOSSIBLE"
    else:
        label = "✅ NORMAL"

    print(f"t={t:02d} | temperature={temp:.2f} | {label}")
    time.sleep(INTERVAL)

print("✅ Simulation finished")
