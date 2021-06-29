import telebot
from telebot import types

import logging
import os

import telegram
from telegram import Update, ForceReply, Message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import decimal
import random

TOKEN = 'token'

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
    options = [['Region', 'Postal Code']]
    update.message.reply_text("Please select your region or enter your postal code.", reply_markup = telegram.ReplyKeyboardMarkup(options,
                                                                                                                                  resize_keyboard = True,
                                                                                                                                one_time_keyboard = True))

def get_recommendation(update, context):
    options = [['Region', 'Postal Code (to be updated)']]
    update.message.reply_text("Please select your region or enter your postal code.", reply_markup = telegram.ReplyKeyboardMarkup(options,
                                                                                                                                  resize_keyboard = True,
                                                                                                                                one_time_keyboard = True))
        
def get_postalcd(update, context):
    update.message.reply_text("Enter your postal code below! \U0001F60B")

def food_near_pc(update, context):
    update.message.reply_text('to be updated')
        ##TODO

def get_region(update, context):
    options = [['1. North', '2. Northeast', '3. East'], ['4. West', '5. Central', '/back']]
    update.message.reply_text("Where are you now? \U0001F914", reply_markup = telegram.ReplyKeyboardMarkup(options, resize_keyboard = True))

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
    update.message.reply_text('List of food recommendations located in the North \n\n' + north_food,
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)

def get_northeast(update, context):
    #file = open('northeast.txt')
    northeast_food = random_shuffle('northeast.txt')
    update.message.reply_text('List of food recommendations located in the Northeast \n\n' + northeast_food,
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)

def get_east(update, context):
    #file = open('east.txt')
    east_food = random_shuffle('east.txt')
    update.message.reply_text('List of food recommendations located in the East \n\n' + east_food,
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)

def get_west(update, context):
    #file = open('west.txt')
    west_food = random_shuffle('west.txt')
    update.message.reply_text('List of food recommendations located in the West \n\n' + west_food,
                              parse_mode = 'HTML',
                              disable_web_page_preview = True)

def get_central(update, context):
    #file = open('central.txt')
    central_food = random_shuffle('central.txt')
    update.message.reply_text('List of food recommendations located in Central \n\n' + central_food,
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

