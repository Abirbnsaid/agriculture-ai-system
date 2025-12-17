def recommend_action(status):
    actions = {
        "IMPOSSIBLE": "Check sensor calibration.",
        "OVERHEAT": "Activate irrigation immediately.",
        "HIGH": "Monitor crop and consider irrigation.",
        "NORMAL": "No action required."
    }
    return actions.get(status, "No recommendation.")
