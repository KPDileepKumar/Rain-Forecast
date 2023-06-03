import requests
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
import os

api_key = "275c245e72c727b7f2d74a0c4f7bc0c8"
account_sid = "ACf16a968c08bd490d98f3b2829bc3bceb"
auth_token = "82f8adf3fbe65c7b64c67ecb2078bb97"

# account_sid = "ACf16a968c08bd490d98f3b2829bc3bceb"
# auth_token = os.environ["AUTH_TOKEN"]
# api_key = os.environ["OWM_API_KEY"]

END_POINT = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {"lat": 12.650264, "lon": 77.440017, "appid": api_key}
response = requests.get(url=END_POINT, params=parameters)
response.raise_for_status()
data = response.json()["list"][0:4]
will_rain = False
for hour_data in data:
    w_id = hour_data["weather"][0]["id"]
    if w_id < 700:
        will_rain = True
if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ.get("https_proxy")}
    client = Client(account_sid, auth_token)  # http_client=proxy_client)

    message = client.messages.create(
        body="It's going to rain today, remember to bring an umbrella☔",
        from_='+16203902014',
        to='+918971474762'
    )

    print(message.status)
