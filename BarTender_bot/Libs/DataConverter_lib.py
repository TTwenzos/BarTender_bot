# Импорты встроенных библиотек 
import sys
import os
import pprint
# Импорты сторонних библиотек || Смотрите фаил property.toml
import openpyxl 
import sqlite3
import pandas as pd
#  Свои импорты
if __name__ == "__main__":
  sys.path.insert(0, os.path.join(sys.path[0], '..//..'))
from  Logs.logs import logoose, logus
from BarTender_bot.Parametrs.configs import BL_xlsx_path, BL_db_path



def bottle_listToSQL():
  conn = sqlite3.connect(BL_db_path)
  workbook = pd.ExcelFile(BL_xlsx_path)
  alco_list = workbook.parse('Alco', index_col=0)
  nonalco_list = workbook.parse('NonAlco', index_col=0)
  bottle_list = pd.concat([alco_list, nonalco_list])
  bottle_list.to_sql(name='Bottles', con=conn, if_exists='replace',index=False)
  conn.commit()
  conn.close()

  pprint.pprint(bottle_list)



bottle_listToSQL()