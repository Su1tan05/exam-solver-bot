#!/usr/bin/python

from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_filters import StateFilter
from telebot.asyncio_storage import StateMemoryStorage
from hendlers.setup import setup_hendlers
from configs import config
import asyncio

if __name__ == '__main__':
    bot = AsyncTeleBot(config.get_token(),state_storage=StateMemoryStorage())
    bot.add_custom_filter(StateFilter(bot))
    setup_hendlers(bot)
    asyncio.run(bot.polling())