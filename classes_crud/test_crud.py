# coding: utf-8

import unittest
import mock
from pb_phone_book import PhoneBook


class TestNumber(unittest.TestCase):
    def setUp(self):
        self.n = PhoneBook()

    @mock.patch('pb_view.get_data_from_user')
    @mock.patch('pb_view.message_to_user')
    def test_search1(self, f1, f2):
        f2.side_effect = ['dada']
        self.n.search_contact()
        f1.assert_called_once_with("dada doesn't exist")

    @mock.patch('pb_view.get_data_from_user')
    @mock.patch('pb_view.message_to_user')
    def test_search2(self, f1, f2):
        f2.side_effect = ['dadad']
        self.n.search_contact()
        f1.assert_called_once_with("dada doesn't exist")

    def tearDown(self):
        print "tearDown"
