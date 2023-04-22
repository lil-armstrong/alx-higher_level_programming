#!/usr/bin/python3
""" City relationship

Create the State “California” with the City “San Francisco” from the\
    database hbtn_0e_100_usa

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

    # Create state
    california = State(name="California")
    california.cities.append(City(name="San Francisco"))

    session.add(california)
    session.commit()
