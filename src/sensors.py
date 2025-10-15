"""sensors.py
Reads sensor data. Contains a hardware mock (for development) and a simple interface
that can be replaced with real GPIO sensor reads on Raspberry Pi/Arduino.
"""
import time
import random
from typing import Dict

def read_mock_sensors() -> Dict[str, float]:
    """Return a mock sensor reading (temperature °C, vibration index, current mA)."""
    temperature = round(30 + random.gauss(0,1.5), 2)
    vibration = max(0, int(random.gauss(0.5,0.8)))
    current = int(random.gauss(500,40))
    return {"temperature": temperature, "vibration": vibration, "current": current}

if __name__ == "__main__":
    try:
        while True:
            data = read_mock_sensors()
            print(data)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped mock sensor reading.")
