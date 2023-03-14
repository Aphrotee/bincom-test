#!/usr/bin/python3

"""
This provides the class `PollingUnit`
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Text

Base = declarative_base()


class PollingUnit(Base):
    """
    This class provides a maping to the table `polling_unit`
    """

    __tablename__ = 'polling_unit'
    uniqueid = Column(Integer, nullable=False,
                      autoincrement=True, primary_key=True)
    polling_unit_id = Column(Integer, nullable=False)
    ward_id = Column(Integer, nullable=False)
    lga_id = Column(Integer, nullable=False)
    uniquewardid = Column(Integer, default=None)
    polling_unit_number = Column(String(50), default=None)
    polling_unit_name = Column(String(50), default=None)
    polling_unit_description = Column(Text)
    lat = Column(String(255), default=None)
    long = Column(String(255), default=None)
    entered_by_user = Column(String(50), default=None)
    date_entered = Column(DateTime, default=None)
    user_ip_address = Column(String(50), default=None)
