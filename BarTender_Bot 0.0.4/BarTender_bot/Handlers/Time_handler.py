from datetime import datetime, time, date


def get_date() -> str:
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
def greeting() -> str:
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
    if iso_date == 'today':
        today = datetime.today()
        week = today.isocalendar()[1]
        return int(week)
    else:
        iso = date.fromisoformat(iso_date)
        week = iso.isocalendar()[1]
        return int(week)