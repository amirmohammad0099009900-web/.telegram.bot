import telebot

# اینجا توکن رو وارد کن
TOKEN = "8324781457:AAFtBm_pedMF-o6mtzbce04zf6Hp7zv7yYM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! ربات شما فعال شد 😊")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("ربات در حال اجراست...")
bot.infinity_polling()
