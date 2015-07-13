__author__ = 'dqin2'

import unittest
import datetime

from reports.directory import Directory
from models import Person


class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.report = Directory()

    def test_load_single(self):
        self.report.load_single(',', 'Jack,Knife,Male,Pink,2000-Sep-20')
        session = self.report.get_session()
        results = session.query(Person).all()
        self.assertEqual(len(results), 1)
        p = results[0]
        self.assertEqual(p.first_name, 'Jack')
        self.assertEqual(p.last_name, 'Knife')
        self.assertEqual(p.gender, 'Male')
        self.assertEqual(p.favorite_color, 'Pink')
        self.assertEqual(p.date_of_birth, datetime.date(2000, 9, 20))

    def test_report_data(self):
        self.report.load_single(',', 'Jack,Ham,Male,Pink,2000-Sep-20')
        self.report.load_single(',', 'Jack,Knife,Male,Pink,2000-Sep-20')

        unordered_results = self.report.report_data()
        self.assertEqual(len(unordered_results), 2)
        self.assertEqual(unordered_results[0].last_name, 'Ham')
        self.assertEqual(unordered_results[1].last_name, 'Knife')

        ordered_results = self.report.report_data([('last_name', 'DESC')])
        self.assertEqual(len(ordered_results), 2)
        self.assertEqual(ordered_results[0].last_name, 'Knife')
        self.assertEqual(ordered_results[1].last_name, 'Ham')


if __name__ == '__main__':
    unittest.main()
