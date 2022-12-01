import telebot
import random
from ladder import *


player = ''
max_candies = 28
stash = 221
bot = telebot.TeleBot("SOME_TOKEN")


def check_win():
    if stash < 29:
        return True
    else:
        return False


@bot.message_handler(commands=['start'])
def welcome_messages(message):
    global player
    player = message.from_user.first_name
    text = f'Привет, {player}! Для новой игры введи /game\nДля просмотра рейтинговой таблицы введи /ladder'
    bot.reply_to(message, text)


@bot.message_handler(commands=['ladder'])
def welcome_messages(message):
    text = see_ladder()
    bot.reply_to(message, text)


@bot.message_handler(commands=['game'])
def rules_messages(message):
    global stash
    stash = 221
    text = f'Добро пожаловать в копитал-шоу Сундук конфет!\nПравила игры: в сундуке Candyman лежат конфеты, чьё количество задано игроком.\nИгрок и Candyman ходят по очереди, право первого хода определяется жеребьёвкой.\nЗа один ход можно взять из сундука не меньше 1 и не больше {max_candies} конфет.\nСделавшему последний ход достаются все конфеты =)\nТы ходишь первым. Сколько конфет возьмешь?'
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, candy_game)


@bot.message_handler(content_types=['text'])
def candy_game(message):
    global stash
    global max_candies
    global player
    if check_win():
        bot.send_message(message.chat.id, f'{player} победил!')
        write_ladder('Человек')
        return
    take = message.text
    if not take.isdigit() or int(take) > max_candies or int(take) < 1:
        bot.send_message(message.chat.id, f'Нужно вести число от 1 до {max_candies}')
        return
    else:
        take = int(message.text)
    stash -= take
    bot.send_message(message.chat.id, f'{player} взял {take} конфет. В сундуке осталось {stash} конфет. Следущим ходит Candyman.')
    if check_win():
        bot.send_message(message.chat.id, 'Candyman победил!')
        write_ladder('Candyman')
        return
    if stash > 57:
        take = random.randint(1, 28)
    if 28 < stash < 57:
        take = stash - 29
    stash -= take
    bot.send_message(message.chat.id, f'Candyman взял {take} конфет. В сундуке осталось {stash} конфет. Следущим ходит игрок. Сколько конфет возьмешь, {player}?')
