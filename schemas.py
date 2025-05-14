from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class ParkingSpots(BaseModel):
    id: Any
    aisle: str
    number: str
    is_occupied: int
    size_type: str


class ReadParkingSpots(BaseModel):
    id: Any
    aisle: str
    number: str
    is_occupied: int
    size_type: str
    class Config:
        from_attributes = True


class Vehicles(BaseModel):
    id: Any
    license_plate: str
    make: str
    model: str


class ReadVehicles(BaseModel):
    id: Any
    license_plate: str
    make: str
    model: str
    class Config:
        from_attributes = True


class ParkingEvents(BaseModel):
    id: Any
    vehicle_id: int
    parking_spot_id: int
    start_time: Any
    end_time: Any


class ReadParkingEvents(BaseModel):
    id: Any
    vehicle_id: int
    parking_spot_id: int
    start_time: Any
    end_time: Any
    class Config:
        from_attributes = True




class PostParkingEvents(BaseModel):
    id: int
    vehicle_id: int
    parking_spot_id: int
    start_time: str
    end_time: str

    class Config:
        from_attributes = True



class PostParkingSpots(BaseModel):
    id: int
    aisle: str
    number: str
    is_occupied: int
    size_type: str

    class Config:
        from_attributes = True



class PostVehicles(BaseModel):
    id: int
    license_plate: str
    make: str
    model: str

    class Config:
        from_attributes = True

