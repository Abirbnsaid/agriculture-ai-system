# 🌱 Agriculture AI System

## 📌 Project Overview
This project is an intelligent agriculture monitoring system that simulates sensor data (temperature, humidity, soil moisture), detects anomalies using AI techniques, and provides rule-based explanations and recommendations.

The system is built using **Django**, **Django REST Framework**, and **Python**.

---

## 🎯 Project Objectives
- Simulate agricultural sensor data
- Detect abnormal sensor behavior
- Apply AI techniques for anomaly detection
- Generate explanations and recommendations
- Integrate AI logic into a Django backend

---

## 🏗️ Project Structure

agriculture_ai/
│
├── backend/
├── farms/
├── sensors/
├── anomaly_ml/
│ └── detector.py
│
├── simulate_sensor.py
├── anomaly_simulation.py
├── test_agent.py
└── README.md



## 🤖 AI & Logic Components

### 1️⃣ Rule-Based AI Agent
- Threshold-based rules
- Explanation generator
- Recommendation engine

### 2️⃣ Anomaly Detection
- Rolling statistics approach
- Sliding window average
- Detects abnormal deviations

States:
- ✅ NORMAL
- ❌ ANOMALY
- ⏳ LEARNING

---

## 🧪 How to Test

### Run Django Server
```bash
python manage.py runserver
Run Sensor Simulation
bash
Copier le code
python simulate_sensor.py
Test Rule-Based Agent
bash
Copier le code
python test_agent.py
🛠️ Technologies Used
Python

Django

Django REST Framework

Git & GitHub

🎓 Academic Context
This project was developed as part of SOA learning process.

