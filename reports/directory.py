__author__ = 'dqin2'

import logging

import sqlalchemy

from sqlalchemy.orm import sessionmaker

from models import Person
from importers.text_importers import DelimtedTextImporter


class Directory(object):
    """
    Data storage for report, utilizes memory db
    """

    DATA_FILES = ['data/commas.txt',
                  'data/pipe.txt',
                  'data/space.txt']

    def __init__(self):
        self._db_engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

        # initialize data tables
        Person.metadata.create_all(self._db_engine)
        self._sessionmaker = sessionmaker(bind=self._db_engine)

    def get_session(self):
        return self._sessionmaker()

    def load_sample_data(self):
        """
        loads data for sample report

        :return:
        """
        session = self.get_session()

        try:
            # Load comma separated file
            session.add_all(DelimtedTextImporter(',').load('../data/comma.txt'))

            # Load pipe separated file
            session.add_all(DelimtedTextImporter('|').load('../data/pipe.txt'))

            # Load space separated file
            session.add_all(DelimtedTextImporter(' ').load('../data/space.txt'))

            session.commit()
        except Exception, ex:
            logging.exception(ex)
            raise ex

    def report1_data(self):
        return self.get_session().query(Person).order_by(Person.gender, Person.last_name).all()

    def report2_data(self):
        return self.get_session().query(Person).order_by(Person.date_of_birth).all()

    def report3_data(self):
        return self.get_session().query(Person).order_by(Person.last_name.desc()).all()
