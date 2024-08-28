# Запустите этот фаил, для запуска бота
# Импорты встроенных библиотек 
import sys
import os
# Импорты сторонних библиотек || Смотрите фаил property.toml
import telebot

#  Свои импорты
sys.path.insert(0, os.path.join(sys.path[0], '..'))
from Parametrs.configs import TOKEN
from Logs.logs import logoose, logus

bot = telebot.TeleBot(TOKEN)

try:
  @bot.message_handler(commands=["start"])
  def bot_started_command(message):
    logus.debug('bot started')
  @bot.message_handler(commands=["restart"])
  def bot_restarted_command(message):
    logus.debug('bot restarted')
  
# Дебаг команнды, для входа в бота под разными ролями 
  @bot.message_handler(commands=["root"]) # Вход под суперпользователем
  def root_debug_user_command(message):
    logus.debug('root have been received')
  @bot.message_handler(commands=["director"]) # Вход под директором
  def director_debug_user_command(message):
    logus.debug('entrance by director')
  @bot.message_handler(commands=["storekeeper"]) # Вход под кладовщиком
  def storekeeper_debug_user_command(message):
    logus.debug('entrance by storekeeper')
  @bot.message_handler(commands=["manager"]) # Вход под менеджером
  def manager_debug_user_command(message):
    logus.debug('entrance by manager')
  @bot.message_handler(commands=["bartender"]) # Вход под барменом
  def bartender_debug_user_command(message):
    logus.debug('entrance by bartender')
    
except Exception as e:
  logoose(__name__, e, 'c')

if __name__ == '__main__':
  bot.infinity_polling()