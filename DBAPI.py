from DB.sqlGETS import *
from DB.sqlSETS import *
from Book import *
import random
import re

books = []

book_table = default_write_table("books",
                                 id="id INTEGER PRIMARY KEY AUTOINCREMENT",
                                 name="name TEXT NOT NULL",
                                 author="author TEXT NOT NULL",
                                 description="description TEXT NOT NULL",
                                 release="release TEXT NOT NULL",
                                 tags="tags TEXT NOT NULL",
                                 links="links TEXT NOT NULL")

read_books = default_table_select("books",
                                  name="books.name",
                                  author="books.author",
                                  description="books.description",
                                  release="books.release",
                                  tags="books.tags",
                                  links="books.links")

def add_to_sql():
    global books
    data_base = create_connection(DB)
    for book in books:
        new_users = default_add_info_table("books",
                                           "name, author, description, release, tags, links",
                                           a="('{name}', '{author}', '{description}', '{release}', '{tags}', '{links}')"
                                           .format(name=book.name, author=book.author,
                                                   description=book.description,
                                                   release=book.release, tags=book.tags, links=book.links))
        write_query(data_base, new_users)
    books = []

def take_random_book(count):
    books_ = []
    data_base = create_connection(DB)
    info = read_query(data_base, read_books)
    for i in range(count):
        rnd = random.randrange(0, len(info))
        book = Book(info[rnd][0], info[rnd][1], info[rnd][2], info[rnd][3], info[rnd][4], info[rnd][5])
        books_.append(book)
    return books_

def find_name(word, find: int = 0):
    """0 - name, 1 - author"""
    data_base = create_connection(DB)
    books_info = read_query(data_base, read_books)
    book = None
    books = []

    if find < 0 or find > 1:
        find = 0
    counter = 0
    for i in range(len(books_info)):
        result = re.match(r'' + word.lower(), books_info[i][find].lower())

        if result is not None:
            counter += 1
            if find == 0:
                book = Book(books_info[i][0], books_info[i][1], books_info[i][2],
                            books_info[i][3], books_info[i][4], books_info[i][5])
            if find == 1:
                book = Book(books_info[i][0], books_info[i][1], books_info[i][2],
                            books_info[i][3], books_info[i][4], books_info[i][5])
            books.append(book)
    return books


#find_name(input("Cto nyzhno nayti"), 0)