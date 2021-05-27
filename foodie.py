import telebot

bot = telebot.TeleBot("1754559930:AAGk8J4IbywhOE-RfH8UVN-fWXl9I-zKJ7E")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
