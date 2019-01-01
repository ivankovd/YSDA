import json
import re
from datetime import datetime

import pymorphy2
import requests

import keys
from utils import config


class TextParser:
    def __init__(self):
        with open("./utils/cities.txt") as f:
            self.cities_dict = json.load(f)
            self.cities_set = set(self.cities_dict)

        self.pymorphy2_info = []
        self.now_date = datetime.now()

    def parse(self, text):
        self.now_date = datetime.now()
        params = {}
        text = self._del_punctuation(text)
        normal_words = self._lemmatization(text)
        normal_words = list(
            filter(lambda w: w not in config.BASIC_WORDS, normal_words)
        )
        print("normal_words", normal_words)
        params.update(self.find_city(normal_words))
        params.update(self.find_data(params["other_words"], normal_words))
        print(params)
        return params

    def _del_punctuation(self, text):
        return "".join(["" if i in config.PUNCTUATION else i for i in text])

    def _lemmatization(self, text):
        morph = pymorphy2.MorphAnalyzer()
        text = "".join(["" if i in config.PUNCTUATION else i for i in text])
        words = text.lower().split()

        self.pymorphy2_info = [morph.parse(word)[0] for word in words]
        normal_forms = []
        for pm2_info, word in zip(self.pymorphy2_info, words):
            if str(pm2_info.tag) != "PREP":
                normal_forms.append(pm2_info.normal_form)

        return normal_forms

    def translate(self, text):
        req = requests.get(url=config.TRANSLATE_PAGE,
                           params={
                               "key": keys.TRANSLATE_KEY,
                               "text": text,
                               "lang": "ru-en"
                           }).json()
        return req["text"][0].lower()

    def find_city(self, normal_forms):
        for word in normal_forms:
            en_word = self.translate(text=word)
            if en_word in self.cities_set:
                geoid = self.cities_dict[en_word]
                return {
                    "ru_city": word,
                    "en_city": en_word,
                    "geoid": geoid,
                    "other_words": set(normal_forms) - {word}
                }

        for i in range(0, len(normal_forms), 2):
            word = " ".join(normal_forms[i:i + 2])
            en_word = self.translate(text=word)
            if en_word in self.cities_set:
                geoid = self.cities_dict[en_word]
                return {
                    "ru_city": word,
                    "en_city": en_word,
                    "geoid": geoid,
                    "other_words": set(normal_forms) - set(word.split())
                }

        return {
            "geoid": None,
            "other_words": set(normal_forms)
        }

    def find_data(self, words, normal_words):
        print("#" * 50)
        print("!!!!!!words!!!!!", words)
        predict_day = None

        normal_sent = " ".join(normal_words)

        if len(words) == 0:
            predict_day = -1

        elif len(re.findall(config.REG_MONTH_WORD, normal_sent)) == 1:
            date = re.findall(config.REG_MONTH_WORD, normal_sent)[0]
            day, month = date.split(" ")
            day = int(day)
            month = config.MONTH[month]
            year = 2018
            date = datetime(day=day, month=month, year=year)
            predict_day = (date - self.now_date).days + 1

        else:
            for word in words:
                if word in config.NOW_WORDS:
                    predict_day = 0

                elif word in config.RELATIVE_WORDS:
                    predict_day = config.RELATIVE_WORDS[word]

                elif word in config.WEEKDAY:
                    predict_day = self._timedelta(config.WEEKDAY[word])

                elif word in config.SHORT_WEEKDAY:
                    predict_day = self._timedelta(config.SHORT_WEEKDAY[word])

        return {"predict_day": predict_day}

    def _timedelta(self, request_weekday):
        if request_weekday - self.now_date.weekday() >= 0:
            return request_weekday - self.now_date.weekday()
        else:
            return 7 - self.now_date.weekday() + request_weekday


if __name__ == '__main__':
    parser = TextParser()
    response = parser.parse("какая погода в Сан-Франциско завтра")
    print(response)
