__author__ = 'dqin2'

import logging
import datetime

import models


class DelimtedTextImporter(object):
    def __init__(self, delimiter):
        self._delimiter = delimiter

    def parse(self, data):
        """
        Parse data and return list of Person objects

        :param data: list of strings
        :return: list of Person
        """

        try:
            results = []
            for line in data:
                f_name, l_name, gender, color, dob = line.strip().split(self._delimiter)
                try:
                    dob = datetime.datetime.strptime(dob, '%Y-%b-%d').date()
                except:
                    print "(%s)" % dob
                    raise

                results.append(models.Person(first_name=f_name,
                                             last_name=l_name,
                                             gender=gender,
                                             favorite_color=color,
                                             date_of_birth=dob))

            return results
        except ValueError, ex:
            logging.exception(ex)
            raise ValueError('Invalid input data')

    def load(self, file_path):
        """
        Loads a file and parses the contents

        :param file_path: str
        :return: list of Person
        """
        with open(file_path, 'r') as handle:
            data = handle.readlines()

        return self.parse(data)
