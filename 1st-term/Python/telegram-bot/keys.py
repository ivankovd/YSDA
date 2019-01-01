import json

with open("./keys.json") as f:
	keys_dict = json.load(f)

TELEGRAM_API_TOKEN = keys_dict["TELEGRAM_API_TOKEN"]
TRANSLATE_KEY = keys_dict["TRANSLATE_KEY"]
WEATHER_KEY = keys_dict["WEATHER_KEY"]
BING_KEY = keys_dict["BING_KEY"]
PROXY_KEY = keys_dict["PROXY_KEY"]
