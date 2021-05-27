from DBAPI import *

def parser_book():
    file = open("book.txt", "r", encoding="utf-8")
    counter = 0

    name = None
    author = None
    description = None
    release = None
    tags = None
    links = None

    for line in file.readlines():
        line = line.replace("\n", "")
        if counter == 0:
            name = line
        if counter == 1:
            author = line
        if counter == 2:
            description = line
        if counter == 3:
            release = line
        if counter == 4:
            tags = line
        if counter == 5:
            links = line
        counter += 1
        if counter == 6:
            book = Book(name, author, description, release, tags, links)
            books.append(book)
            counter = 0
    add_to_sql()

parser_book()