from sqlalchemy import Column, String, Integer, Date, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from db import Base


class Details(Base):
    __tablename__ = 'details'

    id_det = Column(Integer, primary_key=True)
    min_tem = Column(Float)
    max_tem = Column(Float)
    wind_speed = Column(Float)
    wind_dir = Column(Float)
    dew_point = Column(Float)
    precipitation = Column(Float)
    visibility = Column(Float)
    conditions = Column(String)
    could_cov = Column(Float)
    relative_hum = Column(Float)

    def __init__(self, new):
        if new["Minimum Temperature"] == '':
            new["Minimum Temperature"] = '0.0'
        self.min_tem = new["Minimum Temperature"]

        if new["Maximum Temperature"] == '':
            new["Maximum Temperature"] = '0.0'
        self.max_tem = new["Maximum Temperature"]

        if new["Wind Speed"] == '':
            new["Wind Speed"] = '0.0'
        self.wind_speed = new["Wind Speed"]

        if new["Wind Direction"] == '':
            new["Wind Direction"] = '0.0'
        self.wind_dir = new["Wind Direction"]

        if new["Dew Point"] == '':
            new["Dew Point"] = '0.0'
        self.dew_point = new["Dew Point"]

        if new["Precipitation"] == '':
            new["Precipitation"] = '0.0'
        self.precipitation = new["Precipitation"]

        if new["Visibility"] == '':
            new["Visibility"] = '0.0'
        self.visibility = new["Visibility"]

        if new["Conditions"] == '':
            new["Conditions"] = 'unknow'
        self.conditions = new["Conditions"]

        if new["Cloud Cover"] == '':
            new["Cloud Cover"] = '0.0'
        self.could_cov = new["Cloud Cover"]

        if new["Relative Humidity"] == '':
            new["Relative Humidity"] = '0.0'
        self.relative_hum = new["Relative Humidity"]

    def __repr__(self):
        return f"<Details(min_tem='{self.min_tem}'," \
               f" max_tem='{self.max_tem}'," \
               f" wind_speed='{self.wind_speed}'," \
               f" wind_dir='{self.wind_dir}',"\
               f" dew_point='{self.dew_point}'," \
               f" precipitation='{self.precipitation}'," \
               f" visibility='{self.visibility}'," \
               f" conditions='{self.conditions}'," \
               f" could_cov='{self.could_cov}'," \
               f" relative_hum='{self.relative_hum}')>"