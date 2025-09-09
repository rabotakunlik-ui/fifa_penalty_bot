import telebot
from config import BOT_TOKEN, CHANNEL_ID
from utils import generate_coupon, check_confidence

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! FIFA Penalty kupon botiga xush kelibsiz!")

# Har 5 daqiqada kupon yuborish (simulyatsiya)
import threading, time

def send_coupons():
    while True:
        coupon, confidence = generate_coupon()
        if confidence >= 75:
            bot.send_message(CHANNEL_ID, f"Yangi kupon:\n{coupon}\nIshonch: {confidence}%")
        time.sleep(300)  # 5 daqiqa

threading.Thread(target=send_coupons).start()

bot.infinity_polling()
