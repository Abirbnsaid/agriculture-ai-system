from anomaly_ml.detector import detect_temperature
import random

print("🧪 TEST ML")

for i in range(10):
    temp = 20 + random.uniform(-2, 2)
    print(temp, "→", detect_temperature(temp))

print("🔥 TEST ANOMALIE")
print(50, "→", detect_temperature(50))
