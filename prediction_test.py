import requests
from datetime import datetime

url = "http://127.0.0.1:5000/predict"

# Get current date and time details
now = datetime.now()

# Simulating a landslide-prone location
data = {
    # High-risk coordinates (Change to a known landslide-prone area if needed)
    "latitude": 30.3344,  # Example: Uttarakhand landslide-prone area
    "longitude": 78.0438,  

    # 🚨 High-risk terrain
    "Slope": 45.0,   # Steep slope (higher risk)
    "Aspect": 270.0,  # Direction can matter, but let's assume it's risky

    # 🚨 High-risk environmental factors
    "distance_to_nearest_landslide": 0.1,  # Very close to past landslides
    "risk_zone": 3,  # Assuming 3 means high-risk zone
    "location_risk_score": 1.0,  # Max risk score

    # 🚨 High-risk weather conditions
    "temperature": 5.0,   # Lower temperatures may increase instability
    "precipitation": 100.0,  # Heavy rainfall (high landslide trigger)
    "wind_speed": 25.0,  # Strong winds

    # Time-based factors
    "event_year": now.year,
    "event_month": now.month,
    "event_day": now.day,
    "event_weekday": now.weekday(),
    "event_hour": now.hour,
    "season_encoded": 2,  
    "time_of_day_encoded": 1,  

    # 🚨 Landslide characteristics
    "landslide_category": 3,  # Large landslides
    "landslide_size": 5,  # Big landslide
    "landslide_trigger": 2  # Heavy rainfall trigger
}

response = requests.post(url, json=data)
print("Prediction:", response.json())
