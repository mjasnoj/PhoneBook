# coding=utf-8

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
            while True:
                name = raw_input("name?").strip()
                if name:
                    break
                else:
                    print "You entered empty string"
            while True:
                tel = raw_input("tel?").strip()
                if tel:
                    break
                else:
                    print "You entered empty string"
            phone_book.update({name: tel})
        elif command == 'del':
            print "del"
            while True:
                name_to_delete = raw_input("name?").strip()
                if name:
                    if name in phone_book:
                        del phone_book[name]
                        print "%s deleted from PhoneBook" % (name)
                    else:
                        print "%s not in PhoneBook" % (name)
                    break
                else:
                    print "You entered empty string"
            pass
        elif command == 'upd':
            print "upd"
            pass
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
