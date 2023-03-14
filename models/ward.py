#!/usr/bin/python3

"""
This provides the class `Ward`
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Text

Base = declarative_base()


class Ward(Base):
    """
    This class provides a maping to the table `ward`
    """

    __tablename__ = 'ward'
    uniqueid = Column(Integer, nullable=False,
                      autoincrement=True, primary_key=True)
    ward_id = Column(Integer, nullable=False)
    ward_name = Column(String(50), nullable=False)
    lga_id = Column(Integer, nullable=False)
    ward_description = Column(Text)
    entered_by_user = Column(String(50), default=None)
    date_entered = Column(DateTime, default=None)
    user_ip_address = Column(String(50), default=None)
