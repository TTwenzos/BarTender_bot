# Импорты встроенных библиотек 
import sys
import os


# Импорты сторонних библиотек || Смотрите фаил property.toml
from telebot import TeleBot, types
#  Свои импорты
if __name__ == "__main__":
  sys.path.insert(0, os.path.join(sys.path[0], '../..'))
from BarTender_bot.Handlers.Time_handler import greeting
from BarTender_bot.Libs.Keyboard_lib import Markup
from BarTender_bot.Handlers.User_handler import check_user_role
from BarTender_bot.Parametrs.constans import FEEDBACK_SALUTE_MESSAGE, BOT_UNKNOWN_TEXT_COMMAND


def replay_keyboard_handler(message, bot: TeleBot):
  text = message.text
  user_id = message.chat.id
  user_role = check_user_role(user_id)
  # Меню бота:
  if text == 'Вернуться в меню 🔙':
    markup = Markup('bb, b', 'Бар 🍸, Склад 📦, Обратная связь 📞', message.chat.id)
    bot.send_message(message.chat.id, f'{greeting()}', reply_markup=markup.get_markup)  
  elif text == 'Обратная связь 📞':
    bot.send_message(user_id, FEEDBACK_SALUTE_MESSAGE)
  # Меню Бара
  elif text == 'Бар 🍸':
    markup = Markup('bb, bbb, b', '''График 📅, Топ\стоп-лист 🔝⛔
                                    ,Списания ✍, Технологии 🛠️, Чек-лист ✅
                                    ,Вернуться в меню 🔙''', user_id)
    bot.send_message(user_id, "Открыт бар", reply_markup=markup.get_markup)
  # Вкладка — «График»
  elif text == 'График 📅':
    markup = Markup('md, b', 'Добавить график 📅, Удалить график ❌, Вернуться в меню 🔙', user_id)
    bot.send_message(user_id, "График", reply_markup=markup.get_markup)
  elif text == 'Добавить график 📅': pass
  elif text == 'Удалить график ❌': pass
  # Вкладка — «Стоп-листа»
  elif text == 'Топ\стоп-лист 🔝⛔':
    markup = Markup('bb, mmm, b', '''Получить Топ\стоп-лист📤
                                    ,Добавить позицию в стоп-лист 📥
                                    ,Создать или Изменить топ\стоп-лист ✏️
                                    ,Изменить топ-лист 🔝
                                    ,Изменить стоп-лист ⛔
                                    ,Вернуться в меню 🔙''', user_id)
    bot.send_message(user_id, "Топ/стоп-лис", reply_markup=markup.get_markup)
  elif text == 'Получить Топ\стоп-лист 📤': pass
  elif text == 'Добавить позицию в стоп-лист 📥': pass
  elif text == 'Создать или Изменить топ\стоп-лист ✏️': pass
  elif text == 'Изменить топ-лист 🔝': pass
  elif text == 'Изменить стоп-лист ⛔': pass
  # Вкладка — «Списания»
  elif text == 'Списания ✍':
    markup = Markup('b, md, b', '''Создать список списаний ✏️
                                  ,Получить список списаний 📲
                                  ,Удалить списания ❌
                                  ,Вернуться в меню 🔙''', user_id)
    bot.send_message(user_id, "Списания", reply_markup=markup.get_markup)
  elif text == 'Создать список списаний ✏️': pass
  elif text == 'Получить список списаний 📲': pass
  elif text == 'Удалить списания': pass
  # Вкладка — «Технологий»
  elif text == 'Технологии 🛠️':
    markup = Markup('bb, b', '''Все ттк 📖,
                                Поиск рецептуры 🔍,
                                Вернуться в меню 🔙''', user_id)
    bot.send_message(user_id, "Технологии", reply_markup=markup.get_markup)
  elif text == 'Все ттк 📖': pass
  elif text == 'Поиск рецептуры 🔍': pass
  # Вкладка — «Чек-лист»
  elif text == 'Чек-лист ✅':
    markup = Markup('bb, md, b', '''Создать чек-лист 📃,
                                    Посмотреть чек-лист 📋,
                                    Все чек-листы 📅,
                                    Удалить чек-лист ❌,
                                    Вернуться в меню 🔙''', user_id)
    bot.send_message(user_id, "Чек-лист", reply_markup=markup.get_markup)
  elif text == 'Создать чек-лист 📃': pass
  elif text == 'Посмотреть чек-лист 📋': pass
  elif text == 'Все чек-листы 📅': pass
  elif text == 'Удалить чек-лист ❌': pass
  # Меню Склада
  elif text == 'Склад 📦':
    markup = Markup('bb, b', '''Заказ 🛒,
                                Инвентаризация 📋,
                                Вернуться в меню 🔙''', user_id)
    bot.send_message(user_id, "Склад", reply_markup=markup.get_markup)
  # Вкладка — «Заказ»
  elif text == 'Заказ 🛒':
    markup = Markup('b, sd, b', '''Создать заказ 🛒
                                  ,Просмотреть список заказов 👀
                                  ,Удалить заказ ❌
                                  ,Вернуться в меню 🔙''', user_id)
    bot.send_message(user_id, "Заказ", reply_markup=markup.get_markup)
  elif text == 'Создать заказ 🛒': pass
  elif text == 'Просмотреть список заказов 👀': pass
  elif text == 'Удалить заказ ❌': pass
  #  Вкладка — «Инвентаризация»
  elif text == 'Инвентаризация 📋':
    markup = Markup('b, bs, ssd, d, b', '''Начать инвентаризацию 📝
                                          ,Пустой бланк 📃
                                          ,Кол-во по отдельной позиции 👀
                                          ,Получить инвентаризацию 📋
                                          ,Все позиции списком 📲
                                          ,Заполненный бланк по неделям 📅
                                          ,Удалить инвентаризацию ❌
                                          ,Вернуться в меню 🔙''', user_id)
    bot.send_message(user_id, "Инвентаризация", reply_markup=markup.get_markup)
  elif text == 'Начать инвентаризацию 📝': pass
  elif text == 'Получить инвентаризацию 📋': pass
  elif text == 'Пустой бланк 📃': pass
  elif text == 'Заполненный бланк по неделям 📅': pass
  elif text == 'Кол-во по отдельной позиции 👀': pass
  elif text == 'Все позиции списком 📲': pass
  elif text == 'Удалить инвентаризацию ❌': pass

  else: bot.send_message(user_id, BOT_UNKNOWN_TEXT_COMMAND)


# Сбор обратной связи
def feedback(message): pass
