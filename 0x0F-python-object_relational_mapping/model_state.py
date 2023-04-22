#!/usr/bin/python3

""" Class definition of State """
from sqlalchemy import Column, Integer, String, MetaData, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """ State class """

    __tablename__ = "states"
    id = Column(Integer, Sequence(name='state_id_seq'),
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates='state')

    def __repr__(self):
        """Nicely format State object"""
        return "<State(name='%s')>" % (self.name)
