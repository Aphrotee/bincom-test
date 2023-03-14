#!/usr/bin/python3

"""
This provides the class `PollingUnit`
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, CHAR

Base = declarative_base()


class AnnouncedPUResults(Base):
    """
    This class provides a mapping to the table `polling_unit`
    """

    __tablename__ = 'announced_pu_results'
    result_id = Column(Integer, nullable=False,
                       autoincrement=True, primary_key=True)
    polling_unit_uniqueid = Column(String(50), nullable=False)
    party_abbreviation = Column(CHAR(4))
    party_score = Column(Integer, nullable=False)
    entered_by_user = Column(String(50), default=None)
    date_entered = Column(DateTime, default=None)
    user_ip_address = Column(String(50), default=None)
