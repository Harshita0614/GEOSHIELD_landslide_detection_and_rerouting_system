import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "longitude": 80.0,
    "latitude": 13.0,
    "Aspect": 30,
    "Slope": 15,
    "temperature": 25,
    "precipitation": 10,
    "wind_speed": 5,
    "event_year": 2024,
    "event_month": 2,
    "event_day": 10,
    "event_weekday": 6,
    "season_encoded": 1,
    "event_hour": 14,
    "time_of_day_encoded": 2,
    "risk_zone": 3,
    "distance_to_nearest_landslide": 500,
    "location_risk_score": 7,
    "landslide_category": 2,
    "landslide_size": 1,
    "landslide_trigger": 3
}

response = requests.post(url, json=data)
print("Response:", response.json())
