__author__ = 'dqin2'

import unittest
import datetime

import mock

import importers.text_importers


class TestDelimtedTextImporter(unittest.TestCase):
    def setUp(self):
        self.data = ['Bob|Smith|Male|Blue|1980-Jan-01']

    def test_parse(self):
        results = importers.text_importers.DelimtedTextImporter('|').parse(self.data)

        self.assertEqual(len(results), 1, 'Only expected 1 record')
        self.assertEqual(results[0].first_name, 'Bob')
        self.assertEqual(results[0].last_name, 'Smith')
        self.assertEqual(results[0].gender, 'Male')
        self.assertEqual(results[0].favorite_color, 'Blue')
        self.assertEqual(results[0].date_of_birth, datetime.date(1980, 1, 1))

    def test_load(self):
        my_mock = mock.MagicMock()
        with mock.patch('__builtin__.open', my_mock):
            manager = my_mock.return_value.__enter__.return_value
            manager.readlines.return_value = self.data
            with open('foo') as h:
                results = importers.text_importers.DelimtedTextImporter('|').load(None)

        self.assertEqual(len(results), 1, 'Only expected 1 record')
        self.assertEqual(results[0].first_name, 'Bob')
        self.assertEqual(results[0].last_name, 'Smith')
        self.assertEqual(results[0].gender, 'Male')
        self.assertEqual(results[0].favorite_color, 'Blue')
        self.assertEqual(results[0].date_of_birth, datetime.date(1980, 1, 1))


if __name__ == '__main__':
    unittest.main()
