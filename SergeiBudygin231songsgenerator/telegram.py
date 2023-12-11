import telebot
from telebot import types
from generator import generator_track

bot = telebot.TeleBot("token")


@bot.message_handler(commands=['start'])
def start_message(message):
    last_namee = " " + message.from_user.last_name if message.from_user.last_name else ""
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}{last_namee}!')
    bot.register_next_step_handler(message, callback=smt_singer)


def smt_singer(message):
    mes = message.text.split()
    print(mes)
    if len(mes) == 3 or len(mes) == 2:

        bot.send_message(message.chat.id, generator_track(*mes))
    bot.register_next_step_handler(message, callback=smt_singer)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, message)


bot.infinity_polling()
