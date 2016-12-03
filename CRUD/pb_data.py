# coding=utf-8

from pb_config import *
import pickle
import csv


def get_data_from_pickle_file(phone_book_db_file):
    with open(phone_book_db_file, 'rt') as f:
        phone_book_pickled = f.read()
    return pickle.loads(phone_book_pickled)


def update_pickle_file(phone_book_dict, phone_book_db_file):
    phone_book_pickled = pickle.dumps(phone_book_dict)
    with open(phone_book_db_file, 'wt') as f:
        f.write(phone_book_pickled)


def get_data_from_csv_file(phone_book_db_file):
    csv_dict = {}
    with open(phone_book_db_file, 'rb') as csvfile:
        phone_book_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in phone_book_csv:
            csv_dict[row[0]] = row[1]
    return csv_dict


def update_csv_file(phone_book_dict, phone_book_db_file):
    print "start update"
    with open(phone_book_db_file, 'wb') as csvfile:
        phone_book_csv = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for name in phone_book_dict:
            print name, phone_book_dict[name]
            phone_book_csv.writerow([name, phone_book_dict[name]])

if FILE_FORMAT == 'csv':
    get_data_from_dbfile = get_data_from_pickle_file
    update_db_file = update_pickle_file
elif FILE_FORMAT == 'pickle':
    get_data_from_dbfile = get_data_from_csv_file
    update_db_file = update_csv_file
else:
    print "Error in config"
    exit()