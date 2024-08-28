# Импорты встроенных библиотек 
from dataclasses import dataclass
import sys
import os

# Импорты сторонних библиотек || Смотрите фаил property.toml
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Импорты своих модулей
if __name__ == '__main__':
  sys.path.insert(0, os.path.join(sys.path[0], '..'))
  sys.path.insert(0, os.path.join(sys.path[0], '..'))
from Handlers.User_handler import Roles, check_user_role
from Logs.logs import logus, logoose

class MarkupException(Exception):
  def message():
    message = 'Ошибка клавиатуры'
class LenButtonException(MarkupException): # TODO Разобраться как писать эксепшены
  def message():
    message = 'Ошибка указания кнопок и раскладки'

# markup = (bb,bb,x), buttons = "ent, order, bar, storage", handler = "/start"
class Markup:
  """
  Объект кастомизации клавиатуры телеграм бота, от него наследуется реплай и инлаин клавиатур.

  Parameters
  ----------
  :markup: :obj:`str` — расположение кнопок на клавиатуре.

  Количеством блоков указывается количество строк, буквы в блоке указывает на кнопки в строке. 
  
  Что-бы указать, каким ролям доступна кнопка используйте следующий код

    * **b** — Bartender 'Бармен' 
    * **m** — Manager 'Менеджер'
    * **s** — Storekeeper 'Кладовщик'
    * **d** — Director 'Директор'
    * **a** — Superuser 'Суперпользователь'

  Пример 
    *"bb, bbb, bb"*.

  :buttons: :obj:`str` — название кнопок, указывается в том же порядке что и **markup**. 

  Пример 
    *"button 1, button 2, button3"*.

  :user_id: :obj:`int` — Id пользователя, которому отправляется клавиатура.

  Returns
  -------
  :None: Пока ничего

  Exceptions
  ----------
  :LenButtonException: Кол-во букв при указании *markup*, должны совпадать с кол-вом названии.
  """

  keyboard_markup: ReplyKeyboardMarkup = None
  matrix: list = None
  buttons: dict = None

  def __init__(self,markup: str, buttons: str, user_id: int = 0, handler: str = None) -> ReplyKeyboardMarkup:
    self.markup: str = markup
    self.buttons: str = buttons
    self.handler: str = handler
    self.user_id: int = user_id
    Markup.get_matrix(self)

  @logus.catch()
  def get_matrix(self):
    raw_button_markup_list = self.markup.replace(' ', '').split(',')
    button_name_list = [i.strip(' ') for i in self.buttons.split(',')]
    matrix = list()
    button_markup_list = list()
    buttons = dict()
    count = 0
    for row in raw_button_markup_list:
      for column in row:
        if column == 'b':
          role = 0
        elif column == 's':
          role = 1
        elif column == 'm':
          role = 2
        elif column == 'd':
          role = 3
        elif column == 'a':
          role = 4
        
        button_markup_list.append(role)
        count += 1
      matrix.append(count)
      count = 0
    try:
      if len(button_markup_list) == len(button_name_list):
        for i in range(len(button_name_list)):
          buttons[i] = button_name_list[i], button_markup_list[i]
      else: raise LenButtonException()
    except Exception as e: logoose(__name__, e, "e")
    self.matrix = matrix
    self.buttons = buttons
  
  @property
  def set_markup(self):
    def check_user_privilege(user_role):
      if user_role == 'Бармен':
        privilege = 0
      elif user_role == 'Кладовщик':
        privilege = 1
      elif user_role == 'Менеджер':
        privilege = 2
      elif user_role == 'Директор':
        privilege = 3
      elif user_role == 'Суперпользователь':
        privilege = 4
      return privilege
    
    def chech_input_buttons(self, user):
      count = 0
      index = 0
      matrix_index = 0
      matrix = self.matrix
      buttons = self.buttons
      new_matrix = list()
      new_buttons = dict()
      for i in matrix:
        for j in range(i):
          if user >= buttons[count][1]:
            new_buttons[index] = buttons[count][0]
            index += 1
            matrix_index += 1
          count += 1
        if matrix_index > 0: new_matrix.append(matrix_index)
        matrix_index = 0
        self.buttons = new_buttons
        self.matrix = new_matrix
        logus.debug(f"{self.matrix}, {self.buttons}")
      
    logus.debug(check_user_role(self.user_id))
    user = check_user_privilege(check_user_role(self.user_id))
    chech_input_buttons(self, user)
    keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    self.keyboard_markup = keyboard_markup
    logus.debug(self.buttons)
    count = 0

    for i in self.matrix:
      if i == 1:
        logus.debug(self.buttons[count])
        btn = KeyboardButton(self.buttons[count])
        self.keyboard_markup.add(btn)
        count += 1
      elif i == 2:
        logus.debug(self.buttons[count])
        logus.debug(self.buttons[count+1])
        btn = KeyboardButton(self.buttons[count])
        btn1 = KeyboardButton(self.buttons[count+1])
        self.keyboard_markup.add(btn, btn1)
        count += 2
      elif i == 3:
        logus.debug(self.buttons[count])
        logus.debug(self.buttons[count+1])
        logus.debug(self.buttons[count+2])
        btn = KeyboardButton(self.buttons[count])
        btn1 = KeyboardButton(self.buttons[count+1])
        btn2 = KeyboardButton(self.buttons[count+2])
        self.keyboard_markup.add(btn, btn1, btn2)
        count += 3
      else: continue
    return self.keyboard_markup

  