TELEGRAM_BOT_TOKEN = '7749696009:AAGSabfeBF0amubhey7gOIDOjaHpvkGeNKs'
TELEGRAM_CHAT_ID = '1374840231'
from telegram import Bot

import telebot
from telebot import types
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я ваш бот для заказа букетов. Чем могу помочь?')

@bot.message_handler(commands=['check'])
def check_bot(message):
    bot.reply_to(message, 'Бот работает!')

def send_order_to_telegram(order):
    message = f'Новый заказ!\nБукет: {order.flower.name}\nЦена: {order.flower.price} руб.'
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("Сообщение успешно отправлено")
    except Exception as e:
        print(f"Ошибка при отправке: {e}")


def send_order_to_telegram(order):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    message = f'Новый заказ!\nБукет: {order.flower.name}\nЦена: {order.flower.price} руб.'
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("Сообщение успешно отправлено")
    except Exception as e:
        print(f"Ошибка при отправке: {e}")

if __name__ == '__main__':
    bot.polling()