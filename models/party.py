#!/usr/bin/python3

"""
This provides the class `Party`
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class Party(Base):
    """
    This class provides a maping to the table `party`
    """

    __tablename__ = 'party'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    partyid = Column(String(11), nullable=False)
    partyname = Column(String(11), nullable=False)