import datetime
import unittest

import models

__author__ = 'dqin2'


class Person(unittest.TestCase):
    """
    Unit test for Person
    """

    def setUp(self):
        """
        Set up method

        :return: None
        """
        self.last_name = 'Bar'
        self.first_name = 'Foo'
        self.gender = 'Male'
        self.favorite_color = 'Black'
        self.dob = datetime.date(2000, 1, 1)

        self.person = models.Person(self.first_name, self.last_name, self.gender, self.favorite_color, self.dob)

    def test_constructor_date_parse(self):
        person = models.Person(self.first_name,
                               self.last_name,
                               self.gender,
                               self.favorite_color,
                               self.dob.strftime('%Y-%b-%d'))

        self.assertEquals(self.person.date_of_birth, self.dob,
                          "DoB incorrect, expected %s, got %s" % (self.dob, self.person.date_of_birth))

    def test_properties(self):
        """
        Ensure properties are set correctly

        :return: None
        """
        self.assertEquals(self.person.last_name, self.last_name,
                          "Last name incorrect, expected %s, got %s" % (self.last_name, self.person.last_name))
        self.assertEquals(self.person.first_name, self.first_name,
                          "First name incorrect, expected %s, got %s" % (self.first_name, self.person.first_name))
        self.assertEquals(self.person.gender, self.gender,
                          "Gender incorrect, expected %s, got %s" % (self.gender, self.person.gender))
        self.assertEquals(self.person.favorite_color, self.favorite_color,
                          "Color incorrect, expected %s, got %s" % (self.favorite_color, self.person.favorite_color))
        self.assertEquals(self.person.date_of_birth, self.dob,
                          "DoB incorrect, expected %s, got %s" % (self.dob, self.person.date_of_birth))


if __name__ == '__main__':
    unittest.main()
