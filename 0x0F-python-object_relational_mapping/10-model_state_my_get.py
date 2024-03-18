#!/usr/bin/python3
"""Print the ID of the State object with the specified name from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database_n> <state_n>".format(
            sys.argv[0]))
        sys.exit(1)

    # Database connection details
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, dbname))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with specified name
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
