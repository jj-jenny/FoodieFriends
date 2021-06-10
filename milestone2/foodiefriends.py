import telebot
from telebot import types

import logging
import os

import telegram
from telegram import Update, ForceReply, Message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "insert token here"

bot = telebot.TeleBot("insert token here")
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
      
def get_recommendation(update, context):
    options = [['Region', 'Postal Code']]
    update.message.reply_text("Please select your region or enter your postal code.", reply_markup = telegram.ReplyKeyboardMarkup(options,
                                                                                                                                  resize_keyboard = True,
                                                                                                                                  one_time_keyboard = True))


def split_bills(update, context):
    update.message.reply_text("Please enter each person and their amount paid in the following format: \nName Amount Name Amount")
        
        ##TODO
        
def get_postalcd(update, context):
    update.message.reply_text("Enter your postal code below! \U0001F60B")

@bot.message_handler(func=lambda message: message.text.isdigit() and len(message.text) == 6)
def food_near_pc(update, context):
    update.message.reply_text(chat_id, 'Here are some yummy food choices near ' + message.text + '! \U0001F609'
                         '\n\n<b>928 Yishun Laksa</b>'
                         '\n928 Yishun Central 1, #01-155, Singapore 760928'
                         '\n\nto be updated', parse_mode = 'HTML')
        ##TODO

def get_region(update, context):
    options = [['North', 'South', 'East'], ['West', 'Central', '/back']]
    update.message.reply_text("Where are you now? \U0001F914", reply_markup = telegram.ReplyKeyboardMarkup(options, resize_keyboard = True))
        


@bot.message_handler(func=lambda message: message.text == 'North')
def get_north(update, context):
        ## TODO
   update.message.reply_text(chat_id, 'Here are some yummy food choices nearby! \U0001F609'
                         '\n\n<b>928 Yishun Laksa</b>'
                         '\n928 Yishun Central 1, #01-155, Singapore 760928'
                         '\n\nto be updated', parse_mode = 'HTML')

@bot.message_handler(func=lambda message: message.text == 'South')
def get_south(update, context):
        ## TODO
    update.message.reply_text(chat_id, 'List of food recommendations located in the South (to be updated)')

@bot.message_handler(func=lambda message: message.text == 'East')
def get_east(update, context):
        ## TODO
    update.message.reply_text(chat_id, 'List of food recommendations located in the East (to be updated)')

@bot.message_handler(func=lambda message: message.text == 'West')
def get_west(update, context):
        ## TODO
    update.message.reply_text(chat_id, 'List of food recommendations located in the West (to be updated)')
        

@bot.message_handler(commands=['splitBill'])
def split_bill(update, context):
    update.message.reply_text("How many people are splitting the bill?")

#bot.polling()

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("back", start))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.regex('Food recommendation \U0001F924'), get_recommendation))
    dispatcher.add_handler(MessageHandler(Filters.regex('Split my bills \U0001F4B8'), split_bills))
    dispatcher.add_handler(MessageHandler(Filters.regex('Postal Code'), get_postalcd))
    dispatcher.add_handler(MessageHandler(Filters.regex('Region'), get_region))
                    
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
