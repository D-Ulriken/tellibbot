import botAPI_new as bot
from DBApi_new import *

if __name__ == '__main__':
    data_base = create_connection(DB)
    write_query(data_base, book_table)
    bot.start_bot()
