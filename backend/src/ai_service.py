import requests
import os
from datetime import datetime, timedelta

XAI_API_KEY = os.getenv("XAI_API_KEY", "your-xai-api-key")
XAI_API_URL = "https://api.x.ai/v1/chat/completions"

def predict_maintenance(data):
    """
    Use Grok API to predict maintenance schedules based on equipment data.
    """
    try:
        # Prepare prompt for Grok
        prompt = (
            "You are an AI system for predictive maintenance in mining equipment. "
            "Given the following equipment data, predict potential failures and recommend maintenance schedules. "
            "Data includes equipment_id, timestamp, normalized vibration, normalized temperature, and uptime_hours. "
            "Provide a JSON response with predictions for each equipment_id, including failure_probability (0-1), "
            "recommended_maintenance_date, and health_status (Good, Warning, Critical). "
            f"Data: {data}"
        )
        
        headers = {
            "Authorization": f"Bearer {XAI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "grok-beta",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1000
        }
        
        response = requests.post(XAI_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        predictions = response.json().get("choices", [{}])[0].get("message", {}).get("content", "{}")
        return eval(predictions)  # Assuming Grok returns JSON string
    except Exception as e:
        raise Exception(f"Error in AI prediction: {str(e)}")