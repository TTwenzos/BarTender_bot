# Запустите этот фаил, для запуска бота
# Импорты встроенных библиотек 
import os
import sys
# Импорты сторонних библиотек || Смотрите фаил property.toml
import telebot
#  Свои импорты
sys.path.insert(0, os.path.join(sys.path[0], '..'))
sys.path.insert(0, os.path.join(sys.path[0], '..'))
from BarTender_bot.Handlers.Time_handler import greeting
from BarTender_bot.Handlers.User_handler import Roles, user_log_in, user_rerole
from BarTender_bot.Libs.Keybort_lib import Markup
from BarTender_bot.Parametrs.configs import TOKEN
from Logs.logs import logoose, logus

logus.debug(TOKEN)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def bot_started_command(message):
  logus.debug('Bot started')
  USER = user_log_in(message)
  markup = Markup('bb, b', 'Бар, Склад, Обратная связь', message.chat.id)
  bot.send_message(message.chat.id, f'{greeting()} {USER.get_name}. Вы вошли как {USER.get_role}', reply_markup=markup.get_markup)

@bot.message_handler(commands=["role"])
def user_rerole_inbot(message):
  user_id = message.chat.id
  markup = Markup("bb, bb, b", "Бармен, Кладовщик, Менеджер, Директор, Суперпользователь", user_id)
  bot.send_message(user_id, "Выберете роль", reply_markup=markup.get_markup)

@bot.message_handler(commands=["test"])
def user_rerole_inbot(message):
  user_id = message.chat.id
  markup = Markup("bs, md, a", "Бармен, Кладовщик, Менеджер, Директор, Суперпользователь", user_id)
  bot.send_message(user_id, "Выберете роль", reply_markup=markup.get_markup)

@bot.message_handler(content_types=['text'])
def message_text(message):
  user = user_log_in(message).get_name
  logus.debug(user)
  # logus.debug(text)
  text = str(message.text)
  markup = Markup('bb, b', 'Бар, Склад, Обратная связь', message.chat.id)
  if text == 'Бармен':
    user_rerole(user, Roles.BARTENDER)
    bot.send_message(message.chat.id, f'Теперь вы {Roles.BARTENDER.value}', reply_markup=markup.get_markup)
  elif text == 'Кладовщик':
    user_rerole(user, Roles.STOREKEEPER)
    bot.send_message(message.chat.id, f'Теперь вы {Roles.STOREKEEPER.value}', reply_markup=markup.get_markup)
  elif text == 'Менеджер':
    user_rerole(user, Roles.MANAGER)
    bot.send_message(message.chat.id, f'Теперь вы {Roles.MANAGER.value}',reply_markup=markup.get_markup)
  elif text == 'Директор':
    user_rerole(user, Roles.DIRECTOR)
    bot.send_message(message.chat.id, f'Теперь вы {Roles.DIRECTOR.value}', reply_markup=markup.get_markup)
  elif text == 'Суперпользователь':
    user_rerole(user, Roles.SUPERUSER)
    bot.send_message(message.chat.id, f'Теперь вы {Roles.SUPERUSER.value}', reply_markup=markup.get_markup)
  else: pass


if __name__ == '__main__':
  bot.infinity_polling()
  