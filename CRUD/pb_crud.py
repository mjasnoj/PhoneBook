# coding=utf-8

import pb_data
import pb_view
from pb_config import *


def start_phone_book():
    try:
        # phonebook = pb_data.get_data_from_dbfile(PHONE_BOOK_DB_FILE)
        phonebook = pb_data.get_data_from_csvfile(PHONE_BOOK_DB_FILE)
    except (EOFError, IOError):
        pb_view.message_to_user("Error loading data from file. Starting new phone_book.")
        phonebook = {}
    return phonebook


def save_changes(f):
    def wrapper(*args, **kwargs):
        pbch = f(*args, **kwargs)
        # pb_data.update_dbfile(phone_book, PHONE_BOOK_DB_FILE)
        pb_data.update_csvfile(phone_book, PHONE_BOOK_DB_FILE)
        return pbch
    return wrapper


@save_changes
def add_entry_to_phone_book(name, tel):
    if name in phone_book:
        raise ValueError('Such name already exists')
    phone_book[name] = tel


@save_changes
def del_entry_from_phone_book(name):
    if name not in phone_book:
        raise ValueError('No such entry in PhoneBook')
    del phone_book[name]


@save_changes
def update_phone_book(name, tel):
    phone_book[name] = tel


def list_phone_book():
    if not phone_book:
        pb_view.message_to_user("PhoneBook is empty")
    else:
        for name, number in phone_book.iteritems():
            pb_view.message_to_user("%s: %s" % (name, number))


def search_name_in_phone_book(name_to_search):
    if name_to_search in phone_book:
        pb_view.message_to_user("%s: %s" % (name_to_search, phone_book[name_to_search]))
        return True
    else:
        pb_view.message_to_user("no %s in PhoneBook" % name_to_search)
        return False


phone_book = start_phone_book()