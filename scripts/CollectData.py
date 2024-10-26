import requests
import json
import os
from datetime import datetime

# Configuration
RATP_API_URL = "https://api-ratp.pierre-grimaud.fr/v4/schedules"
SNCF_API_URL = "https://api.sncf.com/v1/coverage/sncf/"

API_KEY_SNCF = "YOUR_SNCF_API_KEY"

def get_ratp_data(type, line, station, way):
    url = f"{RATP_API_URL}/{type}/{line}/{station}/{way}"
    response = requests.get(url)
    data = response.json()
    print(data)
    return data

def get_sncf_data():
    headers = {'Authorization': f'Bearer {API_KEY_SNCF}'}
    response = requests.get(SNCF_API_URL, headers=headers)
    data = response.json()
    return data

def save_data(data, filename):
    with open(f"data/real_time_data/{filename}", 'w') as f:
        json.dump(data, f)

def collect_data():
    # Collect RATP data
    ratp_data = get_ratp_data("metros", "8", "bastille", "R")
    # save_data(ratp_data, f"ratp_data_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.json")

    # Collect SNCF data
    sncf_data = get_sncf_data()
    # save_data(sncf_data, f"sncf_data_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.json")

if __name__ == "__main__":
    collect_data()
