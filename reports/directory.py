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

    def __init__(self, verbose=False):
        self._db_engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=verbose)

        # initialize data tables
        Person.metadata.create_all(self._db_engine)
        self._sessionmaker = sessionmaker(bind=self._db_engine)

    def load_single(self, delimiter, value):
        session = self.get_session()
        result = DelimtedTextImporter(delimiter).parse([value])
        session.add_all(result)
        session.commit()

    def get_session(self):
        return self._sessionmaker()

    def load_sample_data(self):
        """
        loads data for sample report, TODO, move this function elsewhere, to a bootstrap class or something

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

    def report_data(self, order_by=None):
        """
        Returns all results using an order by as passed in

        :param order_by: list of columns with sort type e.g. [('gender','ASC'), ('date_of_birth','DESC')]
        :return: Ordered list of data
        """
        if not order_by:
            return self.get_session().query(Person).all()
        else:
            return self.get_session().query(Person).order_by(
                *[getattr(getattr(Person, attrib), 'desc' if order == 'DESC' else 'asc')()
                  for attrib, order in order_by if hasattr(Person, attrib)]
            ).all()

    def report1_data(self):
        return self.report_data(order_by=[('gender', 'ASC'), ('last_name', 'ASC')])

    def report2_data(self):
        return self.report_data(order_by=[('date_of_birth', 'ASC')])

    def report3_data(self):
        return self.report_data(order_by=[('last_name', 'DESC')])


if __name__ == '__main__':
    d = Directory()
    d.load_single(',', 'Foo,Bar,Male,Pink,2000-Sep-20')
