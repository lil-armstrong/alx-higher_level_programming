#!/usr/bin/python3
""" List relationship

lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy import (create_engine, MetaData)
from sqlalchemy.orm import (sessionmaker)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
        sys.argv[1], sys.argv[2], 3306, sys.argv[3]), pool_pre_ping=True)
    metadata = MetaData(bind=engine, schema=Base.metadata)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).\
            order_by(State.id):
        print("%s: %s" % (state.id, state.name))
        for city in state.cities:
            print("    ", end="")
            print("%s: %s" % (city.id, city.name))
