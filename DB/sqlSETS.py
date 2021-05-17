import sqlite3
import sys
from sqlite3 import Error
import os

DB = sys.path[1] + "\BookDB.sqlLite"

def create_connection(path=DB):
    """Делает подключение к БД записывать в переменную и использовать"""
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def write_query(connection, query):
    """Делает подключение к бд и передает в нее запись"""
    cursor = connection.cursor()# object of db
    try:
        cursor.execute(query) # integrate values in db
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def default_write_table(name_table: str, **kwargs: str):
    """делает таблицу, с полями в зависимости от количества аргументов"""
    fields = ""
    for args in kwargs.values():
        fields += args + ","
    fields = fields[:-1]
    create_users_table = """
    CREATE TABLE IF NOT EXISTS {name_table} (
        {args}
    );
    """.format(name_table=name_table, args=fields)
    return create_users_table


def default_add_info_table(name_table: str, fields: str, **kwargs: str):
    """Добавляет новые значения в таблицу и в определенные поля"""
    info = ""
    for args in kwargs.values():
        info += args + ","
    values = info[:-1]
    add_users = """
    INSERT INTO 
      {name_table}({fields})
    VALUES
      {values};
    """.format(name_table=name_table, fields=fields, values=values)
    return add_users