def explain_temperature(status, value):
    explanations = {
        "IMPOSSIBLE": f"Temperature {value}°C is physically impossible.",
        "OVERHEAT": f"Temperature {value}°C indicates extreme heat stress.",
        "HIGH": f"Temperature {value}°C is above normal range.",
        "NORMAL": f"Temperature {value}°C is within normal range."
    }
    return explanations.get(status, "No explanation available.")
