import telebot
from telebot import types

import DBApi_new as db

token = '1657569148:AAFjoH6Q7Vv-bkme2SUghcdYYWJybOWaDZM'

bookBot = telebot.TeleBot(token)

counter = 0

query_book_finder = ""

@bookBot.message_handler(commands=['start'])
def start_bot(message):
    img = open('welcome.png', 'rb')
    bookBot.send_photo(message.chat.id, img, "Вітаємо вас в *BookBot* 🙋‍♂\n\n"
                                             "📕-------------------------------------------------------📘\n\n"
                                             "Бот з перспективною базою книг 😀\n\n"
                                             "💡 Для перегляду команд натисни /help", parse_mode='Markdown')


@bookBot.message_handler(commands=['help'])
def help_bot(message):
    bookBot.send_message(message.chat.id, "Як мною користуватись?\n"
                                          "Все дуже просто, вибире спосіб пошуку та напиши назву книги або автора для пошуку"
                                          "\n\n"
                                          "Список доступних команд для мене: \n\n"
                                          "/start - перша команда з якої почнеться наше спілкування\n"
                                          "/book *НАЗВА КНИГИ* - пошук книжки по її назві\n"
                                          "/author *ІМ'Я АВТОРА* - пошук книжки по автору\n"
                                          "/random - випадкова книжка", parse_mode='Markdown')


@bookBot.message_handler(commands=['book'])
def book_finder(message):
    print(message.text)
    global counter, books, query_book_finder

    book_name = str(message.text).replace("/book", "")
    book_name = book_name.lstrip()


    if book_name == "":
         bookBot.send_message(message.chat.id, "Введіть *НАЗВУ КНИГИ*", parse_mode='Markdown')
         return

    query_book_finder = book_name

    books = db.find_name(book_name, 0)

    markup_inline = types.InlineKeyboardMarkup()
    prev = types.InlineKeyboardButton(text='Prev', callback_data='book_finder_prev')
    next = types.InlineKeyboardButton(text='Next', callback_data='book_finder_next')
    markup_inline.add(prev, next)

    if counter < 0:
        counter = len(books) - 1
    if counter > len(books) - 1:
        counter = 0

    if len(books) > 0:
        bookBot.send_message(message.chat.id, "[" + str(counter+1) + "/" + str(books.__len__()) + "] "
                            + "Із списка знайдено такі книги: \n\n"
                            + books[counter].show_info(), reply_markup=markup_inline)
    else:
        bookBot.send_message(message.chat.id, "По вашому запиту нічого не знайдено!")




@bookBot.message_handler(commands=['author'])
def author_finder(message):

    global counter, books, query_book_finder

    author_name = str(message.text).replace("/author", "")
    author_name = author_name.lstrip()
    if author_name == "":
        bookBot.send_message(message.chat.id, "Введіть *НАЗВУ КНИГИ*", parse_mode='Markdown')
        return

    query_book_finder = author_name

    books = db.find_name(author_name, 1)

    markup_inline = types.InlineKeyboardMarkup()
    prev = types.InlineKeyboardButton(text='Prev', callback_data='book_finder_prev')
    next = types.InlineKeyboardButton(text='Next', callback_data='book_finder_next')
    markup_inline.add(prev, next)

    if counter < 0:
        counter = len(books) - 1
    if counter > len(books) - 1:
        counter = 0
    print(counter)
    bookBot.send_message(message.chat.id, "[" + str(counter + 1) + "/" + str(books.__len__()) + "] "
                         + "Із списка знайдено такі книги: \n\n"
                         + books[counter].show_info(), reply_markup=markup_inline)


@bookBot.message_handler(commands=['random'])
def random_finder(message):
    for book in db.take_random_book(1):
        bookBot.send_message(message.chat.id, book.show_info(), parse_mode='Markdown')

@bookBot.callback_query_handler(func=lambda call: True)
def finder_counter(call):
    global counter
    if call.data == 'book_finder_next':
        counter += 1
        call.message.text = query_book_finder
        book_finder(call.message)
    if call.data == 'book_finder_prev':
        counter -= 1
        call.message.text = query_book_finder
        book_finder(call.message)

def start_bot():
    bookBot.polling(none_stop=True, interval=0)
