from hendlers.message import MessageHandler
from states.user_information import UserInformation

def setup_hendlers(bot):
    hendler = MessageHandler(bot);
    bot.message_handler(commands=['start'])(hendler.start_handler)
    bot.message_handler(commands=['shpora'])(hendler.send_pdf)
    bot.message_handler(commands=['help'])(hendler.help_handler)
    bot.message_handler(commands=['solver'])(hendler.task_init_message)
    bot.message_handler(commands=['github'])(hendler.send_github_link)
    bot.message_handler(state=UserInformation.first_source_params)(hendler.set_first_source_params)
    # bot.message_handler(content_types=['text'])(hendler.handle_callback)
