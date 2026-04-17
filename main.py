import requests
from twilio.rest import Client

account_sid = "test"
auth_token = "test"
client = Client(account_sid, auth_token)

OPEN_WEATHER_API_KEY = "test"
MY_LAT = 53.285347
MY_LONG = -9.012642
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid":OPEN_WEATHER_API_KEY,
    "cnt":3,
    "units":"metric"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
weather_codes = [int(data_point["weather"][0]["id"]) for data_point in data["list"] if int(data_point["weather"][0]["id"]) < 700]
for codes in weather_codes:
    if codes < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella",
        to='whatsapp:+917738405806'
    )


# for i in data["list"]:
#     # print(i["weather"])
#     # print(i["dt_txt"])
#     print(f"The weather in Ballybane at {i["dt_txt"]} will be mostly {i["weather"][0]["main"]} and it would be {i["weather"][0]["description"]}.")

# for data_point in data["list"]:
#     print(int(data_point["weather"][0]["id"]))
#     if int(data_point["weather"][0]["id"]) < 700:
#
#         print("Bring an umbrella!")
# message = client.messages.create(
#     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#     from_="+19892822992",
#     to="+353 89 461 9023",
# )
