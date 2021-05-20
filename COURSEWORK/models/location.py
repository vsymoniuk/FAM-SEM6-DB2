from sqlalchemy import Column, String, Integer, Float
from db import Base


class Location(Base):
    __tablename__ = 'location'

    id_loc = Column(Integer, primary_key=True)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    def __init__(self, new):
        self.address = new["Address"]
        self.longitude = new["Longitude"]
        self.latitude = new["Latitude"]

    def __repr__(self):
        return f"<Details(address='{self.address}'," \
               f" longitude='{self.longitude}'," \
               f" latitude='{self.latitude}')>"