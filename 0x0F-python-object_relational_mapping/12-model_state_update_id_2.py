#!/usr/bin/python3
"""Start link class to table in database."""
import sys
from model_state import Base, State
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
    # Query for data to update
    new_data = session.query(State).filter(State.id == 2).first()
    # Add new data to session APIDB
    new_data.name = "New Mexico"
    # Safe the new element to database
    session.commit()
    # Close connection
    session.close()
