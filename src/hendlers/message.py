import typing as t
from telebot.types import Message
from telebot.async_telebot import AsyncTeleBot
from states.user_information import UserInformation
import pathlib

class MessageHandler:
    def __init__(self, bot: AsyncTeleBot):
        self.bot = bot

    async def start_handler(self, message: Message):
        await self.bot.send_message(message.from_user.id, f'Привет 🖐, {message.from_user.first_name}, '
                                           f'<b>\nЯ бот, который поможет тебе успешно сдать экз!</b>', parse_mode='html')
        await self.bot.send_message(message.from_user.id, '<b>И вот что я умею:\n'
                                           '/help — помощь по командам бота\n'
                                           '\n'
                                           '/shpora — получение шпоры в формате pdf\n'
                                           '\n'
                                           '/solver — рашение задачи\n'
                                           '\n'
                                           '/github — ссылка на мой гитхаб репоз с кодом данного проекта 😝</b>', parse_mode='html')

    async def help_handler(self, message: Message):
        pass

    async def send_pdf(self, message: Message):
        pdf_file_path =  pathlib.Path(__package__).parent.absolute().joinpath('resources', 'Shpora.pdf')
        with open(pdf_file_path, 'rb') as pdf:
            await self.bot.send_document(message.chat.id, pdf)

    async def task_init_message(self, message: Message):
        await self.bot.send_message(message.chat.id, \
            "Решение задачи: \n1. Рассчитать мощности для электроприемников")
        await self.bot.send_message(message.chat.id, "Введите значение для ЭП1 (слитно с разделитем ';')\n\
            Пример ввода: 24.0;4;0.82;0.82;6.5")
        await self.bot.set_state(message.from_user.id, UserInformation.first_source_params, message.chat.id)
    
    async def set_first_source_params(self, message: Message):
        async with self.bot.retrieve_data(message.from_user.id) as data:
            data['name'] = message.text
        return await self.bot.send_message(message.chat.id, f"Вы ввели: {data['name']}")

    async def send_github_link(self, message: Message):
        await self.bot.send_message(message.chat.id, "https://github.com/Su1tan05/exam_bot")