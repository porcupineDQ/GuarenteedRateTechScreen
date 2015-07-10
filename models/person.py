__author__ = 'dqin2'

from datetime import datetime


class Person(object):
    """
    Person data type
    """

    def __init__(self, first_name, last_name, gender, favorite_color, date_of_birth):
        """
        Constructor

        :param first_name: str
        :param last_name: str
        :param gender: str
        :param favorite_color: str
        :param date_of_birth: str (YYYY-MMM-DD, i.e. 2010-Jan-01) or datetime.date
        :return: None
        """
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._favorite_color = favorite_color
        if isinstance(date_of_birth, str):
            self._date_of_birth = datetime.strptime(date_of_birth, '%Y-%b-%d').date()
        else:
            self._date_of_birth = date_of_birth

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def gender(self):
        return self._gender

    @property
    def favorite_color(self):
        return self._favorite_color

    @property
    def date_of_birth(self):
        return self._date_of_birth
