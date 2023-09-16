import random
import math

def detect_anomalies(data):
    mean = sum(data) / len(data)
    std = math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
    threshold = 3 * std  # Umbral para detectar anomalías (3 desviaciones estándar)

    anomalies = [value for value in data if abs(value - mean) > threshold]
    return anomalies

if __name__ == "__main__":
    # Generar datos de ejemplo (1000 valores)
    data = [random.random() for _ in range(900)]  # Datos normales
    data.extend([10 + random.random() for _ in range(100)])  # Anomalías

    # Detectar anomalías en los datos
    anomalies = detect_anomalies(data)

    # Imprimir las anomalías encontradas
    print("Anomalies:")
    for anomaly in anomalies:
        print(anomaly)
