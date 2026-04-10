import time
import psutil
import requests

CONTROLLER_URL = "http://controller:5001/metrics"

def collect_metrics():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent
    }

while True:
    data = collect_metrics()
    
    try:
        requests.post(CONTROLLER_URL, json=data)
        print("Metrics sent:", data)
    except Exception as e:
        print("Error:", e)

    if data["cpu"] > 80 or data["memory"] > 80:
        print("ALERT: High resource usage detected")

    time.sleep(5)
