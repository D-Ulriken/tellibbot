import sqlite3
from sqlite3 import Error


def read_query(connection, query):
    """Читает поля таблици нужно передать запрос"""
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



def default_table_select(name_table, **kwargs):
    """выбор таблици для чтения"""
    value = ""
    for args in kwargs.values():
        value += args + ","
    value = value[:-1]
    select = """
    SELECT
        {value}
    FROM
        {name_table}
    """.format(name_table=name_table, value=value)
    return select


def default_table_from(**kwargs):
    """REWRITE FUNCTION"""
    value = ""
    for args in kwargs.values():
        value += args + ","
    value = value[:-1]
    select = """
    FROM
    {value}
    INNER JOIN users ON users.id = posts.user_id
    """.format(value=value)
    return select