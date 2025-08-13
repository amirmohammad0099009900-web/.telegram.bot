import os
import telebot

# توکن ربات رو اینجا بذار (فعلاً). بهتره بعداً توکن جدید بسازی و توی محیط میزبانی به صورت ENV ست کنی.
TOKEN = os.getenv("BOT_TOKEN") or "PASTE-YOUR-TOKEN-HERE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! ربات روشنه ✅")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # هرچی بفرستی همونو برمی‌گردونه
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling(skip_pending=True)
