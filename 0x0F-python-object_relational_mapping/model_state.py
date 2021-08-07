#!/usr/bin/python3
"""Module for the State class"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """Class represents the table for the states"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String)
