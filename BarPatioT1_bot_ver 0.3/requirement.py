from lib import BottleList, Sql_libs
from datetime import date
import menu
from constans import *
import loging

try:
    fullname_require = {}

    class Require_request:
        # Функция принимающая грязный запрос, возвращающая чистый запрос в виде словаря.
        def announcer(message) -> dict:
            user_text = str(message.text).lower()
            clean_raw_request_list = []
            clean_raw_request_dict = {}
            raw_request_list = user_text.split('\n')
            for i in raw_request_list:
                clean_raw_request_list.append(i.split('-'))
            try:
                for i in clean_raw_request_list:
                    clean_raw_request_dict[i[0]] = i[1]
            except IndexError: 
                bot.send_message(message.chat.id, INCORRECT_REQUIREMENT_FORMAT_MESSAGE)
                bot.send_message(message.chat.id, REQUIREMENT_FORMAT_MESSAGE)
                return None
            except Exception as e:
                loging.err_archivist(__name__, e)  
            else: return clean_raw_request_dict
        
        # Функция принимающая запрос от пользователя.
        def recipient(message): 
            global fullname_require
            exit_require = ['выход', 'отмена']
            if str(message.text).lower() in 'готово':
                Require_request.stenographer(message, fullname_require)
            elif str(message.text).lower() in exit_require:
                bot.send_message(message.chat.id, 'Потребность удалена', 
                                    reply_markup=menu.Reply_menu_keyboard.main_reply_keyboard())
                fullname_require = {}
            else: 
                raw_req = {}
                raw_req = Require_request.announcer(message) # Получение словаря с запросом пользователя
                if raw_req == None:
                    pass
                else:
                    for i in raw_req:
                        names = str(BottleList.search(str(i).lower(), 'only_names')) # Получение библиотеки с названиями и сравнение ее со словарем запроса от пользователя
                        if 'Ничего не найдено' in names:
                            bot.send_message(message.chat.id, 'Позиция «' + str(i) + '» не найдена' )
                            continue
                        elif 'Найдены следующие позиции:' in names and 'Уточните название...' in names:
                            bot.send_message(message.chat.id, "По названию: «" + str(i) + "» " + names)
                            continue
                        else:
                            value = raw_req[i] 
                            fullname_require[names] = value # создание словаря с полным названием позиций
                bot.register_next_step_handler(message, Require_request.recipient)

        def stenographer(message, require: dict):
            global fullname_require
            clean_str_require = str(fullname_require)
            clean_str_require = clean_str_require.replace('[', '').replace(']', '').replace('{', '').replace(  #Чистка строки от мусора
                                                            '}', '').replace('"', '').replace('"', '').replace(
                                                            "'", '').replace('}', "'").replace(', ', '\n')
            call = Sql_libs.create_requires_lib(clean_str_require)
            if call == 'done': bot.send_message(message.chat.id, 'Потребность создана',  
                                                    reply_markup=menu.Reply_menu_keyboard.main_reply_keyboard())
            else: bot.send_message(message.chat.id, RETRY_CREATE_REQUIREMENT,  
                                                    reply_markup=menu.Reply_menu_keyboard.main_reply_keyboard())

            fullname_require = {} 

except Exception as e:
    loging.err_archivist(__name__, e)
