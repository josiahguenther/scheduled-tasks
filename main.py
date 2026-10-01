import requests
import smtplib
import os

API_KEY = "618419268a6ac434cf26d53da3be8356"
MY_LAT = 33.908989
MY_LONG = -118.009949
will_rain = False
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

forecast = requests.get("https://api.openweathermap.org/data/2.5/forecast", params= parameters)
forecast.raise_for_status()
weather_data = forecast.json()
"""total = weather_data["list"][0]["weather"][0]["id"] + weather_data["list"][1]["weather"][0]["id"] + weather_data["list"][2]["weather"][0]["id"] + weather_data["list"][3]["weather"][0]["id"]

if total/4 < 800:
    print("Bring an umbrella.")"""

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as new_connection:
        new_connection.starttls()
        new_connection.login(user=my_email, password=password)
        new_connection.sendmail(from_addr=my_email, to_addrs="josiah@josiahguenthermagic.com",
                                msg=f"Subject:It's Going to Rain!\n\nBring an Umbrella")
