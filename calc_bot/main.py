from operation import *
import telebot
from logger import *
from telebot import types


bot = telebot.TeleBot("токен")


@bot.message_handler(commands=['start', 'help'])
def welcome_messages(message):
    text = 'Привет! Для вычислений нажми /calc'
    bot.reply_to(message, text)


@bot.message_handler(commands=['calc'])
def get_text_messages(message):
    text = 'Введите выражение для вычисления через пробелы: '
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, make_calc)


def make_calc(message):
    some_str = message.text
    res = math_op(some_str)
    bot.send_message(message.chat.id, f'{some_str} = {res}\n')
    save_log(some_str, res)


bot.polling(none_stop=True)