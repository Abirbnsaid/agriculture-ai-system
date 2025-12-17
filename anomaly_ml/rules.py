def temperature_rule(temp):
    if temp < -5:
        return "IMPOSSIBLE"
    elif temp > 40:
        return "OVERHEAT"
    elif temp > 30:
        return "HIGH"
    else:
        return "NORMAL"
