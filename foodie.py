import telebot

bot = telebot.TeleBot("1754559930:AAGk8J4IbywhOE-RfH8UVN-fWXl9I-zKJ7E")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello, what would you like to eat today?")
	
@bot.message_handler(func=lambda message: True)
def breathe_all(message):
	bot.reply_to(message, "I love Food!")

bot.polling()
