import telebot

bot = telebot.TeleBot("1754559930:AAGk8J4IbywhOE-RfH8UVN-fWXl9I-zKJ7E")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello, what would you like to do today?"
                     "Try the /getFood command for food recommendations or /splitBill command")
	bot.send_message(chat_id=update.message.chat_id,
                text=msg, reply_markup=reply_kb_markup)
	

@bot.message_handler(commands=['getFood'])
def get_recommendation(message):
        bot.reply_to(message, "Please select your region or enter postal code for nearby food recommendations.")

@bot.message_handler(commands=['splitBill'])
def split_bill(message):
        bot.reply_to(message, "How many people are splitting the bill?")

bot.polling()
