from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class CD(Base):
    __tablename__ = 'city_date'

    id_cd = Column(Integer, primary_key=True)
    date = Column(Date)
    id_det = Column(Integer, ForeignKey('details.id_det'))
    Details = relationship("Details", backref='city_date')
    id_loc = Column(Integer, ForeignKey('location.id_loc'))
    Location = relationship("Location", backref='city_date')

    def __init__(self, new):
        self.date = new["Date time"]
        self.id_det = new["id_det"]
        self.id_loc = new["id_loc"]

    def __repr__(self):
        return f"<Details(Date time='{self.date}'," \
               f" id_loc='{self.id_loc}'," \
               f" id_det='{self.id_det}')>"