import numpy as np
from scipy.stats import norm

def detect_anomalies(data):
    mean = np.mean(data)
    std = np.std(data)
    threshold = 3 * std  # Umbral para detectar anomalías (3 desviaciones estándar)

    anomalies = []

    for value in data:
        if np.abs(value - mean) > threshold:
            anomalies.append(value)

    return anomalies

# Generar datos de ejemplo (1000 valores)
data = np.concatenate([np.random.normal(0, 1, 900), np.random.normal(10, 1, 100)])

# Detectar anomalías en los datos
anomalies = detect_anomalies(data)

# Imprimir las anomalías encontradas
print("Anomalies:")
for anomaly in anomalies:
    print(anomaly)
