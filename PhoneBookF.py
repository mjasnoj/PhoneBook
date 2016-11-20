# coding=utf-8

def update_phone_book(name, tel):
    phone_book.update({name: tel})

def get_data_from_user(param):
    while True:
        value = raw_input(param+"?").strip()
        if value:
            break
        else:
            print "You entered empty string"
    return value

print """
Welcome to PhoneBook.
Available commands:
add - Add Contact
del - Delete Contact
upd - Update Contact
lst - List Contacts
exit - Exit from PhoneBook
"""

commands = ['add', 'del', 'upd', 'lst', 'exit']
phone_book = {}

while True:
    command = raw_input("?").strip()

    if command in commands:
        if command == 'add':
            print "add"
            name = get_data_from_user("name")
            tel = get_data_from_user("tel")
            update_phone_book(name, tel)
        elif command == 'del':
            print "del"
            name_to_delete = get_data_from_user("name")
            if name_to_delete in phone_book:
                del phone_book[name_to_delete]
                print "%s deleted from PhoneBook" % (name_to_delete)
            else:
                print "%s not in PhoneBook" % (name_to_delete)
        elif command == 'upd':
            print "upd"
            name_to_update = get_data_from_user("name")
            if name_to_update in phone_book:
                tel = get_data_from_user("tel")
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
        else:
            print "Exit."
            break
    else:
        print "Bad command. Please input correct one!"
        continue
