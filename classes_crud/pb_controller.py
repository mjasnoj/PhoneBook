# coding: utf-8

#import pb_view
import pb_view_telnet as pb_view
import pb_phone_book
from settings import *


def pb_exit():
    pb_view.message_to_user("Exit.")
    exit()


def pb_help():
    pb_view.message_to_user(HLP_MSG)

pb_view.message_to_user("Welcome to PhoneBook.")
pb_view.message_to_user(HLP_MSG)

new_book = pb_phone_book.PhoneBook()

COMMANDS = {'add':  new_book.add_contact,
            'del':  new_book.del_contact,
            'upd':  new_book.update_contact,
            'lst':  new_book.list_contacts,
            'exit': pb_exit,
            'srch': new_book.search_contact,
            'help': pb_help
            }

while True:
    COMMANDS.get(pb_view.get_data_from_user("?"), pb_phone_book.PhoneBook.default_method)()