import telebot
from telebot import types
import requests
import json
import webbrowser


API_code = "-"
bot = telebot.TeleBot("-")
# http://api.openweathermap.org/data/2.5/find?q=Moscow&type=like&APPID=18c22d958fa3fb4a185e57d7fb324831&units=metric
@bot.message_handler(content_types=['photo'])
def message1(message):
    pass
    bot.send_message(message.chat.id, message)
def get_weather(city):
    d = requests.get(
        f"http://api.openweathermap.org/data/2.5/find?q={city}&type=like&APPID={API_code}&units=metric")
    if d.status_code == 200:
        d = json.loads(d.content)
        if d["list"]:
            type_of_wr = d["list"][0]["weather"][0]["main"]
            degrees = d["list"][0]["main"]["temp"]
            extra = d["list"][0]["weather"][0]["description"]
            try:
                file = open(f'weather_photo/{type_of_wr.lower()}.png', 'rb')
            except FileNotFoundError:
                file = None

            return (
                f"<em>In <b>{city[0].upper()}{city[1:]}</b> it is <b>{type_of_wr.lower()}</b> ({extra}) and <b> {degrees}</b>°C</em>",
                file)
        return (None, None)


@bot.message_handler(commands=['start'])
def start_message(message):
    last_namee = " " + message.from_user.last_name if message.from_user.last_name else ""
    bot.reply_to(message,
                 f'Hello, {message.from_user.first_name}{last_namee}!\n<u>Please write the city where you would like to know the weather:</u>',
                 parse_mode="html")


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
    markup.add(types.KeyboardButton("Moscow"))
    btm1 = types.KeyboardButton("Petersburg")
    btm2 = types.KeyboardButton("Paris")
    btm3 = types.KeyboardButton("Berlin")
    btm4 = types.KeyboardButton("London")
    btm5 = types.KeyboardButton("Amsterdam")
    btm6 = types.KeyboardButton("Rome")
    btm7 = types.KeyboardButton("Madrid")
    btm8 = types.KeyboardButton("Dusseldorf")
    btm9 = types.KeyboardButton("Dubai")
    markup.add(btm1, btm2, btm3, btm4, btm5, btm6, btm7, btm8, btm9)

    bot.send_message(message.chat.id, f"{message.from_user.first_name},\nPlease, choose the city", reply_markup=markup)


@bot.message_handler(commands=['help'])
def message_reply2(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("YouTube help",
                                          url="https://www.youtube.com/watch?v=-l_CYgBj4IE&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=2"))
    bot.send_message(message.chat.id,
                     "Possible operations <b>/button</b> or <b>/weather</b> or write the city where you would like to know the weather",
                     parse_mode="html", reply_markup=markup)


@bot.message_handler(commands=['weather'])
def weather_smt(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🌦Moscow", callback_data="Moscow"))
    btm1 = types.InlineKeyboardButton("🌦Petersburg", callback_data="Petersburg")
    btm2 = types.InlineKeyboardButton("🌦Paris", callback_data="Paris")
    markup.row(btm1, btm2)
    btm3 = types.InlineKeyboardButton("🌦Berlin", callback_data="Berlin")
    btm4 = types.InlineKeyboardButton("🌦London", callback_data="London")
    markup.row(btm3, btm4)
    btm5 = types.InlineKeyboardButton("🌦Amsterdam", callback_data="Amsterdam")
    btm6 = types.InlineKeyboardButton("🌦Rome", callback_data="Rome")
    btm7 = types.InlineKeyboardButton("🌦Madrid", callback_data="Madrid")
    markup.row(btm5, btm6, btm7)
    btm8 = types.InlineKeyboardButton("🌦Dusseldorf", callback_data="Dusseldorf")
    btm9 = types.InlineKeyboardButton("🌦Dubai", callback_data="Dubai")
    btm10 = types.InlineKeyboardButton("🌦Prague", callback_data="Prague")
    markup.row(btm8, btm9, btm10)

    bot.send_message(message.chat.id, "Choose the city:", reply_markup=markup)


# @bot.message_handler(commands=['clear'])
# def clearing(message):
#     i = 0
#     while True:
#         try:
#             bot.delete_message(message.chat.id, message.message_id - i)
#             i += 1
#         except telebot.apihelper.ApiTelegramException:
#             break


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    text = callback.data.lower()
    ans, file = get_weather(text)
    bot.send_message(callback.message.chat.id, ans, parse_mode="html")
    if file:
        bot.send_photo(callback.message.chat.id, file)


@bot.message_handler(content_types='text')
def message_reply1(message):
    text = message.text.lower()
    ans, file = get_weather(text)
    if ans:
        bot.send_message(message.chat.id, ans, parse_mode="html")
    if file:
        bot.send_photo(message.chat.id, file)





bot.infinity_polling()
