# AI-Powered Predictive Maintenance for IoT Devices

## Overview
Predict machine failures using IoT sensor data (temperature, vibration, current). This repo contains:
- data/: sample synthetic dataset
- src/: sensor mocks, model training, Flask API, motor control, cloud sender
- reports/: example outputs
- models/: (created after training) trained model file

## Quick start
1. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate   # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
```

2. Train model:
```bash
python src/ai_model.py
```

3. Run Flask API (after training):
```bash
python src/app.py
```

4. Use the mock sensor reader:
```bash
python src/sensors.py
```

5. Demo motor control:
```bash
python src/motor_control.py
```

## Notes
- `src/send_to_cloud.py` is a placeholder that shows how to POST JSON to an endpoint.
- Replace mocks with actual GPIO code when deploying to Raspberry Pi.
- Model is a RandomForest by default; for time-series or richer data consider LSTM/GRU.

## License
MIT
