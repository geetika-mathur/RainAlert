import requests
from twilio.rest import Client


api_key = "API key"
response = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "account SID"
auth_token  = "auth_token"

weather_params = {
"lat": 123,
"lon": 456,
"appid": api_key
}

data = requests.get(response,params= weather_params)
data.raise_for_status()
weather_data = data.json()
weather_slice = weather_data["list"][:9]
print(weather_slice )
for hour_data in weather_slice :
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+1234567890",
        from_="+19876543210",
        body="Its going to Rain! Bring an umbrella☂️")

    print(message.status)

# print(weather_data["list"][0]["weather"])


