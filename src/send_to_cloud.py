"""send_to_cloud.py
Simple placeholder that demonstrates packaging sensor data and sending to a REST endpoint.
For ESP8266/ESP32 based sending, implement the HTTP POST/MQTT publish on the device firmware.
"""
import json
import requests

def send_json(endpoint: str, payload: dict, timeout=5):
    try:
        r = requests.post(endpoint, json=payload, timeout=timeout)
        print('Sent, status:', r.status_code)
        return r.status_code, r.text
    except Exception as e:
        print('Failed to send:', e)
        return None, str(e)

if __name__ == '__main__':
    example = { 'temperature': 35.2, 'vibration': 1, 'current': 520, 'device_id': 'demo-001' }
    print('Example send (will fail without a real endpoint):')
    print(send_json('https://example.com/api/sensor', example))
