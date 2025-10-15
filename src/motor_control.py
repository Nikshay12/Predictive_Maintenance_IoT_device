"""motor_control.py
Mock motor/fan control. Replace mock functions with actual GPIO calls (e.g., RPi.GPIO)
when running on Raspberry Pi and using drivers like L298N.
"""
import time

def start_fan():
    print("[motor_control] Fan START")

def stop_fan():
    print("[motor_control] Fan STOP")

def control_based_on_prediction(prediction: int, threshold: float = 0.5):
    # prediction: 0 or 1 (or probability if model returns float)
    if isinstance(prediction, float):
        prob = prediction
        if prob >= threshold:
            start_fan()
        else:
            stop_fan()
    else:
        if prediction == 1:
            start_fan()
        else:
            stop_fan()

if __name__ == "__main__":
    # simple demo loop
    for p in [0, 0.3, 0.7, 1]:
        control_based_on_prediction(p)
        time.sleep(0.5)
