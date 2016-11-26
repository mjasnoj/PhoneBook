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
def add_entry_to_phonebook(name, tel):
    if name in phone_book:
        raise ValueError('Such name already exists')
    phone_book[name] = tel


@update_dbfile_dec
def del_entry_from_phonebook(name):
    if name not in phone_book:
        raise ValueError('No such entry in PhoneBook')
    del phone_book[name]


@update_dbfile_dec
def update_phone_book(name, tel):
    # phone_book.update({name: tel})
    phone_book[name] = tel


def search_name_in_phonebook(name):
    pass


def get_data_from_user(param):
    while True:
        name = raw_input(param).strip()
        if name:
            return name


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

commands = { 'add', 'del', 'upd', 'lst', 'exit', 'srch', 'help'}

while True:
    command = raw_input("?").strip()

    if command == 'add':
        print "add"
        name = get_data_from_user("name?")
        tel = get_data_from_user("tel?")
        try:
            add_entry_to_phonebook(name, tel)
            print "%s: %s added successfully." %(name, tel)
        except ValueError as e:
            print e
    elif command == 'del':
        print "del"
        name_to_delete = get_data_from_user("name?")
        try:
            del_entry_from_phonebook(name_to_delete)
            print "%s successfully deleted" % name_to_delete
        except ValueError as e:
            print e
    elif command == 'upd':
        print "upd"
        name_to_update = get_data_from_user("name")
        if name_to_update in phone_book:
            tel = get_data_from_user("tel?")
            update_phone_book(name_to_update, tel)
        else:
            print "%s not in PhoneBook" % name_to_update
    elif command == 'lst':
        print "lst"
        if not phone_book:
            print "PhoneBook is empty"
        else:
            for name, number in phone_book.iteritems():
                print "%s: %s" % (name, number)
    elif command == 'srch':
        print "srch"
        name_to_search = get_data_from_user("name?")
        if name_to_search in phone_book:
            print phone_book[name_to_search]
        else:
            print "no %s in PhoneBook" % name_to_search
    elif command == 'help':
        print HLP_MSG
    elif command == 'exit':
        print "Exit."
        update_dbfile(phone_book, PHONE_BOOK_DB_FILE)
        break
    else:
        print "Bad command. Please input correct one!"
