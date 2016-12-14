# coding: utf-8
from settings import *
import pickle
import csv
import pb_contact
import MySQLdb


class PhoneBookDB(object):
    def __new__(cls, db):
        if db == 'csv':
            return PhoneBookDBCSV()
        elif db == 'pickle':
            return PhoneBookDBPickle()
        elif db == 'mysql':
            return PhoneBookDBMySQL()
        else:
            return PhoneBookDBPickle()


class PhoneBookDBBasic(object):
    def __init__(self, phone_book_db_file=PHONE_BOOK_DB_FILE):
        self.phone_book_db_file = phone_book_db_file


class PhoneBookDBPickle(PhoneBookDBBasic):
    def get_data_from_file(self):
        with open(self.phone_book_db_file, 'rt') as f:
            phone_book_pickled = f.read()
        return pickle.loads(phone_book_pickled)

    def update_file(self, phone_book_dict):
        phone_book_pickled = pickle.dumps(phone_book_dict)
        with open(self.phone_book_db_file, 'wt') as f:
            f.write(phone_book_pickled)


class PhoneBookDBCSV(PhoneBookDBBasic):
    def get_data_from_file(self):
        csv_dict = {}
        with open(self.phone_book_db_file, 'rb') as csvfile:
            phone_book_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in phone_book_csv:
                csv_dict[row[0]] = pb_contact.PhoneBookContact(*row)
        return csv_dict

    def update_file(self, phone_book_dict):
        print "start update"
        with open(self.phone_book_db_file, 'wb') as csvfile:
            phone_book_csv = csv.writer(csvfile, delimiter=',',
                                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for name in phone_book_dict:
                print phone_book_dict[name].get_contact()
                phone_book_csv.writerow(phone_book_dict[name].get_contact())


class PhoneBookDBMySQL(PhoneBookDBBasic):
    con = MySQLdb.connect(user='root', passwd='root', db='PB')

    def __init__(self):
        self.cursor = PhoneBookDBMySQL.con.cursor()

    def get_data_from_file(self):
        print "List"
        self.cursor = PhoneBookDBMySQL.con.cursor()
        self.cursor.execute("select * from PhoneBook")
        for row in self.cursor:
            print row

    def update_file(self, phone_book_db_file):
        pass

    def new_phone_book(self):
        self.cursor.execute(
            "CREATE TABLE PhoneBook (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20), tel VARCHAR(20)) "
        )

    def check_phone_book(self):
        print "check"
        self.cursor.execute(
            "SELECT count(*) FROM information_schema.TABLES WHERE TABLE_NAME = 'PhoneBook'"
        )
        if int(self.cursor.fetchone()[0]) == 1:
            return True
        else:
            return False

