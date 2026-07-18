import os
import sqlite3
import pandas

class Database:

  def __init__(self, path):
    self.main_db=sqlite3.connect(path, check_same_thread=False)
    self.Cursor=self.main_db.cursor() 
    self.export_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
    if not os.path.exists(self.export_dir):
        self.export_dir = os.path.expanduser('~')
    self.SQL('''CREATE TABLE IF NOT EXISTS Calculator (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        arguments TEXT,
        result TEXT
    )''')

  def SQL(self, query, parameters=()):
    do_it=self.Cursor.execute(query, parameters)
    self.main_db.commit()
    return do_it
  
  def insert(self, datas=()):
    self.SQL('INSERT INTO Calculator (arguments, result) VALUES (?, ?)', datas)

  def get_all_datas(self):
    return self.SQL('SELECT * FROM Calculator;').fetchall()
  
  def export_csv(self, rename):
    rsql = pandas.read_sql_query('SELECT * FROM Calculator;', self.main_db)
    file_path = os.path.join(self.export_dir, f'{rename}.csv')
    rsql.to_csv(file_path, index=False)

  def export_html(self, rename):
    rsql = pandas.read_sql_query('SELECT * FROM Calculator;', self.main_db)
    file_path = os.path.join(self.export_dir, f'{rename}.html')
    rsql.to_html(file_path, index=False)

  def export_excel(self, rename):
    rsql = pandas.read_sql_query('SELECT * FROM Calculator;', self.main_db)
    file_path = os.path.join(self.export_dir, f'{rename}.xlsx')
    rsql.to_excel(file_path, index=False)

  def closed(self):
    self.main_db.close()