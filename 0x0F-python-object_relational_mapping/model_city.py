#!/usr/bin/python3
"""Defines the City class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """City class that inherits from Base"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Define the relationship between City and State
    state = relationship("State", back_populates="cities")

    def __repr__(self):
        """Return string representation of City object"""
        return "<City(id={}, name='{}', state_id={})>".format(
            self.id, self.name, self.state_id)
