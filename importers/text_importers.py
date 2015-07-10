__author__ = 'dqin2'

import logging

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
            return [models.Person(*line.split(self._delimiter)) for line in data]
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
