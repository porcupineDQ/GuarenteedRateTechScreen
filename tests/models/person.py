__author__ = 'dqin2'

import unittest
import datetime

from models import Person


class TestPerson(unittest.TestCase):
    def test_to_dict(self):
        p = Person(first_name='First',
                   last_name='Last',
                   gender='Male',
                   favorite_color='Color',
                   date_of_birth=datetime.date(1990, 1, 1))

        expected = {'Last Name': 'Last',
                    'First Name': 'First',
                    'Favorite Color': 'Color',
                    'Date of Birth': '1990-01-01',
                    'Gender': 'Male'}
        self.assertDictEqual(p.to_dict(), expected, 'Mismatch between expected and result')
