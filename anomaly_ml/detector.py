# anomaly_ml/detector.py

WINDOW = 5
history = []

def detect_temperature(value):
    """
    Détection d'anomalie simple basée sur statistiques glissantes
    """
    history.append(value)

    if len(history) < WINDOW:
        return "LEARNING"

    avg = sum(history[-WINDOW:]) / WINDOW

    if abs(value - avg) > 8:
        return "ANOMALY"

    return "NORMAL"
