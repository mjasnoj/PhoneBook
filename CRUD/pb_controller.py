# coding=utf-8

import pb_crud
import pb_view
from pb_config import *


def pb_add():
    name = pb_view.get_data_from_user("add.name?")
    tel = pb_view.get_data_from_user("add.tel?")
    try:
        pb_crud.add_entry_to_phone_book(name, tel)
        pb_view.message_to_user("%s: %s added successfully." % (name, tel))
    except ValueError as e:
        pb_view.message_to_user(e)


def pb_del():
    name_to_delete = pb_view.get_data_from_user("del.name?")
    try:
        pb_crud.del_entry_from_phone_book(name_to_delete)
        pb_view.message_to_user("%s successfully deleted" % name_to_delete)
    except ValueError as e:
        pb_view.message_to_user(e)


def pb_upd():
    name_to_update = pb_view.get_data_from_user("upd.name?")
    if pb_crud.search_name_in_phone_book(name_to_update):
        tel = pb_view.get_data_from_user("upd.tel?")
        pb_crud.update_phone_book(name_to_update, tel)
    else:
        pb_view.message_to_user("Failed to update %s" % name_to_update)


def pb_lst():
    pb_crud.list_phone_book()


def pb_srch():
    name_to_search = pb_view.get_data_from_user("srch.name?")
    pb_crud.search_name_in_phone_book(name_to_search)


def pb_help():
    pb_view.message_to_user(HLP_MSG)


def pb_exit():
    pb_view.message_to_user("Exit.")
    exit()


def pb_default():
    pb_view.message_to_user("Bad command. Please input correct one!")

pb_view.message_to_user("Welcome to PhoneBook.")
pb_view.message_to_user(HLP_MSG)

commands = {'add':  pb_add,
            'del':  pb_del,
            'upd':  pb_upd,
            'lst':  pb_lst,
            'exit': pb_exit,
            'srch': pb_srch,
            'help': pb_help
            }

while True:
    commands.get(pb_view.get_data_from_user("?"), pb_default)()