#!/usr/bin/python3
"""Delete all State objects with name containing letter 'a' from database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(
            sys.argv[0]))
        sys.exit(1)

    # Database connection details
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, dbname))

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects with a name containing 'a' and delete them
    states_to_del = session.query(State).filter(State.name.like('%a%')).all()
    if states_to_del:
        for state in states_to_del:
            session.delete(state)
        session.commit()
        print("States deleted successfully")
    else:
        print("No State objects with a name containing 'a' found")

    # Close the session
    session.close()
