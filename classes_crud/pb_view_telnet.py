# coding: utf-8
import socket


def get_data_from_user(param):
    global child
    while True:
        telnet_write(child, param)
        name = telnet_read(child).strip()
        print name
        if name:
            return name


def message_to_user(param):
    global child
    print param
    telnet_write(child, param)


def dict_to_user(pb_dict):
    if not pb_dict:
        message_to_user("PhoneBook is empty")
    else:
        for name in pb_dict:
            message_to_user(str(pb_dict[name]) + "\n")


def iter_to_user(a):
    for row in a:
        print row


def telnet_read(c):
    data = c.recv(1024)
    print data
    return data


def telnet_write(c, user_content):
    print user_content
    c.sendall(user_content)


s = socket.socket()
s.bind(('127.0.0.1', 8004))
s.listen(5)
print "Server started"

child, a = s.accept()
print "Connected ", a
