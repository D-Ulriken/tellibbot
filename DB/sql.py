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

# new_users = default_add_info_table("user",
#                                    "name, age",
#                                    a="('James', 25)",
#                                    b="('Leila', 32)",
#                                    c="('Brigitte', 35)",
#                                    d="('Mike', 40)",
#                                    f="('Elizabeth', 21)")
#
# read_users = default_table_select("user",
#                                   name="user.name",
#                                   age="user.age")


write_query(data_base, user_table)
# write_query(data_base, new_users)
# info = read_query(data_base, read_users)
# print(info)