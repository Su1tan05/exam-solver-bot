#!/usr/bin/python

from telebot.async_telebot import AsyncTeleBot

from hendlers.message import MessageHandler
from configs import config

bot = AsyncTeleBot(config.get_token())

def setup_hendles():
    hendler = MessageHandler(bot);
    bot.message_handler(commands=['start'])(hendler.start)
    bot.message_handler(commands=['compliment'])(hendler.send_compliment)
    bot.message_handler(content_types=['text'])(hendler.handle_callback)

import asyncio
setup_hendles()
asyncio.run(bot.polling())