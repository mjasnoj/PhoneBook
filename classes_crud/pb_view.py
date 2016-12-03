# coding: utf-8


def get_data_from_user(param):
    while True:
        name = raw_input(param).strip()
        if name:
            return name


def message_to_user(param):
    print param


def dict_to_user(pb_dict):
    if not pb_dict:
        message_to_user("PhoneBook is empty")
    else:
        for name in pb_dict:
            message_to_user(pb_dict[name])


def iter_to_user(a):
    for row in a:
        print row
