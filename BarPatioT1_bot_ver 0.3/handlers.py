from constans import *
from config import *
from menu import Reply_menu_keyboard, Inline_menu_keyboard
from requirement import Require_request
from lib import Sql_libs

# Обработчики Реплай клавиатуры
class Reply_markup_handlers:  
    def reply_keyboard_handler(message):
        if message.text == 'Бар':
            bot.send_message(message.chat.id, 'Открыт бар', 
                                reply_markup = Reply_menu_keyboard.bar())
        elif message.text == 'Склад':
            bot.send_message(message.chat.id, 'Открыт склад',
                                reply_markup = Reply_menu_keyboard.storage())
        elif message.text == 'График':
            pass
        elif message.text == 'Стоп лист':
            pass
        elif message.text == 'Потребность':
            bot.send_message(message.chat.id, 'Открыто меню потребностей',
                                reply_markup = Reply_menu_keyboard.require())
        elif message.text == 'Создать потребность':
            bot.send_message(message.chat.id, REQUIREMENT_FORMAT_MESSAGE,
                                reply_markup = Reply_menu_keyboard.create_require())
            bot.register_next_step_handler(message, Require_request.recipient)
        elif message.text == 'Получить потребность':
            bot.send_message(message.chat.id, 'Какую потребность хотите получить?',
                                reply_markup= Inline_menu_keyboard.require())
        elif message.text == 'Инвентаризация':
            pass
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
