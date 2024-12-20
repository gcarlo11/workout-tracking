import requests
import datetime as dt
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]

today = dt.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["SHEETY_ENDPOINT"]


exercise = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
exercise_config = {
    "query": exercise,
    "gender": "Male",
    "weight_kg": "65",
    "height_cm": "173",
    "age": "20"
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
result = response.json()

sheety_header = {
    "Authorization": os.environ["SHEETY_AUTH"]
}
for exercise in result["exercises"]:
    sheety_json = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response2 = requests.post(url=sheety_endpoint, json=sheety_json, headers=sheety_header)
    print(response2)
