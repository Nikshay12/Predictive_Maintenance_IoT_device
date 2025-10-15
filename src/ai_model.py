"""ai_model.py
Train a RandomForest classifier on data/iot_sensor_data.csv and save the trained model to models/ 
This script is intentionally lightweight and uses scikit-learn for portability.
"""
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'iot_sensor_data.csv')
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, 'rf_predictive_maintenance.pkl')

def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    return df

def train():
    df = load_data()
    X = df[['temperature','vibration','current']]
    y = df['failure']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print('Accuracy on test set:', acc)
    print(classification_report(y_test, preds))
    joblib.dump(clf, MODEL_PATH)
    print('Saved model to', MODEL_PATH)

if __name__ == '__main__':
    train()
