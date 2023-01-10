import json
import typing as t
from telebot.types import Message, KeyboardButton, ReplyKeyboardMarkup
from telebot.async_telebot import AsyncTeleBot
import pathlib

class MessageHandler:
    def __init__(self, bot: AsyncTeleBot):
        self.bot = bot

    async def start(self, message: Message):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembtn1 = KeyboardButton('Шпора')
        itembtn2 = KeyboardButton('Задача')
        itembtn3 = KeyboardButton('Help')
        itembtn4 = KeyboardButton('Source code')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
        await self.bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)

    async def send_compliment(self, message: Message):
        complement = "self.repo.get_random_complement()"
        return await self.bot.send_message(message.chat.id, text=complement)

    # handle all keyboard buttons callbacks
    async def handle_callback(self, message: Message):
        if message.text == 'Шпора':
            await self.send_pdf(message)
        elif message.text == 'Задача':
            await self.bot.send_message(message.chat.id, "Шпора")
        elif message.text == 'Help':
            await self.bot.send_message(message.chat.id, "Hellop")
        elif message.text == 'Source code':
            await self.bot.send_message(message.chat.id, "гитхаб")

    # async send pdf file
    async def send_pdf(self, message: Message):
        pdf_file_path =  pathlib.Path(__package__).parent.absolute().joinpath('resources', 'Shpora.pdf')
        with open(pdf_file_path, 'rb') as pdf:
            await self.bot.send_document(message.chat.id, pdf)