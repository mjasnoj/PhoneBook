# coding=utf-8

print """
Welcome to PhoneBook
add - Add Contact
del - Delete Contact
upd - Update Contact
lst - List Contacts
"""

commands = ['add', 'del', 'upd', 'lst']
phone_book = {}

while True:
    command = raw_input("?")

    if command in commands:
        pass
    else:
        print "error"
        break

