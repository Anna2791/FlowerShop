TELEGRAM_BOT_TOKEN = '7749696009:AAGSabfeBF0amubhey7gOIDOjaHpvkGeNKs'
TELEGRAM_CHAT_ID = '1374840231'
from telegram import Bot

import telebot
from telebot import types
def send_order_to_telegram(order):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    message = f'Новый заказ!\nБукет: {order.flower.name}\nЦена: {order.flower.price} руб.'
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("Сообщение успешно отправлено")
    except Exception as e:
        print(f"Ошибка при отправке: {e}")

