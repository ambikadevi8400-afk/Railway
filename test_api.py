import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAILRADAR_API_KEY")

print("API key loaded:", bool(API_KEY))
train_number = "12919"

url = f"https://api.railradar.in/v1/trains/{train_number}/live"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(url, headers=headers, timeout=15)

print("Status:", response.status_code)
data = response.json()

print("Status:", response.status_code)
print("API connected successfully!")
print("Data received:", type(data))
print("Top-level keys;", list(data.keys()))
print("data keys;",data["data"].keys())
print("Current Location:", data["data"]["currentLocation"])
print("Route:", data["data"]["route"])