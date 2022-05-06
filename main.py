import requests
from datetime import datetime
import os

API_KEY = os.getenv("API_KEY")
API_ID = os.getenv("API_ID")
URL_NAME = os.getenv("nutrition_endpoint")
shetty_endpoint = os.getenv("shetty_endpoint")
exercise_input = input("What have you done ?").title()
json_params = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 78,
    "height_cm": 178,
    "age": 26
}

today = datetime.now()
show_year = today.strftime("%Y")
show_month = today.strftime("%m")
show_day = today.strftime("%d")
show_time = today.strftime("%X")
header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}
response = requests.post(url=URL_NAME, json=json_params, headers=header)
exercise = response.json()
doc_exercise = exercise["exercises"][0]["name"].title()
doc_duration = exercise["exercises"][0]["duration_min"]
doc_calories = round(exercise["exercises"][0]["nf_calories"])

shetty_params = {
    "sheet1": {
        "date": f"{show_day}/{show_month}/{show_year}",
        "time": show_time,
        "exercise": doc_exercise,
        "duration": doc_duration,
        "calories": doc_calories
    }
}

response_doc = requests.post(url=shetty_endpoint, json=shetty_params)
print(response_doc.text)
