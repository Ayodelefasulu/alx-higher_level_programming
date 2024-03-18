#!/usr/bin/python3
"""Fetches and prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(
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

    # Query all City objects and print them sorted by city id
    """cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    """
    cities = session.query(City).join(State).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # Close the session
    session.close()
