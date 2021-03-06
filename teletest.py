#!/usr/bin/python
import sys
sys.path.insert(1, "/nfs/2016/o/omartyno/python_pachages")
import telegram
import logging
import time
from threading import Thread
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
								TimedOut, ChatMigrated, NetworkError)

class TimerThread(Thread):
	def __init__(self, seconds, message):
		'''Constructor'''

		Thread.__init__(self)
		self.seconds = seconds
		self.message = message

	def run(self):
		time.sleep(self.seconds)
		bot.send_message(chat_id="31568844", text=self.message)

bot = telegram.Bot(token="448756955:AAHKS3vwRFETKMWtTr-y-ciTFkzbUlxtTk8")

TimersArray = []

print (bot.get_me())

updater = Updater(token="448756955:AAHKS3vwRFETKMWtTr-y-ciTFkzbUlxtTk8")
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
	# time.sleep(10)
	bot.send_message(chat_id=update.message.chat_id, text="Hello")

def ponyal(bot, update, args):
	if (len(args) < 2):
		bot.send_message(chat_id=update.message.chat_id, text="Wrong input. You need to unput time and then text")
		return
	if not args[0].isdigit():
		bot.send_message(chat_id=update.message.chat_id, text="Wrong input. First argument must be time in seconds")
		return
	message = args[1];
	for i in range(2, len(args)):
		message += " " + args[i]
		i += 1
	tmr = TimerThread(int(args[0]), message)
	tmr.start()
	# time.sleep(int(args[0]))
	# bot.send_message(chat_id="31568844", text=message)


start_handler = CommandHandler('start', start)
ponyal_handler = CommandHandler('time', ponyal, pass_args=True)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(ponyal_handler)

def error_callback(bot, update, error):
	print ("Error: ")
	print (error)
	print ("Update: ")
	print (update)
dispatcher.add_error_handler(error_callback)

updater.start_polling()
bot.send_message(chat_id="31568844", text="idle online")
updater.idle()
