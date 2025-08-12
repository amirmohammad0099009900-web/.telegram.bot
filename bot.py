import telebot

# توکن ربات خودت رو اینجا بذار
TOKEN = "8324781457:AAFtBm_pedMF-o6mtzbce04zf6Hp7zv7yYM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "سلام، ربات روشنه ✅")

print("ربات روشن شد و منتظر پیام است...")
bot.polling()
