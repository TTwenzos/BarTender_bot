# Импорты встроенных библиотек 
from datetime import datetime, date

def get_date() -> str:
    '''Возвращает дату сегодня в формате **iso**'''
    date_day = date.today()
    return str(date_day)
def get_hour() -> int:
    '''Возвращает текущий час'''
    current_datetime = datetime.now()
    hour = current_datetime.hour
    return hour
def local_time() -> str:
    '''Возвращает текущую дату и время в формате **iso**'''
    date_current_datetime = str(date.today())
    time_current_datetime = f"""{datetime.now().hour}:
                                {datetime.now().minute}:
                                {datetime.now().second}"""
    time = f"local time {date_current_datetime} {time_current_datetime}"
    return time
def greeting() -> str:
    '''Приветствие в зависимости от времени на сервере'''
    hour = get_hour()
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
    '''Возвращает номер текущей недели.
    Если указать дату в формате **iso**, вернет номер недели'''
    if iso_date == 'today':
        today = datetime.today()
        week = today.isocalendar()[1]
        return int(week)
    else:
        iso = date.fromisoformat(iso_date)
        week = iso.isocalendar()[1]
        return int(week)