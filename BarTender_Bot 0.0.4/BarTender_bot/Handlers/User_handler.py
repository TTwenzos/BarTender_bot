# Импорты встроенных библиотек 
from dataclasses import dataclass
from enum import Enum
import sys
import os

# Импорты сторонних библиотек || Смотрите фаил property.toml
import sqlite3

# Импорты своих модулей
if __name__ == '__main__':
  sys.path.insert(0, os.path.join(sys.path[0], '..'))
  sys.path.insert(0, os.path.join(sys.path[0], '..'))
from Logs.logs import logoose, logus
from Handlers.Time_handler import get_date

@dataclass
class Roles(str, Enum):
  SUPERUSER = "Суперпользователь"
  DIRECTOR = "Директор"
  STOREKEEPER = "Кладовщик"
  MANAGER = "Менеджер"
  BARTENDER = "Бармен"

class User:
  def __init__(self, username: str, role: str, id: int) -> None:
    self.username: str = username
    self.role: str = role
    self.id: int = id
  @property
  def get_name(self):
    return self.username
  @property
  def get_role(self):
    return self.role
  @property
  def get_id(self):
    return self.id


def user_log_in(message):
  username = f"{message.from_user.first_name} {message.from_user.last_name} ({message.from_user.username})"
  user_id = message.chat.id
  user = user_init(username, user_id)
  return user

# Инициализация пользователя
def user_init(username: str, user_id: int) -> User:
  users = sqlite3.connect("Bartender_bot\\Data Bases\\Users.db")
  cursor = users.cursor()
  cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                      (
                      username text primary key,
                      role text,
                      id int,
                      date text
                      )""")
  users.commit()
  cursor.execute("SELECT * FROM users WHERE username = '%s'" % (username))
  user = cursor.fetchone()
  try:
    if user == None:
      logus.debug(f'Пользователя: «{username}» — нет в базе') 
      write_users(username, user_id) # Если полльзователя нет в базе, регистрируем
      cursor.execute("SELECT * FROM users WHERE username = '%s'" % (username))
      user = cursor.fetchone()
    name = user[0]
    role = user[1]
    id = user[2]
  except Exception as e:
    logoose(__name__, e, 'e')
  cursor.close()
  users.close()
  logus.debug(f'Пользователь: {username}, вошел в бота')
  return User(name, role, id)

# Регистрация пользователя
def write_users(username: str, user_id: int, role: str = Roles.BARTENDER):
  date = get_date()
  role = role.value
  users = sqlite3.connect("BarTender_bot\\Data Bases\\Users.db")
  cursor = users.cursor()
  cursor.execute("INSERT INTO users VALUES ('%s', '%s', '%s', '%s')" % (username, role, user_id, date))
  users.commit()
  logoose(__name__, f'Пользователь: "{username}" — зарегистрирован!', 'i')
  cursor.close()
  users.close()

# Переназначение роли пользователя. По умолчанию каждый пользователь регистрируется как бармен 
def user_rerole(username: str, role: Roles): 
  users = sqlite3.connect("Bartender_bot\\Data Bases\\Users.db")
  cursor = users.cursor()
  cursor.execute("UPDATE users SET role = '%s' WHERE username = '%s'" % (role.value, username))
  logoose(__name__, f'Пользователю: {username} — назначена роль {role.value}', "s")
  users.commit()
  cursor.close()
  users.close()

def user_del(username: str):
  users = sqlite3.connect("Bartender_bot\\Data Bases\\Users.db")
  cursor = users.cursor()
  cursor.execute("DELETE FROM Users WHERE username = '%s'" % (username))
  users.commit()
  logus.debug(f'Пользователь: {username} — Удален')
  cursor.close()
  users.close()

def check_user_role(user_id) -> Roles:
  users = sqlite3.connect("Bartender_bot\\Data Bases\\Users.db")
  cursor = users.cursor()
  cursor.execute("SELECT role FROM users WHERE id = '%s'" % (user_id))
  role = cursor.fetchone()
  cursor.close()
  users.close()
  return str(*role)

# user_rerole('John Doe', Roles.MANAGER)
# user_rerole("Игорь Макарьевский (TTwenzos)", Roles.MANAGER)

# user_del('Игорь Макарьевский (TTwenzos)')
