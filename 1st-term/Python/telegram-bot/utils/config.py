import re
import string

#
# Parse params
#

PUNCTUATION = set(string.punctuation) - set('-')

WEEKDAY = {
    "понедельник": 0,
    "вторник": 1,
    "среда": 2,
    "четверг": 3,
    "пятница": 4,
    "суббота": 5,
    "воскресенье": 6
}

SHORT_WEEKDAY = {
    "пн": 0,
    "вт": 1,
    "ср": 2,
    "чт": 3,
    "пт": 4,
    "сб": 5,
    "вс": 6
}

MONTH = {
    "январь": 1,
    "февраль": 2,
    "март": 3,
    "апрель": 4,
    "май": 5,
    "июнь": 6,
    "июль": 7,
    "август": 8,
    "сентябрь": 9,
    "октябрь": 10,
    "ноябрь": 11,
    "декабрь": 12
}

REG_MONTH_WORD = re.compile(r"\d{1,2} январь|\d{1,2} февраль|\d{1,2} март|"
                            r"\d{1,2} апрель|\d{1,2} май|\d{1,2} июнь|\d{1,2} "
                            r"июль|\d{1,2} август|\d{1,2} сентябрь|\d{1,2} "
                            r"октябрь|\d{1,2} ноябрь|\d{1,2} декабрь")

NOW_WORDS = ["сейчас", "сегодня"]
RELATIVE_WORDS = {
    "завтра": 1,
    "послезавтра": 2
}

BASIC_WORDS = {"погода", "какой", "будет"}

#
# Forecast params
#
CLOUDNESS = {
    0: {
        "ru": "ясно",
        "en": "clear",
        "emoji": "☀️"
    },
    0.25: {
        "ru": "малооблачно",
        "en": "clear",
        "emoji": "🌤"
    },
    0.5: {
        "ru": "облачно с прояснениями",
        "en": "cloudy",
        "emoji": "⛅️"
    },
    0.75: {
        "ru": "облачно с прояснениями",
        "en": "cloudy",
        "emoji": "⛅️"
    },
    1: {
        "ru": "пасмурно",
        "en": "overcast",
        "emoji": "☁️️"
    },
}

SEARCH_CONDITIONS = {
    "clear": "sunny",
    "mostly-clear": "sunny",
    "partly-cloudy": "cloudy",
    "overcast": "cloudy",
    "partly-cloudy-and-light-rain": "cloudy",
    "partly-cloudy-and-rain": "rainy",
    "overcast-and-rain": "thunderstorm",
    "overcast-thunderstorms-with-rain": "thunderstorm",
    "cloudy": "cloudy",
    "cloudy-and-light-rain": "rainy",
    "overcast-and-light-rain": "rainy",
    "cloudy-and-rain": "rainy",
    "overcast-and-wet-snow": "rainy",
    "partly-cloudy-and-light-snow": "snowy",
    "partly-cloudy-and-snow": "snowy",
    "overcast-and-snow": "snowy",
    "cloudy-and-light-snow": "snowy",
    "overcast-and-light-snow": "snowy",
    "cloudy-and-snow": "snowy",
}

EMOJI_CONDITIONS = {
    "clear": "☀️",
    "mostly-clear": "☀️",
    "partly-cloudy": "☁️",
    "overcast": "☁️",
    "partly-cloudy-and-light-rain": "☁️",
    "partly-cloudy-and-rain": "🌧",
    "overcast-and-rain": "⛈",
    "overcast-thunderstorms-with-rain": "⛈",
    "cloudy": "☁️",
    "cloudy-and-light-rain": "🌧",
    "overcast-and-light-rain": "🌧",
    "cloudy-and-rain": "🌧",
    "overcast-and-wet-snow": "🌧",
    "partly-cloudy-and-light-snow": "❄️",
    "partly-cloudy-and-snow": "❄️",
    "overcast-and-snow": "❄️",
    "cloudy-and-light-snow": "❄️",
    "overcast-and-light-snow": "❄️",
    "cloudy-and-snow": "❄️",
}

TRANSLATE_CONDITIONS = {
    'blowing-snow-metar-synop': 'метель',
    'clear': 'ясно',
    'cloudy': 'облачно с прояснениями',
    'cloudy-and-light-rain': 'небольшой дождь',
    'cloudy-and-light-snow': 'небольшой снег',
    'cloudy-and-rain': 'дождь',
    'cloudy-and-snow': 'снег',
    'continuous-heavy-rain-metar-synop': 'сильный дождь',
    'decreasing-moon': 'Убывающая луна',
    'drifting-snow-metar-synop': 'слабая метель',
    'drizzle-metar-synop': 'морось',
    'dust-metar-synop': 'пыль',
    'dust-suspension-metar-synop': 'пылевая взвесь',
    'duststorm-metar-synop': 'пыльная буря',
    'first-quarter': 'Первая четверть',
    'fog-metar-synop': 'туман',
    'freezing-rain-metar-synop': 'ледяной дождь',
    'full-moon': 'Полнолуние',
    'growing-moon': 'Растущая луна',
    'hail-metar-synop': 'град',
    'heavy-rain-metar-synop': 'ливень',
    'ice-pellets-metar-synop': 'ледяная крупа',
    'last-quarter': 'Последняя четверть',
    'light-rain-metar-synop': 'небольшой дождь',
    'light-snow-metar-synop': 'небольшой снег',
    'magnetic-field_0': 'спокойное',
    'magnetic-field_1': 'неустойчивое',
    'magnetic-field_2': 'слабо возмущенное',
    'magnetic-field_3': 'возмущенное',
    'magnetic-field_4': 'магнитная буря',
    'magnetic-field_5': 'большая магнитная буря',
    'mist-metar-synop': 'дымка',
    'moderate-rain-metar-synop': 'дожди',
    'new-moon': 'Новолуние',
    'overcast': 'пасмурно',
    'overcast-and-light-rain': 'небольшой дождь',
    'overcast-and-light-snow': 'небольшой снег',
    'overcast-and-rain': 'сильный дождь',
    'overcast-and-snow': 'снегопад',
    'overcast-and-wet-snow': 'дождь со снегом',
    'overcast-thunderstorms-with-rain': 'сильный дождь, гроза',
    'partly-cloudy': 'малооблачно',
    'partly-cloudy-and-light-rain': 'небольшой дождь',
    'partly-cloudy-and-light-snow': 'небольшой снег',
    'partly-cloudy-and-rain': 'дождь',
    'partly-cloudy-and-snow': 'снег',
    'pollution-affect-aqi-0-2-names-other': 'Безопасный уровень. Подходит для прогулок на свежем воздухе',
    'pollution-affect-aqi-2-4-names-o3': 'Очень чувствительные люди могут испытывать дискомфорт в органах дыхательной системы',
    'pollution-affect-aqi-2-4-names-other': 'Безопасный уровень. Подходит для прогулок на свежем воздухе',
    'pollution-affect-aqi-2-4-names-pm2-5-dry-or-pm10': 'Очень чувствительные люди могут испытывать дискомфорт в органах дыхательной системы. Возможны обострения у страдающих заболеваниями сердца и лёгких, а также у пожилых людей',
    'pollution-affect-aqi-4-6-names-co': 'Люди с заболеваниями сердца могут испытывать сложности при обычных физических нагрузках — ощущать боль в области грудной клетки',
    'pollution-affect-aqi-4-6-names-no2': 'Люди, страдающие астмой, могут ощущать стеснение в груди, дискомфорт при дыхании',
    'pollution-affect-aqi-4-6-names-o3': 'Люди с заболеваниями лёгких, больные астмой, дети, пожилые люди и уличные работники с большой вероятностью могут испытывать дискомфорт в органах дыхательной системы',
    'pollution-affect-aqi-4-6-names-other': 'Людям с заболеваниями сердца или легких, детям, пожилым людям и уличным работникам следует уменьшить продолжительность пребывания или активность занятий на улице',
    'pollution-affect-aqi-4-6-names-pm2-5-dry-or-pm10': 'Увеличенная вероятность проявления симптомов респираторных заболеваний у чувствительных людей. Также обострение заболеваний сердца и лёгких, повышение вероятности преждевременной смерти, в том числе у пожилых людей',
    'pollution-affect-aqi-4-6-names-so2': 'Люди, страдающие астмой, могут ощущать стеснение в груди, дискомфорт при дыхании',
    'pollution-affect-aqi-6-8-names-co': 'Люди с заболеваниями сердца могут испытывать сложности при обычных физических нагрузках — ощущать боль в области грудной клетки',
    'pollution-affect-aqi-6-8-names-no2': 'Более частое проявление симптомов респираторных заболеваний у страдающих астмой — стеснение в груди и хрипы. Возможно обострение других заболеваний лёгких',
    'pollution-affect-aqi-6-8-names-o3': 'Большая вероятность проявления симптомов респираторных заболеваний и затруднённое дыхание у людей с заболеваниями лёгких, детей, пожилых людей и уличных работников. Возможен дискомфорт в органах дыхательной системы у всех людей',
    'pollution-affect-aqi-6-8-names-other': 'Людям с заболеваниями сердца и лёгких, детям, пожилым людям и уличным работники категорически противопоказана продолжительная или активная деятельность на улице. Все остальные также должны сократить продолжительность или активность своей деятельности на открытом воздухе',
    'pollution-affect-aqi-6-8-names-pm2-5-dry-or-pm10': 'Повышенный риск обострения заболеваний сердца и легких, высокая вероятность преждевременной смерти среди людей, страдающих такими заболеваниями, а также среди пожилых людей',
    'pollution-affect-aqi-6-8-names-so2': 'Более частое проявление симптомов респираторных заболеваний у страдающих астмой — стеснение в груди и хрипы. Возможно обострение других заболеваний лёгких',
    'pollution-affect-aqi-8-10-names-co': 'Значительное обострение симптомов сердечно-сосудистых болезней (неприятных ощущений в груди) у людей с заболеваниями сердца',
    'pollution-affect-aqi-8-10-names-no2': 'Значительное увеличение симптомов астмы — хрипов и одышки. Обострение других заболеваний лёгких',
    'pollution-affect-aqi-8-10-names-o3': 'Заметно выраженные симптомы и нарушение дыхания у людей с заболеваниями лёгких типа астмы, у детей, пожилых людей и уличных работников. Повышенная вероятность появления дискомфорта при дыхании у всех остальных',
    'pollution-affect-aqi-8-10-names-other': 'Людям с заболеваниями сердца или легких, пожилым людям, детям и уличным работникам следует избегать любой физической активности на открытом воздухе. Все остальные должны избегать продолжительной или активной деятельности на улице',
    'pollution-affect-aqi-8-10-names-pm2-5-dry-or-pm10': 'Значительное обострение заболеваний сердца и легких и повышение вероятности преждевременной смерти у людей с болезнями сердца и лёгких, а также у пожилых людей. Усиление дискомфорта при дыхании у всех остальных',
    'pollution-affect-aqi-8-10-names-so2': 'Значительное увеличение симптомов астмы — хрипов и одышки. Обострение других заболеваний лёгких',
    'pollution-level-danger': 'Опасный уровень загрязнения воздуха',
    'pollution-level-high': 'Высокий уровень загрязнения воздуха',
    'pollution-level-low': 'Низкий уровень загрязнения воздуха',
    'pollution-level-medium': 'Средний уровень загрязнения воздуха',
    'pollution-substance-co': 'моноксид углерода',
    'pollution-substance-co-genitive': 'моноксида углерода',
    'pollution-substance-no': 'окись азота',
    'pollution-substance-no-genitive': 'окиси азота',
    'pollution-substance-no2': 'диоксид азота',
    'pollution-substance-no2-genitive': 'диоксида азота',
    'pollution-substance-o3': 'озон',
    'pollution-substance-o3-genitive': 'озона',
    'pollution-substance-pm10': 'взвешенные частицы',
    'pollution-substance-pm10-genitive': 'взвешенных частиц',
    'pollution-substance-pm2_5_dry': 'мелкодисперсные взвешенные частицы',
    'pollution-substance-pm2_5_dry-genitive': 'мелкодисперсных взвешенных частиц',
    'pollution-substance-so2': 'диоксид серы',
    'pollution-substance-so2-genitive': 'диоксида серы',
    'rain-metar-synop': 'дождь',
    'showers-metar-synop': 'ливни',
    'smoke-metar-synop': 'смог',
    'snow-metar-synop': 'снег',
    'snow-showers-metar-synop': 'снегопад',
    'thunderstorm-metar-synop': 'гроза',
    'thunderstorm-wet-snow-metar-synop': 'гроза, дождь со снегом',
    'thunderstorm-with-duststorm-metar-synop': 'пыльная буря с грозой',
    'thunderstorm-with-hail-metar-synop': 'гроза с градом',
    'thunderstorm-with-rain-metar-synop': 'дождь с грозой',
    'thunderstorm-with-snow-metar-synop': 'гроза, снег',
    'tornado-metar-synop': 'торнадо',
    'uv-index-0': 'Низкий',
    'uv-index-1': 'Низкий',
    'uv-index-10': 'Очень высокий',
    'uv-index-11': 'Экстремальный',
    'uv-index-2': 'Низкий',
    'uv-index-3': 'Средний',
    'uv-index-4': 'Средний',
    'uv-index-5': 'Средний',
    'uv-index-6': 'Высокий',
    'uv-index-7': 'Высокий',
    'uv-index-8': 'Очень высокий',
    'uv-index-9': 'Очень высокий',
    'volcanic-ash-metar-synop': 'вулканический пепел',
    'wet-snow-metar-synop': 'дождь со снегом',
    'wind-c': 'штиль',
    'wind-c-short': 'штиль',
    'wind-e': 'восточный',
    'wind-e-short': 'В',
    'wind-n': 'северный',
    'wind-n-short': 'С',
    'wind-ne': 'северо-восточный',
    'wind-ne-short': 'СВ',
    'wind-nw': 'северо-западный',
    'wind-nw-short': 'СЗ',
    'wind-s': 'южный',
    'wind-s-short': 'Ю',
    'wind-se': 'юго-восточный',
    'wind-se-short': 'ЮВ',
    'wind-sw': 'юго-западный',
    'wind-sw-short': 'ЮЗ',
    'wind-w': 'западный',
    'wind-w-short': 'З'
}

FORECAST_TEMPLATE = "Погода в городе {} на {}\n" \
                    "Температура:\n" \
                    "  🌝  Днем: {} °C\n" \
                    "  🌚  Ночью: {} °C\n" \
                    "Скорость ветра: {} м/с\n" \
                    "Давление: {} мм.рт.ст.\n" \
                    "Облачность: {}\n" \
                    "Осадки: {}\n"

#
# Request pages
#

TRANSLATE_PAGE = "https://translate.yandex.net/api/v1.5/tr.json/translate?"
WEATHER_PAGE = "https://api.weather.yandex.ru/v1/forecast?l10n=true&extra=true"
SEARCH_PIC_PAGE = "https://api.cognitive.microsoft.com/bing/v7.0/images/search?"

#
# Messages
#

START_MSG = "Привет! Я бот, который предсказывает погоду! "
HELP_MSG = "Просто спроси у меня где и на какое число ты хочешь узнать прогноз " \
           "и я тебе отвечу! Не беспокойся, я пойму запрос в любой форме"
CITY_NOT_FOUND_MSG = "Город не нашелся в базе данных :("
ZERO_PREDICT_MSG = "Я не понял, в какой день вам нужен прогноз :("
AFTER_PLOT_MSG = "Так как ты не сказал мне точную дату, на которую тебе нужен прогноз, " \
                 "то я подготовил для тебя вот этот график, а также фотографию" \
                 " с погодой на текущий день в запрашиваемом городе"
