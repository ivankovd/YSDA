import os
import random
import string
import tempfile

import matplotlib.pyplot as plt
import requests

import keys
from utils import config


class Meteum:
    def __init__(self):
        self.url = config.WEATHER_PAGE
        self.weather_header = {
            'X-Yandex-API-Key': keys.WEATHER_KEY
        }

        self.forecast_template = config.FORECAST_TEMPLATE

    def _make_request(self, params):
        req = requests.get(
            url=self.url,
            params={"geoid": params["geoid"]}, headers=self.weather_header)
        req = req.json()
        return req

    def predict(self, params):
        """
        :param params: params for request, geoid and predict_day
        :return:
        """
        req = self._make_request(params)

        if params["predict_day"] < 0:
            response = self._draw_plot(req, params)
            response["search_condition"] = config.SEARCH_CONDITIONS[
                req["forecasts"][0]["parts"]["day"]["condition"]
            ]
            response.update(req["forecasts"][0])
            return response
        else:
            day_forecast = req["forecasts"][params["predict_day"]]
            # print(day_forecast)
            print(config.TRANSLATE_CONDITIONS[day_forecast["parts"]["day"][
                    "condition"]])
            text_response = self.forecast_template.format(
                params["ru_city"].title(),
                day_forecast["date"],
                day_forecast["parts"]["day"]["temp_avg"],
                day_forecast["parts"]["night"]["temp_avg"],
                day_forecast["parts"]["day"]["wind_speed"],
                day_forecast["parts"]["day"]["pressure_mm"],
                config.CLOUDNESS[day_forecast["parts"]["day"]["cloudness"]][
                    "emoji"] + " " + config.CLOUDNESS[day_forecast["parts"][
                    "day"]["cloudness"]]["ru"],
                config.EMOJI_CONDITIONS[day_forecast["parts"]["day"][
                    "condition"]] + " " + config.TRANSLATE_CONDITIONS[
                    day_forecast["parts"]["day"]["condition"]]
            )
            response = {"plot": False, "text": text_response,
                        "search_condition": config.SEARCH_CONDITIONS[
                            day_forecast["parts"]["day"]["condition"]
                        ]}
            response.update(day_forecast)
            return response

    def _draw_plot(self, req, params):
        dates, temp_day, temp_night = [], [], []
        for day_forecast in req["forecasts"]:
            dates.append(day_forecast["date"])
            temp_day.append(day_forecast["parts"]["day"]["temp_avg"])
            temp_night.append(day_forecast["parts"]["night"]["temp_avg"])

        fig = plt.figure(figsize=(15, 10))
        ax = plt.subplot(111)
        ax = plt.plot(dates, temp_day, "-o", label="Днем")
        ax = plt.plot(dates, temp_night, "-o", label="Ночью")
        plt.grid(ls=":")
        plt.title(
            "Среднее значение температуры днем и ночью в городе {} за {} дней".format(
                params["ru_city"].title(), len(dates)), fontsize=18)
        plt.xlabel("День", fontsize=15)
        plt.ylabel("Температура, °C", fontsize=15)
        plt.legend(loc="best", fontsize=15)
        plt.yticks(fontsize=15)
        random_name = "".join(
            random.choices(string.ascii_letters, k=10)) + ".png"

        print(random_name)
        path_to_save = os.path.join(tempfile.gettempdir(), random_name)
        print(path_to_save)
        fig.savefig(path_to_save, pad_inches=0)
        return {
            "plot": True,
            "path_to_plot": path_to_save
        }


if __name__ == '__main__':
    meteum = Meteum()
    pred = meteum.predict({
        "ru_city": "Санкт-Петербург",
        'geoid': 2,
        'predict_day': 0
    })
