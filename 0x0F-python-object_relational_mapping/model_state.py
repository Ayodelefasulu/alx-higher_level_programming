#!/usr/bin/python3
"""Defines the State class linked to the states table
    in the hbtn_0e_6_usa database."""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for the states table."""
    __tablename__ = "states"  # links the class to the table states

    # defines the columns for the table
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


"""
if __name__ == "__main__":
    # Create the engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create all tables defined in the metadata
    Base.metadata.create_all(engine)
"""
