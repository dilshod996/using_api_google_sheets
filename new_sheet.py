import requests

shet_endpoint = "https://api.sheety.co/889c64818b829384ee97ee75c268619f/newSheet/sheet1"

shet_params = {"sheet1":
    {
    "name": "Dilshod",
    "email": "sadfhasdf",
    "number": 345345345345
    }
}

response = requests.post(url=shet_endpoint, json=shet_params)
print(response.text)