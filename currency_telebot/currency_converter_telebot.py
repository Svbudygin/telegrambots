from datetime import date
import sqlite3
import telebot
from telebot import types
from currency_converter import CurrencyConverter

bot = telebot.TeleBot("-")
currency = CurrencyConverter()

sm = 0
num = 0


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect("curr.sql")
    cursor = conn.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS currency_t (id int auto_increment primary key, num varchar(50), summ varchar(50))')
    conn.commit()
    cursor.close()
    conn.close()
    bot.send_message(message.chat.id, f'@{message.from_user.username}! Enter sum:')
    bot.register_next_step_handler(message=message, callback=sum_function)


def sum_function(message):
    try:
        global sm
        global num
        num = "amount: "
        sm = int(message.text)
        if sm <= 0:
            raise ValueError
        conn = sqlite3.connect("curr.sql")
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO currency_t (num, summ) VALUES ("%s", "%s")' % (num, message.text))
        conn.commit()
        cursor.close()
        conn.close()

    except ValueError:
        bot.send_message(message.chat.id, f'{message.from_user.first_name}! Enter sum correctly:')
        bot.register_next_step_handler(message=message, callback=sum_function)
        return None

    markup = types.InlineKeyboardMarkup(row_width=3)
    btm1 = types.InlineKeyboardButton("USD -> RUB", callback_data="USD RUB")
    btm2 = types.InlineKeyboardButton("EUR -> RUB", callback_data="EUR RUB")
    btm3 = types.InlineKeyboardButton("GBP -> RUB", callback_data="GBP RUB")

    btm5 = types.InlineKeyboardButton("RUB -> USD", callback_data="RUB USD")
    btm6 = types.InlineKeyboardButton("RUB -> EUR", callback_data="RUB EUR")
    btm7 = types.InlineKeyboardButton("RUB -> GBP", callback_data="RUB GBP")

    btm9 = types.InlineKeyboardButton("Others", callback_data="Others")
    markup.add(btm1, btm2, btm3, btm5, btm6, btm7, btm9)
    markup.add(types.InlineKeyboardButton("all_sum", callback_data="all_sum"))
    bot.send_message(message.chat.id, "Select currency:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_function(call):
    if call.data == "Others":
        bot.send_message(call.message.chat.id, "Enter currency (ex. EUR USD):\n(to see all currency /help)")
        bot.register_next_step_handler(message=call.message, callback=enter_cur)
    elif call.data == "all_sum":
        conn = sqlite3.connect("curr.sql")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM currency_t")
        data = cursor.fetchall()
        data = (f"({i[1]}) +{i[2]}" for i in data)
        cursor.close()
        conn.close()
        bot.send_message(call.message.chat.id, "\n".join(data))
    else:
        currencies = call.data.upper().split()
        if "RUB" in currencies:
            new_sm = round(currency.convert(sm, *currencies, date=date(2022, 3, 1)), 2)
        else:
            new_sm = round(currency.convert(sm, *currencies), 2)
        bot.send_message(call.message.chat.id, f"{round(sm, 2)} ({currencies[0]}) = {new_sm} ({currencies[1]})")
        # bot.register_next_step_handler(call.message, callback=sum_function)


def enter_cur(arg):
    if "/" in arg.text:
        return None
    try:
        currencies = arg.text.upper().split()
        if "RUB" in currencies:
            new_sm = round(currency.convert(sm, *currencies, date=date(2022, 3, 1)), 2)
        else:
            new_sm = round(currency.convert(sm, *currencies), 2)
        bot.send_message(arg.chat.id, f"{round(sm, 2)} ({currencies[0]}) = {new_sm} ({currencies[1]})")
        bot.register_next_step_handler(message=arg, callback=enter_cur)
    except:
        bot.send_message(arg.chat.id, f"Enter currency correctly (ex. EUR USD):\n(to see all currency /help)")
        bot.register_next_step_handler(message=arg, callback=enter_cur)


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, f'{currency.currencies}')


bot.polling(none_stop=True)
