from DBApi_new import *


def add_book():
    name = input("Enter name")
    author = input("Enter author")
    description = input("Enter description")
    release = input("release")
    tags = input("tags")
    links = input("link")
    book = Book(name, author, description, release, tags, links)
    books.append(book)
    add_to_sql()


add_book()