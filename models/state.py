#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Getter attribute cities that returns the list of City"""
        from models import storage
        from models.city import City
        list = []
        all_city = storage.all(City)
        for city in all_city.values():
            if city.state_id == self.id:
                list.append(city)
        return list
