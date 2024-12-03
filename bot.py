import telebot
from logic import *
from config import TELEGRAM_TOKEN
from telebot import types
import requests
import random

bot = telebot.TeleBot(TELEGRAM_TOKEN)

greeting = random.choice(greetings)





#ОСНОВНОЕ МЕНЮ
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, greeting)
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    main_button1 = types.KeyboardButton('каталог')
    main_button2 = types.KeyboardButton('магазин')
    main_button3 = types.KeyboardButton('наш канал')
    main_button4 = types.KeyboardButton('другое')
    keyboard.add(main_button1, main_button2, main_button3, main_button4)
    bot.reply_to(message, '1', reply_markup=keyboard)



@bot.message_handler(func= lambda message: True)
def handle_message(message):
    if message.text == 'Каталог':
        pass
    elif message.text == 'Магазин':
        text = "Новости и выгодные предложения в [нашем канале](https://mrmattress.ru)"
        bot.send_message(message.chat.id, text, parse_mode='Markdown')
    elif message.text == 'Наш канал':
        text = "Новости и выгодные предложения в [нашем канале](https://t.me/%2B7vMdFbgqm2Q0YzE6)"
        bot.send_message(message.chat.id, text, parse_mode='Markdown')
    elif message.text == 'Прочее':
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            k4_button1 = types.KeyboardButton('Наши адреса')
            k4_button2 = types.KeyboardButton('Связь с менеджером')
            k4_button3 = types.KeyboardButton('Персональный')
            k4_button4 = types.KeyboardButton('Назад')
            keyboard.add(k4_button1, k4_button2, k4_button3, k4_button4)
            bot.reply_to(message, '1', reply_markup=keyboard)
    elif message.text == 'personal':
        bot.send_message(message.chat.id, 'Вам нужен индивидуальный матрас, идеально соответствующий вашим требованиям? Тогда свяжитесь с нашим менеджером\nПо телефону: 8(800)700-49-44\nВ whatsapp:\nВ viber:')
    elif message.text == 'manager':
        text = 'Остались вопросы?\nСвяжитесь с нашим менеджером по телефону:\nВ whatsapp:\nВ viber:'
        bot.send_message(message.chat.id, text, parse_mode = 'Markdown')
    elif message.text == 'address discont':
        text = 'Хотите протестировать нашу продукцию лично? Приходите в наши шоу-румы и магазины:\n<b>Центральный шоу-рум Mr.Mattress г. Москва:</b>\nАдрес: г. Москва, Подколокольный переулок д. 6 стр. 3(вход в арку во двор)\n<b>Центральный шоу-рум Mr.Mattress г. Санкт-Петербург:</b>\nАдрес: г. Санкт-Петербург, ул. Глинки д.1 (наб. Крюкова канала, 4)\n<b>Производство в городе Шатура:</b>\nМосковская область, г. Шатура, ул. Большевик, д. 168'
        bot.send_message(message.chat.id, text, parse_mode = 'HTML')
    elif message.text == 'back':
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        main_button1 = types.KeyboardButton('каталог')
        main_button2 = types.KeyboardButton('магазин')
        main_button3 = types.KeyboardButton('наш канал')
        main_button4 = types.KeyboardButton('другое')
        keyboard.add(main_button1, main_button2, main_button3, main_button4)
        bot.reply_to(message, '1', reply_markup=keyboard)
        


        





   


















































































if __name__ == '__main__':
    bot.polling(none_stop=True)
