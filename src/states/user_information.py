from telebot.asyncio_handler_backends import State, StatesGroup

class UserInformation(StatesGroup):
    start = State()
    first_source_params = State()
    second_source_params = State()
    menu_keyboard = State()
    solver = State()