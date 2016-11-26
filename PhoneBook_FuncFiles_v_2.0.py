# coding=utf-8
import pickle


def get_data_from_dbfile(phone_book_db_file):
    with open(phone_book_db_file, 'rt') as f:
        phone_book_pickled = f.read()
    return pickle.loads(phone_book_pickled)


def update_dbfile(phone_book_dict, phone_book_db_file):
    phone_book_pickled = pickle.dumps(phone_book_dict)
    with open(phone_book_db_file, 'wt') as f:
        f.write(phone_book_pickled)


def update_dbfile_dec(f):
    def wrapper(*args, **kwargs):
        pbch = f(*args, **kwargs)
        update_dbfile(phone_book, PHONE_BOOK_DB_FILE)
        return pbch
    return wrapper


@update_dbfile_dec
def add_entry_to_phone_book(name, tel):
    if name in phone_book:
        raise ValueError('Such name already exists')
    phone_book[name] = tel


@update_dbfile_dec
def del_entry_from_phone_book(name):
    if name not in phone_book:
        raise ValueError('No such entry in PhoneBook')
    del phone_book[name]


@update_dbfile_dec
def update_phone_book(name, tel):
    # phone_book.update({name: tel})
    phone_book[name] = tel


def search_name_in_phone_book(name):
    pass


def get_data_from_user(param):
    while True:
        name = raw_input(param).strip()
        if name:
            return name


def pb_add():
    print "add"
    name = get_data_from_user("name?")
    tel = get_data_from_user("tel?")
    try:
        add_entry_to_phone_book(name, tel)
        print "%s: %s added successfully." % (name, tel)
    except ValueError as e:
        print e


def pb_del():
    print "del"
    name_to_delete = get_data_from_user("name?")
    try:
        del_entry_from_phone_book(name_to_delete)
        print "%s successfully deleted" % name_to_delete
    except ValueError as e:
        print e


def pb_upd():
    print "upd"
    name_to_update = get_data_from_user("name")
    if name_to_update in phone_book:
        tel = get_data_from_user("tel?")
        update_phone_book(name_to_update, tel)
    else:
        print "%s not in PhoneBook" % name_to_update


def pb_lst():
    print "lst"
    if not phone_book:
        print "PhoneBook is empty"
    else:
        for name, number in phone_book.iteritems():
            print "%s: %s" % (name, number)


def pb_srch():
    print "srch"
    name_to_search = get_data_from_user("name?")
    if name_to_search in phone_book:
        print phone_book[name_to_search]
    else:
        print "no %s in PhoneBook" % name_to_search


def pb_help():
    print HLP_MSG


def pb_exit():
    print "Exit."
    update_dbfile(phone_book, PHONE_BOOK_DB_FILE)
    exit()


def pb_default():
    print "Bad command. Please input correct one!"

print "Welcome to PhoneBook."

HLP_MSG="""
Available commands:
add  - Add Contact
del  - Delete Contact
upd  - Update Contact
lst  - List Contacts
srch - search by name
help - print this message
exit - Exit from PhoneBook.
"""

PHONE_BOOK_DB_FILE='phone_book_db.pickle'

try:
    phone_book = get_data_from_dbfile(PHONE_BOOK_DB_FILE)
except (EOFError, IOError) as e:
    print "Error loading data from file. Starting new phone_book."
    phone_book = {}

print HLP_MSG

commands = {'add':  pb_add,
            'del':  pb_del,
            'upd':  pb_upd,
            'lst':  pb_lst,
            'exit': pb_exit,
            'srch': pb_srch,
            'help': pb_help
            }

while True:
    commands.get(raw_input("?").strip(), pb_default)()

