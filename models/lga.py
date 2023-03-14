#!/usr/bin/python3

"""
This provides the class `LGA`
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Text

Base = declarative_base()


class LGA(Base):
    """
    This class provides a maping to the table `lga`
    """

    __tablename__ = 'lga'
    uniqueid = Column(Integer, nullable=False,
                      autoincrement=True, primary_key=True)
    lga_id = Column(Integer, nullable=False)
    lga_name = Column(String(50), nullable=False)
    state_id = Column(Integer, nullable=False)
    lga_description = Column(Text)
    entered_by_user = Column(String(50), default=None)
    date_entered = Column(DateTime, default=None)
    user_ip_address = Column(String(50), default=None)
