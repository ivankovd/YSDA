import telebot
from telebot import apihelper

import keys
from parse_request.parser import TextParser
from picture_search.pic_finder import PicFinder
from utils import config
from yandex_weather.meteum import Meteum

apihelper.proxy = {
    'https': keys.PROXY_KEY
}

# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(keys.TELEGRAM_API_TOKEN)
text_parser = TextParser()
meteum = Meteum()
pic_finder = PicFinder()


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, config.START_MSG)


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id, config.HELP_MSG)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    print("=" * 50, "\nstart text parser")
    parse_params = text_parser.parse(message.text)
    if parse_params["geoid"] is None:
        bot.send_message(message.chat.id, config.CITY_NOT_FOUND_MSG)
        return
    elif parse_params["predict_day"] is None:
        bot.send_message(message.chat.id, config.ZERO_PREDICT_MSG)
        return

    meteum_response = meteum.predict(parse_params)

    print("=" * 50)
    print(meteum_response)
    print("=" * 50)
    if meteum_response["plot"]:
        bot.send_message(message.chat.id, config.AFTER_PLOT_MSG)
        with open(meteum_response["path_to_plot"], "rb") as photo:
            bot.send_photo(message.chat.id, photo=photo)

        # os.system("rm {}".format(meteum_response["path_to_plot"]))

    else:
        bot.send_message(message.chat.id, meteum_response["text"])

    pic_response = pic_finder.get_pic(
        meteum_response["search_condition"] + " " + parse_params[
            "en_city"].title()
    )
    bot.send_photo(message.chat.id, pic_response["url"])


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception:
            pass
