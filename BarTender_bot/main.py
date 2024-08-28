# Запустите этот фаил, для запуска бота
# Импорты встроенных библиотек 
import sys
import os
# Импорты сторонних библиотек || Смотрите фаил property.toml
import telebot
#  Свои импорты
sys.path.insert(0, os.path.join(sys.path[0], '..'))
from Parametrs.configs import TOKEN
from Handlers.User_handler import user_log_in
from Handlers.Keybort_handler import Markup
from Handlers.Time_handler import greeting
from Logs.logs import logoose, logus

logus.debug(TOKEN)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def bot_started_command(message):
  logus.debug('Bot started')
  USER = user_log_in(message)
  bot.send_message(message.chat.id, f'{greeting()} {USER.get_name}. Вы вошли как {USER.get_role}')

@bot.message_handler(commands=["restart"])
def bot_restarted_command(message):
  logus.debug('Bot restarted')



@bot.message_handler(commands=["md"])
def bot_restarted_command(message):
  mar = Markup('bb, b', 'Бар, Склад, Обратная связь', message.chat.id)
  bot.send_message(message.chat.id, 'md', reply_markup=mar.get_markup)

@bot.message_handler(content_types=['text'])
def message_text(message):
  text = message.text
  id = message.chat.id
  if text == 'Бар':
    markup = Markup('bs, mmmm, a, b', 'Бармен, Кладовщик, Менеджер, Директор, Админ, Бармен', id)
    bot.send_message(id, 'Бар', reply_markup=markup.get_markup)
  elif text == 'Склад': pass
  elif text == 'Обратная связь': pass



if __name__ == '__main__':
  bot.infinity_polling()
  