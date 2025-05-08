import pandas as pd
from datetime import datetime, timedelta

def process_excel_data(file_path):
    """
    Process Excel file and prepare data for AI prediction.
    Expected columns: equipment_id, timestamp, vibration, temperature, uptime_hours
    """
    try:
        df = pd.read_excel(file_path)
        required_columns = ['equipment_id', 'timestamp', 'vibration', 'temperature', 'uptime_hours']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("Excel file must contain columns: equipment_id, timestamp, vibration, temperature, uptime_hours")
        
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        # Normalize numerical data
        df['vibration'] = (df['vibration'] - df['vibration'].mean()) / df['vibration'].std()
        df['temperature'] = (df['temperature'] - df['temperature'].mean()) / df['temperature'].std()
        df['uptime_hours'] = df['uptime_hours'].astype(float)
        
        return df.to_dict(orient='records')
    except Exception as e:
        raise Exception(f"Error processing Excel file: {str(e)}")