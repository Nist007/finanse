import telebot
from telebot import types
import base64


import base64
import telebot


with open('api_key.txt', 'r') as file:
    apikey = file.read().strip()
bot = telebot.TeleBot(apikey)






@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Пополнение")
    button2 = types.KeyboardButton("Расходы")
    button3 = types.KeyboardButton("Оsтаток")
    markup.add(button1, button2, button3)

    bot.send_message(message.chat.id, "Введите команду", reply_markup=markup)


def input_message(message):
    return True


def popolnenie(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(func=input_message)
def handle_message(message):
    if message.text == "Пополнение":
        s = bot.send_message(message.chat.id, "Введите сумму пополнения :")
        bot.register_next_step_handler(s, popolnenie)


bot.polling()
