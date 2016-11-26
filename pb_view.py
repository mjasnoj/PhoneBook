# coding=utf-8


def get_data_from_user(param):
    while True:
        name = raw_input(param).strip()
        if name:
            return name


def message_to_user(param):
    print param
