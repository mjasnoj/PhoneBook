# coding=utf-8


def add_entry_to_phonebook(name, tel):
    if name in phone_book:
        raise ValueError('Such name already exists')
    phone_book[name] = tel


def update_phone_book(name, tel):
    # phone_book.update({name: tel})
    phone_book[name] = tel


def del_entry_from_phonebook(name):
    if name not in phone_book:
        raise ValueError('No such entry in PhoneBook')
    del phone_book[name]


def get_data_from_user(param):
    while True:
        name = raw_input(param).strip()
        if name:
            return name


print "Welcome to PhoneBook."

hlp_msg="""
Available commands:
add - Add Contact
del - Delete Contact
upd - Update Contact
lst - List Contacts
srch - search by name
help - print this message
exit - Exit from PhoneBook

"""

print hlp_msg

commands = ['add', 'del', 'upd', 'lst', 'exit', 'srch', 'help']
phone_book = {}

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
            print "%s successfully deleted" % (name_to_delete)
        except ValueError as e:
            print e
    elif command == 'upd':
        print "upd"
        name_to_update = get_data_from_user("name")
        if name_to_update in phone_book:
            tel = get_data_from_user("tel?")
            update_phone_book(name, tel)
        else:
            print "%s not in PhoneBook" % (name_to_update)
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
            print "no %s in PhoneBook" % (name_to_search)
    elif command == 'help':
        print hlp_msg
    elif command == 'exit':
        print "Exit."
        break
    else:
        print "Bad command. Please input correct one!"
