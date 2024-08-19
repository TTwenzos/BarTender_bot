from constans import *
from config import *
from menu import Reply_menu_keyboard, Inline_menu_keyboard
from requirement import Require_request
from lib import Sql_libs
from loguru import logger
from logs.loging import info_logger, feedback
import root

# Обработчики Реплай клавиатуры
class Reply_markup_handlers:  
    def reply_keyboard_handler(message):
        if message.text == 'Бар':
            bot.send_message(message.chat.id, 'Открыт бар', 
                                reply_markup = Reply_menu_keyboard.bar("main"))
        elif message.text == 'Склад':
            bot.send_message(message.chat.id, 'Открыт склад',
                                reply_markup = Reply_menu_keyboard.storage("main"))
        elif message.text == 'Журналы':
            bot.send_message(message.chat.id, 'Открыты журналы',
                                reply_markup = Reply_menu_keyboard.bar("journals"))
        elif message.text == 'Технологии':
            bot.send_message(message.chat.id, 'Открыты технологии',
                                reply_markup = Reply_menu_keyboard.bar("technologies"))
        elif message.text == 'Потребность':
            bot.send_message(message.chat.id, 'Открыто меню потребностей',
                                reply_markup = Reply_menu_keyboard.storage("require"))
        elif message.text == 'Инвентаризация':
            bot.send_message(message.chat.id, 'Открыто меню инвентаризации',
                                reply_markup = Reply_menu_keyboard.storage("inventory"))
        elif message.text == 'Создать потребность':
            bot.send_message(message.chat.id, REQUIREMENT_FORMAT_MESSAGE,
                                reply_markup = Reply_menu_keyboard.storage("create_require")) 
            bot.register_next_step_handler(message, Require_request.recipient)
        elif message.text == 'Получить потребность':
            bot.send_message(message.chat.id, 'Какую потребность хотите получить?',
                                reply_markup= Inline_menu_keyboard.require())
        elif message.text == 'Удалить потребность':
            if os.environ.get("SUPERUSER_RIGHT") == "True":         # Проверка на права супер-пользователя
                bot.send_message(message.chat.id, 'Потребность удалена',
                            reply_markup=Reply_menu_keyboard.main_reply_keyboard())
            else: bot.send_message(message.chat.id, 'Вы не можете этого сделать',
                            reply_markup=Reply_menu_keyboard.main_reply_keyboard())
        elif message.text == 'Обратная связь':
            bot.send_message(message.chat.id, FEEDBACK_MESSAGE)
            bot.register_next_step_handler(message, feedback)
        elif message.text == 'Обратно в меню':
            bot.send_message(message.chat.id, 'Вернулись в меню',
                            reply_markup=Reply_menu_keyboard.main_reply_keyboard())
        else: bot.send_message(message.chat.id, REPLY_MENU_NON_COMMAND)

# Обработчики ин-лаин клавиатуры
class Callback_data_handlers:
    @bot.callback_query_handler(func=lambda callback: True)
    def send_require(callback):
        if callback.data == 'this_week_require':
            require = Sql_libs.get_create_requires_lib('this')
            if require in "err 0.1":
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, REQUIREMENT_NOT_BEEN_CREATED_YET,
                                        reply_markup=Reply_menu_keyboard.main_reply_keyboard())
            else:
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, require,
                                        reply_markup=Reply_menu_keyboard.main_reply_keyboard())
        elif callback.data == 'last_week_require':
            require = Sql_libs.get_create_requires_lib('last')
            if require in "err 0":
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, REQUIREMENT_NOT_EXISTS,
                                        reply_markup=Reply_menu_keyboard.main_reply_keyboard())
            else:
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, require,
                                        reply_markup=Reply_menu_keyboard.main_reply_keyboard())
        elif callback.data == 'next_week_require':
            require = Sql_libs.get_create_requires_lib('next')
            if require in "err 0":
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, REQUIREMENT_NOT_EXISTS, 
                                        reply_markup=Reply_menu_keyboard.main_reply_keyboard())
            else:
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.send_message(callback.message.chat.id, require, 
                                        reply_markup=Reply_menu_keyboard.main_reply_keyboard())
        elif callback.data == 'other_week_require':
            bot.delete_message(callback.message.chat.id, callback.message.message_id)
            bot.send_message(callback.message.chat.id, 'Потребности за другие периоды пока не доступны', 
                                        reply_markup=Reply_menu_keyboard.main_reply_keyboard())

class PasswordException(Exception):
    @property
    def message():
        'Введен неверный пароль'


class Password_handler:
    logger.catch()
    def root_handler(message):
        user = f"{message.from_user.first_name} {message.from_user.last_name} ({message.from_user.username})"
        password = message.text
        pass_check = root.root(user=user, password=password)
        if pass_check == True:
            bot.send_message(message.chat.id, "Пароль принят")
        else:
            bot.send_message(message.chat.id, "Введен неверный пароль")
            raise PasswordException