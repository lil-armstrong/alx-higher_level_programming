#!/usr/bin/python3
""" Start link class to table in database  """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
        sys.argv[1], sys.argv[2], 3306, sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).order_by(State.id).first()
    if first_state is not None:
        print("%d. %s" % (first_state.id, first_state.name))
    else:
        print("Nothing")