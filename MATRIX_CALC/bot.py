import sqlite3
import telebot
from telebot import types
from fractions import Fraction as f
import requests
import json
import webbrowser
from decimal import Decimal

from REF import ref
from RREF import rref
from ERO import stroka_ERO, start_opertions_tb
from input_matrix import hlp, input_matrix_bt
from BD import bd_get_last
import numpy as np

bot = telebot.TeleBot("6181173220:AAF3-woXCuP3u15rTNeccbCJElP1T1En5_Y")


def all_button():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btm1 = types.InlineKeyboardButton("ERO", callback_data="ERO")
    btm2 = types.InlineKeyboardButton("REF", callback_data="REF")
    btm3 = types.InlineKeyboardButton("RREF", callback_data="RREF")
    btm4 = types.InlineKeyboardButton("DET", callback_data="DET")
    btm5 = types.InlineKeyboardButton("inverse", callback_data="inverse")
    btm6 = types.InlineKeyboardButton("transposition", callback_data="transposition")
    btm7 = types.InlineKeyboardButton("trace", callback_data="trace")
    btm8 = types.InlineKeyboardButton("last", callback_data="last")
    markup.add(btm1, btm2, btm3, btm4, btm5, btm6, btm7, btm8)
    return markup


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(message.chat.id, "Введите матрицу или /help:")
    conn = sqlite3.connect("mat.sql")
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS mat (id int auto_increment primary key, matrix varchar(1000))')
    conn.commit()
    cursor.close()
    conn.close()
    bot.register_next_step_handler(message=message, callback=matrix_entry)


@bot.message_handler(commands=['help'])
def start(message: types.Message):
    bot.send_message(message.chat.id, f"{hlp()}")


def matrix_entry(message):
    # if True:
    conn = sqlite3.connect("mat.sql")
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO mat (matrix) VALUES ("%s")' % (message.text))
    conn.commit()
    cursor.close()
    conn.close()
    markup = all_button()
    bot.send_message(message.chat.id, f"select operation", reply_markup=markup)
    # else:
    #     bot.send_message(message.chat.id, f"{hlp()}")
    #     bot.register_next_step_handler(message=message, callback=matrix_entry)


@bot.callback_query_handler(func=lambda call: True)
def callback_function(call):
    data = bd_get_last()
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
    elif "trace" == call.data:
        bot.send_message(call.message.chat.id, np.trace(matrix))
    elif "transposition" == call.data:
        bot.send_message(call.message.chat.id, f"{matrix.T}")
    elif "inverse" == call.data:
        matrix = np.linalg.inv(matrix)
        lst = [[0] * matrix.shape[0] for _ in range(matrix.shape[1])]
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):

                print(eval(f'f{Decimal(str(matrix[i, j])).as_integer_ratio()}'))
                lst[i][j] = str(eval(f'f{Decimal(str(matrix[i, j])).as_integer_ratio()}'))

            bot.send_message(call.message.chat.id, f"{lst}")
    elif call.data == "All the steps ref":
        bot.send_message(call.message.chat.id, f"{ref(data, long=True)}")
    elif call.data == "All the steps rref":
        bot.send_message(call.message.chat.id, f"{rref(data, long=True)}")
    elif "/clear" == call.data:
        clearing(call.message)
    elif "ERO" == call.data:
        bot.send_message(call.message.chat.id, stroka_ERO)
        bot.register_next_step_handler(message=call.message, callback=opertion_tb)
    elif "last" == call.data:
        bot.send_message(call.message.chat.id, data)


def opertion_tb(message):
    markup = all_button()
    data = bd_get_last()
    bot.send_message(message.chat.id, start_opertions_tb(data, message.text), reply_markup=markup)


@bot.message_handler(commands=['clear'])
def clearing(message):
    i = 0
    while True:
        try:
            bot.delete_message(message.chat.id, message.message_id - i)
            i += 1
        except telebot.apihelper.ApiTelegramException:
            break


bot.infinity_polling()
