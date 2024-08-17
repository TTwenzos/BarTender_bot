import telebot
from telebot import types
from datetime import datetime, date
from loging import err_archivist

root_rights = False ## Рут-права

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
        time_current_datetime = f"""{datetime.now().hour}:
                                    {datetime.now().minute}:
                                    {datetime.now().second}"""

        time = f"local time {date_current_datetime} {time_current_datetime}"
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
        btnx = types.KeyboardButton('Обратная связь')
        markup.add(btn1, btn2)
        markup.add(btnx)
        return markup
    def bar(markup_name: str) -> types.ReplyKeyboardMarkup:
        def main_bar():
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Журналы')
            btn2 = types.KeyboardButton('Технологии')
            btnx = types.KeyboardButton('Обратно в меню')
            markup.add(btn1, btn2)
            markup.add(btnx)
            return markup
        def journals():
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Стоп лист')
            btn2 = types.KeyboardButton('Чек лист')
            btn3 = types.KeyboardButton('График')
            btnx = types.KeyboardButton('Обратно в меню')
            markup.add(btn2)
            markup.add(btn1, btn3)
            markup.add(btnx)
            return markup
        def technologies():
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Коктейли')
            btn2 = types.KeyboardButton('Лимонады')
            btn3 = types.KeyboardButton('Полуфабрикаты')
            bnt4 = types.KeyboardButton('Все ТТК')
            btnx = types.KeyboardButton('Обратно в меню')
            markup.add(btn2)
            markup.add(btn1, btn3)
            markup.add(btnx)
            return markup
        if markup_name == 'main':
            return main_bar()
        elif markup_name == 'journals':
            return journals()
        elif  markup_name == 'technologies':
            return technologies()
        else: err_archivist(__name__, 'Неверный вызов меню бара')
    def storage(markup_name: str) -> types.ReplyKeyboardMarkup:
        def main_storage():
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Потребность')
            btn2 = types.KeyboardButton('Инвентаризация')
            btnx = types.KeyboardButton('Обратно в меню')
            markup.add(btn1, btn2)
            markup.add(btnx)
            return markup
        def require():
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            if root_rights == True:
                btn_del = types.KeyboardButton('Удалить потребность')
                markup.add(btn_del)
            btn1 = types.KeyboardButton('Создать потребность')
            btn2 = types.KeyboardButton('Получить потребность')
            btnx = types.KeyboardButton('Обратно в меню')
            markup.add(btn1, btn2)
            markup.add(btnx)
            return markup
        def create_require():
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Готово')
            btn2 = types.KeyboardButton('Отмена')
            markup.add(btn1, btn2)
            return markup
        def inventory():
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Начать инвентаризацию')
            btn2 = types.KeyboardButton('Получить инвентаризацию')
            btnx = types.KeyboardButton('Обратно в меню')
            markup.add(btn1, btn2)
            markup.add(btnx)
            return markup

        if markup_name == "main":
            return main_storage()
        elif markup_name == "require":
            return require()
        elif markup_name == "create_require":
            return create_require()
        elif markup_name == 'inventory':
            return inventory()
        else: err_archivist(__name__, 'Неверный вызов меню склада')
class Inline_menu_keyboard:
    def require():
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('За эту неделю',
                                            callback_data = 'this_week_require')
        btn2 = types.InlineKeyboardButton('За прошлую неделю',
                                            callback_data = 'last_week_require')
        btn3 = types.InlineKeyboardButton('На следующую неделю',
                                            callback_data = 'next_week_require')
        btn4 = types.InlineKeyboardButton('На другой период',
                                            callback_data = 'other_week_require')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
        return markup
