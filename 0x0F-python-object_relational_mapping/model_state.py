#!/usr/bin/env python3
"""class definition for state model"""

import sqlalchemy
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """states model"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
