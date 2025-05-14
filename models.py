from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class ParkingSpots(Base):
    __tablename__ = 'parking_spots'
    id = Column(String, primary_key=True)
    aisle = Column(String, primary_key=False)
    number = Column(String, primary_key=False)
    is_occupied = Column(Integer, primary_key=False)
    size_type = Column(String, primary_key=False)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(String, primary_key=True)
    license_plate = Column(String, primary_key=False)
    make = Column(String, primary_key=False)
    model = Column(String, primary_key=False)


class ParkingEvents(Base):
    __tablename__ = 'parking_events'
    id = Column(String, primary_key=True)
    vehicle_id = Column(Integer, primary_key=False)
    parking_spot_id = Column(Integer, primary_key=False)
    start_time = Column(String, primary_key=False)
    end_time = Column(String, primary_key=False)


