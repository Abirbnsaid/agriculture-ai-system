from anomaly_ml.agent import rule_based_agent

# valeurs de test
test_temperatures = [22, 33, 41, -15]

for temp in test_temperatures:
    result = rule_based_agent(temp)

    print("\n==========================")
    print(f"Temperature: {temp}°C")
    print(f"Status: {result['status']}")
    print(f"Explanation: {result['explanation']}")
    print(f"Recommendation: {result['recommendation']}")
