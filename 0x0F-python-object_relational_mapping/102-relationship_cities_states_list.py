#!/usr/bin/python3
""" List relationship

List all City objects from the database hbtn_0e_101_usa

"""
import sys
from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker, relationship)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
        sys.argv[1], sys.argv[2], 3306, sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).\
            all():

        print("%s: %s -> %s" % (city.id, city.name, city.state.name))
