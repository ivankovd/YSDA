import requests

# ANS_SIMPLE = {}  #
text_sample = 'Добро пожаловать'

# ANS_COMPLEX = {}
text_complex = 'Сюда пришли люди, которым было приятнее быть друг с другом, ' \
               'чем порознь, которые терпеть не могли всякого рода ' \
               'воскресений, ' \
               'потому что в воскресенье им было скучно. Маги, Люди с ' \
               'большой ' \
               'буквы, и девизом их было -- "Понедельник начинается в ' \
               'субботу". ' \
               'Они были магами потому, что очень много знали, так ' \
               'много, что ' \
               'количество перешло у них наконец в качество, и они ' \
               'стали с миром ' \
               'в другие отношения, нежели обычные люди. Они работали ' \
               'в институте, ' \
               'который занимался прежде всего проблемами человеческого ' \
               'счастья и ' \
               'смысла человеческой жизни, но даже среди них никто ' \
               'точно не знал, ' \
               'что такое счастье и в чем именно смысл жизни. И они приняли ' \
               'рабочую гипотезу, что счастье в непрерывном познании ' \
               'неизвестного ' \
               'и смысл жизни в том же. Каждый человек -- маг в душе, ' \
               'но он ' \
               'становится магом только тогда, когда начинает меньше ' \
               'думать о ' \
               'себе и больше о других, когда работать ему становится ' \
               'интереснее, ' \
               'чем развлекаться в старинном смысле этого слова.'

YANDEX_TRANSLATE_KEY = "trnsl.1.1.20180524T001733Z.0b413fdcb28264eb." \
                       "75239dbc83b745f6c066d1ee7ff37b195250b03d"
TRANSLATE_PAGE = "https://translate.yandex.net/api/v1.5/tr.json/" \
                 "translate?"
PAIRS_TRANSLATE_PAGE = "https://translate.yandex.net/api/v1.5" \
                       "/tr.json/getLangs?"


def translate(text, lang_pair):
    req = requests.get(
        url=TRANSLATE_PAGE,
        params={
            "key": YANDEX_TRANSLATE_KEY,
            "text": text,
            "lang": lang_pair
        }).json()
    # print(req)
    return req["text"][0]


def get_translate_pairs():
    req = requests.get(
        url=PAIRS_TRANSLATE_PAGE,
        params={
            "key": YANDEX_TRANSLATE_KEY,
            "ui": "en"
        }
    ).json()
    all_lang_pars = req["langs"]
    need_foreign_langs = list(filter(lambda l: "e" in l, all_lang_pars.keys()))
    need_lang_pairs = []
    for foreign_lang in need_foreign_langs:
        need_lang_pairs.append([
            "{}-{}".format("ru", foreign_lang),
            "{}-{}".format(foreign_lang, "ru"),
            foreign_lang
        ])

    return need_lang_pairs


def run(text, need_lang_pairs):
    response = {}
    for lang_pair in need_lang_pairs:
        ru_to_foreign, foreign_to_ru, code_foreign = lang_pair
        len_chain = 1
        text_to_translate = text
        while True:
            if len_chain > 8:
                response[code_foreign] = "too_much"
                # print(code_foreign, "too_much")
                break

            translated_text = translate(text_to_translate, ru_to_foreign)
            untranslated_text = translate(translated_text, foreign_to_ru)

            if text_to_translate == untranslated_text:
                response[code_foreign] = len_chain
                # print(code_foreign, len_chain)
                break

            text_to_translate = untranslated_text
            len_chain += 1
    return response


# need_lang_pairs = get_translate_pairs()
# response = run(text_complex, need_lang_pairs)
# ANS_COMPLEX = response
ANS_SIMPLE = {"be": 1, "ceb": 1, "de": 1, "el": 1, "en": 1, "eo": 1, "es": 1,
              "et": 1, "eu": 1, "he": 1, "ne": 1, "te": 1}

ANS_COMPLEX = {'be': 2, 'ceb': 6, 'de': 'too much', 'el': 3, 'en': 3,
               'eo': 'too much', 'es': 3, 'et': 'too much', 'eu': 7, 'he': 4,
               'ne': 3, 'te': 'too much'}
