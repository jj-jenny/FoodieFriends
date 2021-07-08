import telebot
from telebot import types

import logging
import os

import telegram
from telegram import Update, ForceReply, Message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import decimal
import random

TOKEN = ''

bot = telebot.TeleBot(TOKEN)
user = bot.get_me()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', '8443'))

# Define command handlers
def start(update, context):
    #select options
    reply_keyboard = [['Food recommendation \U0001F924', 'Split my bills \U0001F4B8']]
    update.message.reply_text("Hello, what would you like to do today?", reply_markup = telegram.ReplyKeyboardMarkup(reply_keyboard,
                                                                                                                     resize_keyboard = True,
                                                                                                                     one_time_keyboard = True))

def back(update, context):
    options = [['Location', 'Cuisine']]
    update.message.reply_text("Looking for something to eat? Use the buttons below to filter by location or cuisine!", reply_markup = telegram.ReplyKeyboardMarkup(options,
                                                                                                                                  resize_keyboard = True,
                                                                                                                                  one_time_keyboard = True))

def get_recommendation(update, context):
    options = [['Location', 'Cuisine']]
    update.message.reply_text("Looking for something to eat? Use the buttons below to filter by location or cuisine!", reply_markup = telegram.ReplyKeyboardMarkup(options,
                                                                                                                                  resize_keyboard = True,
                                                                                                                                  one_time_keyboard = True))
  
def get_location(update, context):
    options = [['1. North', '2. Northeast', '3. East'], ['4. West', '5. Central', '/back']]
    update.message.reply_text("Please select your region or enter your postal code below! \U0001F60B \n\nEg: /postalcode 123456", reply_markup = telegram.ReplyKeyboardMarkup(options, resize_keyboard = True))

    #options = [['Region', 'Postal Code (to be updated)']]
    #update.message.reply_text("Please select your region or enter your postal code!", reply_markup = telegram.ReplyKeyboardMarkup(options,
                                                                                                                                  #resize_keyboard = True,
                                                                                                                                #one_time_keyboard = True))       
def get_postalcd(update, context):
    update.message.reply_text("Enter your postal code below! \U0001F60B \nEg: /postalcode 123456")

def postalcode(update, context):
    userinput = update.message.text.split(" ")
    pc = userinput[1]
    places = open('everything.txt').read()
    para = places.split('\n\n')
    random.shuffle(para)
    output = []
    for i in para:
        before, key, after = i.partition('Singapore')
        if after[1:3] == pc[0:2] :
            output.append(i + "\n\n")

    if len(output) > 5:
        final = output[0:5]
    else:
        final = output

    str1 = ''
    
    result = ''
    if len(pc) != 6:
      result = "Invalid postal code entered! Please try again."
    elif len(final) == 0:
      result = "No recommendations at the moment! We will work to expand our database."
    else:
      result = "Here are some food places near you! \U0001F929 \n\n" + str1.join(final)
        
    update.message.reply_text(result, parse_mode = 'HTML', disable_web_page_preview = True)
        

def food_near_pc(update, context):
    update.message.reply_text('to be updated')
        ##TODO

def get_region(update, context):
    options = [['1. North', '2. Northeast', '3. East'], ['4. West', '5. Central', '/back']]
    update.message.reply_text("Where are you now? \U0001F914", reply_markup = telegram.ReplyKeyboardMarkup(options, resize_keyboard = True))

def get_cuisine(update, context):
    options = [['Chinese', 'Malay', 'Indian'], ['Western', 'Thai', 'Others']]
    update.message.reply_text("Select what you're craving for!", reply_markup = telegram.ReplyKeyboardMarkup(options, 
                                                                                                             resize_keyboard = True))
    
def random_shuffle(fname):
    lines = open(fname).read()
    paragraphs = lines.split('\n\n')
    random.shuffle(paragraphs)
    i = 0
    output = ""
    while i < 3:
        output = output + paragraphs[i] + "\n\n"
        i = i + 1
    return output

def get_north(update, context):
    #file = open('north.txt')
    north_food = random_shuffle('north.txt')
    update.message.reply_text('List of food recommendations in the North! \n\n' + north_food + "Press again for more!",
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)

def get_northeast(update, context):
    #file = open('northeast.txt')
    northeast_food = random_shuffle('northeast.txt')
    update.message.reply_text('List of food recommendations in the Northeast! \n\n' + northeast_food + "Press again for more!",
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)

def get_east(update, context):
    #file = open('east.txt')
    east_food = random_shuffle('east.txt')
    update.message.reply_text('List of food recommendations in the East! \n\n' + east_food + "Press again for more!",
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)

def get_west(update, context):
    #file = open('west.txt')
    west_food = random_shuffle('west.txt')
    update.message.reply_text('List of food recommendations in the West! \n\n' + west_food + "Press again for more!",
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)

def get_central(update, context):
    #file = open('central.txt')
    central_food = random_shuffle('central.txt')
    update.message.reply_text('List of food recommendations in Central! \n\n' + central_food + "Press again for more!",
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)
    
def get_chinese(update, context):
    chinese_food = random_shuffle('chinese.txt')
    update.message.reply_text('Here are some Chinese food recommendations! \n\n' + chinese_food,
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)
    
def get_malay(update, context):
    malay_food = random_shuffle('malay.txt')
    update.message.reply_text('Here are some Malay food recommendations! \n\n' + malay_food,
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)
    
def get_indian(update, context):
    indian_food = random_shuffle('indian.txt')
    update.message.reply_text('Here are some Indian food recommendations! \n\n' + indian_food,
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)
    
def get_western(update, context):
    western_food = random_shuffle('western.txt')
    update.message.reply_text('Here are some Western food recommendations! \n\n' + western_food,
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)
def get_thai(update, context):
    thai_food = random_shuffle('thai.txt')
    update.message.reply_text('Here are some Thai food recommendations! \n\n' + thai_food,
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)
    
def get_others(update, context):
    other_food = random_shuffle('others.txt')
    update.message.reply_text('Here are some miscellaneous food recommendations! \n\n' + other_food,
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)

def split_bills(update, context):
    update.message.reply_text("Please enter each person and their amount paid in the following format: \n /calculate Name Amount Name Amount")       

# Calculate Bill
def calculate(update: Update, _: CallbackContext) -> None:
    """Splits the bill"""
    all_words = update.message.text.split(" ")
    #all_words = ["/calculate", "Name", "Amt", "Name"] //in strings

    #converting to list of integers
    terms = list(all_words[1:])
    names = []
    amounts = []
    i = 0
    while i < len(terms):
        if i % 2 == 0:
            names.append(terms[i])
            i = i + 1
        else:
            amounts.append(decimal.Decimal(terms[i]))
            i = i + 1

    # total amount to pay
    total = sum(amounts)

    # amount per person
    decimal.getcontext().prec = 3
    ave_amt = decimal.Decimal(total / len(names))

    # amount to pay/receive
    diffs = [ave_amt - amnt for amnt in amounts]
    
    to_pay = ""
    index = 0
    while index < len(names):
        if diffs[index] > 0:
            to_pay = to_pay + ("\n" + names[index] + " should pay $" + str(diffs[index]))
            index += 1
        elif diffs[index] == 0:
            to_pay = to_pay + ("\n" + names[index] + " does not have to pay")
            index += 1
        else:
            to_pay = to_pay + ("\n" + names[index] + " should receive $" + str(diffs[index]*(-1)))
            index += 1
            
    #return response
    update.message.reply_text(f"{to_pay}")

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("back", back))
    dispatcher.add_handler(CommandHandler("calculate", calculate))
    dispatcher.add_handler(CommandHandler("postalcode", postalcode))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.regex('Food recommendation \U0001F924'), get_recommendation))
    dispatcher.add_handler(MessageHandler(Filters.regex('Split my bills \U0001F4B8'), split_bills))
    dispatcher.add_handler(MessageHandler(Filters.regex('Postal Code'), get_postalcd))
    dispatcher.add_handler(MessageHandler(Filters.regex('Region'), get_region))
    dispatcher.add_handler(MessageHandler(Filters.regex('1. North'), get_north))
    dispatcher.add_handler(MessageHandler(Filters.regex('2. Northeast'), get_northeast))
    dispatcher.add_handler(MessageHandler(Filters.regex('3. East'), get_east))
    dispatcher.add_handler(MessageHandler(Filters.regex('4. West'), get_west))
    dispatcher.add_handler(MessageHandler(Filters.regex('5. Central'), get_central))
    dispatcher.add_handler(MessageHandler(Filters.regex('Location'), get_location))
    dispatcher.add_handler(MessageHandler(Filters.regex('Cuisine'), get_cuisine))
    dispatcher.add_handler(MessageHandler(Filters.regex('Chinese'), get_chinese))
    dispatcher.add_handler(MessageHandler(Filters.regex('Malay'), get_malay))
    dispatcher.add_handler(MessageHandler(Filters.regex('Indian'), get_indian))
    dispatcher.add_handler(MessageHandler(Filters.regex('Western'), get_western))
    dispatcher.add_handler(MessageHandler(Filters.regex('Thai'), get_thai))
    dispatcher.add_handler(MessageHandler(Filters.regex('Others'), get_others))
                    
    # Start the Bot
    updater.start_polling()
##    updater.start_webhook(listen="0.0.0.0",
##                      port=int(PORT),
##                      url_path=TOKEN,
##                      webhook_url='https://foodiefriendsbot.herokuapp.com/' + TOKEN)
##    updater.bot.set_webhook(url=settings.WEBHOOK_URL)
##    updater.bot.set_webhook("foodiefriendsbot" + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()

