import typing as t
from telebot.types import Message
from telebot.async_telebot import AsyncTeleBot
from states.user_information import UserInformation
from utils.string_parser import parse_string_to_list
from solver.solve_exam_task import solve_first, solve_second
import pathlib

class MessageHandler:

    def __init__(self, bot: AsyncTeleBot):
        self.bot = bot

    async def start_handler(self, message: Message):
        await self.bot.send_message(message.from_user.id, f'Привет 🖐, {message.from_user.first_name}, '
                                           f'<b>\nЯ бот, который поможет тебе успешно сдать экз!</b>', parse_mode='html')
        await self.bot.send_message(message.from_user.id, self.help_message, parse_mode='html')

    async def help_handler(self, message: Message):
        await self.bot.send_message(message.from_user.id, self.help_message, parse_mode='html')

    async def send_pdf(self, message: Message):
        pdf_file_path =  pathlib.Path(__package__).parent.absolute().joinpath('resources', 'Shpora.pdf')
        with open(pdf_file_path, 'rb') as pdf:
            await self.bot.send_document(message.chat.id, pdf)

    async def task_init_message(self, message: Message):
        await self.bot.send_message(message.chat.id, \
            "Задача: \nРассчитать мощности для электроприемников")
        await self.bot.send_message(message.chat.id, "Введите значение для ЭП1 (слитно с разделитем ';')\nПример ввода: 24.0;4;0.82;0.82")
        await self.bot.set_state(message.from_user.id, UserInformation.first_source_params, message.chat.id)

    async def set_first_source_params(self, message: Message):
        await self.bot.set_state(message.from_user.id, UserInformation.second_source_params, message.chat.id)
       
        async with self.bot.retrieve_data(message.from_user.id) as data:
            data['first_property'] = message.text

        params = parse_string_to_list(data['first_property'])
        await self.bot.send_message(message.chat.id, "<b>ЭП1:\n"\
                                                        f"P_номi: {params[0]}\n"\
                                                        f"n_i: {params[1]}\n"\
                                                        f"K_i: {params[2]} \n"\
                                                        f"cosf: {params[3]}</b>", parse_mode='html')
        await self.bot.send_message(message.chat.id, "Введите значение для ЭП2 (слитно с разделитем ';')\nПример ввода: 24.0;4;0.82;0.82")
 
    async def set_second_source_params(self, message: Message):  

        await self.bot.set_state(message.from_user.id, UserInformation.solver, message.chat.id)
      
        async with self.bot.retrieve_data(message.from_user.id) as data:
            data['second_property'] = message.text

        params = parse_string_to_list(data['second_property'])
        await self.bot.send_message(message.chat.id, "<b>ЭП2:\n"\
                                                        f"P_номi: {params[0]}\n"\
                                                        f"n_i: {params[1]}\n"\
                                                        f"K_i: {params[2]} \n"\
                                                        f"cosf: {params[3]}</b>", parse_mode='html')

        await self.bot.send_message(message.chat.id, "Проверьте введенные данные: \nЕсли все ОК введите <b>старт</b>", parse_mode='html')


    async def solve_task(self, message: Message):

        async with self.bot.retrieve_data(message.from_user.id) as data:
            first_params = parse_string_to_list(data['first_property'])
            second_params = parse_string_to_list(data['second_property'])

        await self.bot.send_message(message.chat.id, "<b>Результаты ДЛЯ ЭП №1:\n"\
                                                        f"{solve_first(first_params)}</b>", parse_mode='html')

        await self.bot.send_message(message.chat.id, "<b>Результаты ДЛЯ ЭП №2:\n"\
                                                        f"{solve_second(second_params)}</b>", parse_mode='html')

        await self.bot.delete_state(message.from_user.id, message.chat.id)

    async def send_github_link(self, message: Message):
        await self.bot.send_message(message.chat.id, "https://github.com/Su1tan05/exam_bot")

    help_message = \
                '<b>И вот что я умею:\n'\
                '/help — помощь по командам бота\n'\
                '\n'\
                '/shpora — получение шпоры в формате pdf\n'\
                '\n'\
                '/solver — рашение задачи</b>'

    ep1_msg = \
        '<b>ЭП1:\n'\
        'P_номi: \n'\
        'n_i: \n'\
        'K_i: \n'\
        'cosf: \n'\
        'l: </b>'