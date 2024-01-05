import telebot
from telebot import types
import json
import re
import shutil
from utils.Transposition import transposition
from utils.REF import ref
from utils.RREF import rref
from utils.ERO import stroka_ERO, start_opertions_tb
from utils.input_matrix import hlp, input_matrix_bt
import numpy as np
import os

bot = telebot.TeleBot("")



def all_button():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btm1 = types.InlineKeyboardButton("ERO", callback_data="ERO")
    btm2 = types.InlineKeyboardButton("REF", callback_data="REF")
    btm3 = types.InlineKeyboardButton("RREF", callback_data="RREF")
    btm4 = types.InlineKeyboardButton("DET", callback_data="DET")
    btm7 = types.InlineKeyboardButton("Inverse", callback_data="Inverse")
    btm8 = types.InlineKeyboardButton("Transposition", callback_data="Transposition")
    markup.add(btm1, btm2, btm3, btm4, btm7, btm8)
    return markup


@bot.message_handler(commands=['start'])
def start(message: types.Message, verno=True):
    if os.path.exists('data'):
        shutil.rmtree('data')
        os.mkdir('data')
    if verno:
        bot.send_message(message.chat.id, f"{hlp()}")
        bot.send_message(message.chat.id, "Введите матрицу:")
        bot.register_next_step_handler(message=message, callback=matrix_entry)
    else:
        bot.send_message(message.chat.id, f"{hlp()}")
        bot.send_message(message.chat.id, "Введите матрицу верно:")
        bot.register_next_step_handler(message=message, callback=matrix_entry)


def matrix_entry(message):
    if message.text != '/start':
        matrix = list(map(lambda x: x.split(), message.text.split('\n')))
        if len(set(map(len, matrix))) == 1:
            try:
                matrix = list(map(int, message.text.split()))
                markup = all_button()
                with open(f"data/{message.chat.id}.json", "w", encoding="utf-8") as file:
                    json.dump(message.text, file)
                bot.send_message(message.chat.id, f"Select operation", reply_markup=markup)
            except ValueError:
                start(message, verno=False)
        else:
            start(message, verno=False)
    else:
        start(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_function(call):
    with open(f"data/{call.from_user.id}.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    matrix = input_matrix_bt(data)

    if call.data == "REF":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("All the steps", callback_data="All the steps ref"))
        bot.send_message(call.message.chat.id, f"{ref(data)}", reply_markup=markup)
    elif call.data == "RREF":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("All the steps", callback_data="All the steps rref"))
        bot.send_message(call.message.chat.id, f"{rref(data)}", reply_markup=markup)
    elif call.data == "DET":
        try:
            bot.send_message(call.message.chat.id, f"det(A) = {round(np.linalg.det(matrix), 3)}")
        except np.linalg.LinAlgError:
            bot.send_message(call.message.chat.id, "matrix must be square for det(A)")
    elif "Inverse" == call.data:
        try:
            if np.linalg.det(matrix) != 0:
                bot.send_message(call.message.chat.id, f"Inverse:\n{rref(data, inv=True)}")
            else:
                bot.send_message(call.message.chat.id, "Matrix with det = 0 has no inverse")
        except np.linalg.LinAlgError:
            bot.send_message(call.message.chat.id, "matrix must be square")

    elif call.data == "All the steps ref":
        bot.send_message(call.message.chat.id, f"{ref(data, long=True)}")
    elif call.data == "All the steps rref":
        bot.send_message(call.message.chat.id, f"{rref(data, long=True)}")
    elif "ERO" == call.data:
        bot.send_message(call.message.chat.id, stroka_ERO)
        bot.register_next_step_handler(message=call.message, callback=opertion_tb)
    elif "Transposition" == call.data:
        markup = all_button()
        new_data = transposition(data)
        with open(f"data/{call.message.chat.id}.json", "w", encoding="utf-8") as file:
            json.dump(new_data, file)
        bot.send_message(call.message.chat.id, transposition(data), reply_markup=markup)


def check(data):
    # data = data.split()
    data = re.split(r'\s|/', data)
    if len(data) == 3 and 't' in data:
        try:
            lst = list(map(int, data[:-1]))
            return True
        except ValueError:
            return False

    if len(data) == 2 or len(data) == 3 or len(data) == 4 or len(data) == 5 :
        try:
            lst = list(map(int, data))
            return True
        except ValueError:
            return False
    return False


def opertion_tb(message):
    data = message.text
    if check(data):
        markup = all_button()
        with open(f"data/{message.chat.id}.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        new_data = start_opertions_tb(data, message.text)
        if new_data:
            with open(f"data/{message.chat.id}.json", "w", encoding="utf-8") as file:
                json.dump(new_data, file)
            bot.send_message(message.chat.id, new_data, reply_markup=markup)


bot.infinity_polling()
