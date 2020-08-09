#!/usr/bin/python3
"""Start link class to table in database."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # engine Creation APIDB
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Session for make a queries to db
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query to bd(argv[3]) for join table State and City
    state = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()
    # Travel list of tuples for print resul query
    for i, j in state:
        print("{}: ({}) {}".format(i.name, j.id, j.name))
    # Close connection to database
    session.close()
