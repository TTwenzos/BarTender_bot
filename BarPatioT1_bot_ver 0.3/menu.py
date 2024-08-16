import telebot
from telebot import types
from datetime import datetime, date

class Time:
    def get_date(day = "today") -> str:
        if day == "today":
            date_day = date.today()
        return str(date_day)
    
    def get_hour() -> int:
        current_datetime = datetime.now()
        hour = current_datetime.hour
        return hour
    
    def local_time() -> str:
        date_current_datetime = str(date.today())
        time_current_datetime = str(datetime.now().hour) + ':' + str(
                                    datetime.now().minute) + ':' + str(
                                    datetime.now().second)
        time = 'local time — ' + date_current_datetime + ' ' + time_current_datetime
        return time
    
    def greeting(hour) -> str:
        if hour >= 6 and hour < 12:
            buona = 'Buongiorno'
        elif hour >= 12 and hour < 18:
            buona = 'Buon pomeriggio'
        elif hour >= 18 and hour < 24:
            buona = 'Buona sera'
        elif hour >= 0 and hour < 6:
            buona = 'Buona notte'
        return str(buona)
    def get_week(iso_date = 'today') -> int:
        if iso_date == 'today':
            today = datetime.today()
            week = today.isocalendar()[1]
            return int(week)
        else:
            iso = date.fromisoformat(iso_date)
            week = iso.isocalendar()[1]
            return int(week)

class Reply_menu_keyboard:
    def main_reply_keyboard():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Бар')
        btn2 = types.KeyboardButton('Склад')
        btn3 = types.KeyboardButton('Обратная связь')
        markup.add(btn1, btn2)
        markup.add(btn3)
        return markup
    def bar():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('График')
        btn2 = types.KeyboardButton('Стоп лист')
        btn3 = types.KeyboardButton('Обратно в меню')
        markup.add(btn1, btn2)
        markup.add(btn3)
        return markup
    def storage():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Потребность')
        btn2 = types.KeyboardButton('Инвентаризация')
        btn3 = types.KeyboardButton('Обратно в меню')
        markup.add(btn1, btn2)
        markup.add(btn3)
        return markup
    def create_require():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Готово')
        btn2 = types.KeyboardButton('Отмена')
        markup.add(btn1, btn2)
        return markup
    def require():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Создать потребность')
        btn2 = types.KeyboardButton('Получить потребность')
        btn3 = types.KeyboardButton('Обратно в меню')
        markup.add(btn1, btn2)
        markup.add(btn3)
        return markup
    
class Inline_menu_keyboard:
    def require():
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('За эту неделю', callback_data = 'this_week_require')
        btn2 = types.InlineKeyboardButton('За прошлую неделю', callback_data = 'last_week_require')
        btn3 = types.InlineKeyboardButton('На следующую неделю', callback_data = 'next_week_require')
        btn4 = types.InlineKeyboardButton('На другой период', callback_data = 'other_week_require')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
        return markup
