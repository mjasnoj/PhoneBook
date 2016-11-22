def get_data_from_user(param):
    while True:
        value = raw_input(param).strip()
        if not value:
            raise ValueError('You entered empty string')
        return value

try:
    name = get_data_from_user("")
    print name
except ValueError as e:
    print e