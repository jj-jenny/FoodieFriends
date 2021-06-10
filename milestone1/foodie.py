import telebot
import telegram
from telebot import types


bot = telebot.TeleBot("insert token here")
user = bot.get_me()

@bot.message_handler(commands=['start'])
def send_welcome(message):
        chat_id = message.chat.id
       ## bot.reply_to(message, "Hello, what would you like to do today?"
       ##              " Try the /getFood command for food recommendations or /splitBill command")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        itembtna = types.KeyboardButton('Food recommendation \U0001F924')
        itembtnv = types.KeyboardButton('Split my bills \U0001F4B8')
        markup.row(itembtna, itembtnv)
        bot.send_message(chat_id, "Hello! What would you like to do today?", reply_markup = markup)
	

@bot.message_handler(func=lambda message: message.text == 'Food recommendation \U0001F924')
@bot.message_handler(commands=['back'])
def get_recommendation(message):
        chat_id = message.chat.id
        options = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        itembtna = types.KeyboardButton('Region')
        itembtnv = types.KeyboardButton('Postal Code')
        options.row(itembtna, itembtnv)
        bot.send_message(chat_id, "Please select your region or enter your postal code.", reply_markup = options)

##@bot.message_handler(func=lambda message: message.text == 'Split my bills \U0001F4B8')
##def split_bills(message):
        ##TODO
        
@bot.message_handler(func=lambda message: message.text == 'Postal Code')
def get_postalcd(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Enter your postal code below! \U0001F60B")

@bot.message_handler(func=lambda message: message.text.isdigit() and len(message.text) == 6)
def food_near_pc(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Here are some yummy food choices near ' + message.text + '! \U0001F609'
                         '\n\n<b>928 Yishun Laksa</b>'
                         '\n928 Yishun Central 1, #01-155, Singapore 760928'
                         '\n\nto be updated', parse_mode = 'HTML')
        ##TODO


@bot.message_handler(func=lambda message: message.text == 'Region')
def get_region(message):
        chat_id = message.chat.id
        markup_food = types.ReplyKeyboardMarkup(resize_keyboard=True)
        north = types.KeyboardButton('North')
        south = types.KeyboardButton('South')
        east = types.KeyboardButton('East')
        west = types.KeyboardButton('West')
        central = types.KeyboardButton('Central')
        back = types.KeyboardButton('/back')
        markup_food.row(north, south, east)
        markup_food.row(west, central, back)
        bot.send_message(chat_id, "Where are you now? \U0001F914", reply_markup = markup_food)


@bot.message_handler(func=lambda message: message.text == 'North')
def get_north(message):
        ## TODO
        chat_id = message.chat.id
        file = open('north.txt')
        north_food = file.read()
        bot.send_message(chat_id, 'Here are some yummy food choices in the North! \U0001F609'
                         + north_food +
                         '\n\nto be updated', parse_mode = 'HTML')

@bot.message_handler(func=lambda message: message.text == 'South')
def get_south(message):
        ## TODO
        chat_id = message.chat.id
        file = open('south.txt')
        south_food = file.read()
        bot.send_message(chat_id, 'Here are some yummy food choices in the South! \U0001F609'
                         + south_food +
                         '\n\nto be updated', parse_mode = 'HTML')

@bot.message_handler(func=lambda message: message.text == 'East')
def get_east(message):
        ## TODO
        chat_id = message.chat.id
        file = open('east.txt')
        east_food = file.read()
        bot.send_message(chat_id, 'Here are some yummy food choices in the East! \U0001F609'
                         + east_food +
                         '\n\nto be updated', parse_mode = 'HTML')

@bot.message_handler(func=lambda message: message.text == 'West')
def get_west(message):
        ## TODO
        chat_id = message.chat.id
        file = open('west.txt')
        west_food = file.read()
        bot.send_message(chat_id, 'Here are some yummy food choices in the West! \U0001F609'
                         + west_food +
                         '\n\nto be updated', parse_mode = 'HTML')

@bot.message_handler(func=lambda message: message.text == 'Central')
def get_central(message):
        ## TODO
        chat_id = message.chat.id
        file = open('central.txt')
        central_food = file.read()
        bot.send_message(chat_id, 'Here are some yummy food choices in Central! \U0001F609'
                         + central_food +
                         '\n\nto be updated', parse_mode = 'HTML')
        

@bot.message_handler(commands=['splitBill'])
def split_bill(message):
        bot.reply_to(message, "How many people are splitting the bill?")

bot.polling()
