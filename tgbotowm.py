import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
# ...  - ВСТАВЬ OWM
owm = OWM('...')
mgr = owm.weather_manager()
# ... - ВСТАВЬ БОТА
bot = telebot.TeleBot("...")

@bot.message_handler(commands=['start'])

def send_welcome(message):
        sti = open('...', 'rb') # ПРИВЕТСТВЕННЫЙ СТИКЕР
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, "Добро пожаловать, я - Бот.\nМогу рассказать о погоде в любой точке мира.\nКакой город тебя интересует?")

@bot.message_handler (content_types=["text"] )
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    windd = w.wind() ["speed"]

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура " + str(temp) + " °С." + "\n"
    answer += "Скорость ветра около " + str(windd) + " м/c."

    bot.send_message (message.chat.id, answer)

bot.polling(none_stop=True)
                
