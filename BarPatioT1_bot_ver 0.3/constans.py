import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


RETRY_CREATE_REQUIREMENT = """Извините, но потребность уже была создана.
Если хотите ее пересоздать или удалить,
сообщите об этом вашему менеджеру."""
REQUIREMENT_NOT_EXISTS = 'Потребность не найдена'
REQUIREMENT_NOT_BEEN_CREATED_YET = "Потребность еще не создана."
REQUIREMENT_FORMAT_MESSAGE = '''Для создание потребности укажите
название позиции и необходимое количество.
Пожалуйста, используйте такой формат:
Название1 - кол-во
Название2 - кол-во
Напишете: 
«Готово» что-бы создать потребность
«Выход» или «Отмена» что-бы отменить создание.'''
INCORRECT_REQUIREMENT_FORMAT_MESSAGE = 'Не верный формат сообщения, попробуйте еще раз.'
REPLY_MENU_NON_COMMAND = 'Такой команды бот не знает.'
RETURN_MANY_REQUIRE_NAMES = 'Найдено несколько похожих наименований.'
RETURN_EMPTY_NAMES_REQUIRE = 'Позиции с таким названием не найдено.'
