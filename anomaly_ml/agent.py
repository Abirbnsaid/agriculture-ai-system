from .rules import temperature_rule
from .explanations import explain_temperature
from .recommendations import recommend_action

def rule_based_agent(temp):
    status = temperature_rule(temp)
    explanation = explain_temperature(status, temp)
    recommendation = recommend_action(status)

    return {
        "status": status,
        "explanation": explanation,
        "recommendation": recommendation
    }