# coding: utf-8

import pb_view
import pb_db
import pb_contact
from settings import *


class PhoneBook(object):
    def __init__(self):
        self.phone_book_ser = pb_db.PhoneBookDB(FILE_FORMAT)
        try:
            self.phone_book_dict = self.phone_book_ser.get_data_from_file()
        except (EOFError, IOError):
            pb_view.message_to_user("Error loading data from file. Starting new phone_book.")
            self.phone_book_dict = {}

    def __repr__(self):
        pass

    def __iter__(self):
        for cn, ct in self.phone_book_dict.items():
            yield cn, ct

    def save_phone_book(f):
        def wrapper(self, *args, **kwargs):
            pbch = f(self, *args, **kwargs)
            self.phone_book_ser.update_file(self.phone_book_dict)
            return pbch
        return wrapper

    @save_phone_book
    def add_contact(self):
        cname = pb_view.get_data_from_user("add.name?")
        if self.check_contact(cname)[0]:
            pb_view.message_to_user("{} already exists".format(cname))
        else:
            ctel = pb_view.get_data_from_user("add.tel?")
            self.phone_book_dict[cname] = pb_contact.PhoneBookContact(cname, ctel)

    def search_contact(self):
        cname = pb_view.get_data_from_user("search.name?")
        if self.check_contact(cname)[0]:
            pb_view.message_to_user("{}:{}".format(cname, self.phone_book_dict[cname]))
        else:
            pb_view.message_to_user(self.check_contact(cname)[1])

    def list_contacts(self):
        pb_view.dict_to_user(self.phone_book_dict.copy())
        #pb_view.iter_to_user(self)

    def check_contact(self, cname):
        if cname in self.phone_book_dict:
            return True, "{} exists".format(cname)
        else:
            return False, "{} doesn't exist".format(cname)

    @save_phone_book
    def del_contact(self):
        cname = pb_view.get_data_from_user("delete.name?")
        if self.check_contact(cname)[0]:
            del self.phone_book_dict[cname]
            pb_view.message_to_user("{} deleted".format(cname))
        else:
            pb_view.message_to_user("No such entry in PhoneBook")

    @save_phone_book
    def update_contact(self):
        cname = pb_view.get_data_from_user("update.name?")
        if self.check_contact(cname)[0]:
            ctel = pb_view.get_data_from_user("update.tel?")
            self.phone_book_dict[cname] = ctel
            pb_view.message_to_user("{} updated".format(cname))
        else:
            pb_view.message_to_user("No such entry in PhoneBook")

    @staticmethod
    def default_method():
        pb_view.message_to_user("Bad command. Please input correct one!")