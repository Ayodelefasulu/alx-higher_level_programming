#!/usr/bin/python3
"""Add an object to the State with the specified name to the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Database connection details
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database_name))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert object to database table
    state_object = State(name="Louisiana")
    session.add(state_object)
    session.commit()  # Commit changes

    if state_object:
        print(state_object.id)

    # Close connection
    session.close()
