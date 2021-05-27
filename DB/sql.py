from DB.sqlGETS import *
from DB.sqlSETS import *

data_base = create_connection("BookDB")

user_table = default_write_table("book",
                                id="id INTEGER PRIMARY KEY AUTOINCREMENT",
                                name="name TEXT NOT NULL",
                                author="author TEXT NOT NULL",
                                description="description TEXT NOT NULL",
                                release="release TEXT NOT NULL",
                                tags="tags TEXT NOT NULL")

write_query(data_base, user_table)
