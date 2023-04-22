#!/usr/bin/python3

""" Class definition of State """
from sqlalchemy import Column, Integer, String, MetaData, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import State, Base


class City(Base):
    """ City class """

    __tablename__ = "cities"
    id = Column(Integer, Sequence(name='city_id_seq'),
                primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship(State, back_populates="cities")

    def __repr__(self):
        """Nicely format City object"""
        return str("<City(name='%s')>" % (self.name))
