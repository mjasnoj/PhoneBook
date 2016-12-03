# coding: utf-8


class PhoneBookContact(object):
    def __init__(self, cname, ctel):
        self.name = cname
        self.tel = ctel

    def __repr__(self):
        return "{}: {}".format(self.name, self.tel)

    def get_contact(self):
        return self.name, self.tel

    def update_contact(self, cname, ctel):
        self.name = cname
        self.tel = ctel


