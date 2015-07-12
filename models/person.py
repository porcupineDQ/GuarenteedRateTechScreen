__author__ = 'dqin2'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()


class Person(Base):
    """
    Person data type
    """
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    favorite_color = Column(String)
    date_of_birth = Column(Date)

    def __repr__(self):
        return '<Person ID="%s", First Name="%s", Last Name="%s", Gender="%s", Favorite Color="%s", Date of Birth="%s"' \
               % (self.id, self.first_name, self.last_name, self.gender, self.favorite_color, self.date_of_birth)

    def to_dict(self):
        return {
            'First Name': self.first_name,
            'Last Name': self.last_name,
            'Gender': self.gender,
            'Favorite Color': self.favorite_color,
            'Date of Birth': self.date_of_birth.isoformat()
        }
