from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_parking_spots(db: Session):

    parking_spots_all = db.query(models.ParkingSpots).all()
    parking_spots_all = [new_data.to_dict() for new_data in parking_spots_all] if parking_spots_all else parking_spots_all

    res = {
        'parking_spots_all': parking_spots_all,
    }
    return res

async def get_parking_spots_id(db: Session, id: int):

    parking_spots_one = db.query(models.ParkingSpots).filter(models.ParkingSpots.id == id).first() 
    parking_spots_one = parking_spots_one.to_dict() if parking_spots_one else parking_spots_one

    res = {
        'parking_spots_one': parking_spots_one,
    }
    return res

async def post_parking_events(db: Session, raw_data: schemas.PostParkingEvents):
    id:int = raw_data.id
    vehicle_id:int = raw_data.vehicle_id
    parking_spot_id:int = raw_data.parking_spot_id
    start_time:str = raw_data.start_time
    end_time:str = raw_data.end_time


    record_to_be_added = {'id': id, 'end_time': end_time, 'start_time': start_time, 'vehicle_id': vehicle_id, 'parking_spot_id': parking_spot_id}
    new_parking_events = models.ParkingEvents(**record_to_be_added)
    db.add(new_parking_events)
    db.commit()
    db.refresh(new_parking_events)
    parking_events_inserted_record = new_parking_events.to_dict()


    delete_records = None
    record_to_delete = db.query(models.Vehicles).filter(models.Vehicles.license_plate == end_time).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        delete_records = record_to_delete.to_dict() 

    res = {
        'parking_events_inserted_record': parking_events_inserted_record,
        'delete_records': delete_records,
    }
    return res

async def post_parking_spots(db: Session, raw_data: schemas.PostParkingSpots):
    id:int = raw_data.id
    aisle:str = raw_data.aisle
    number:str = raw_data.number
    is_occupied:int = raw_data.is_occupied
    size_type:str = raw_data.size_type


    record_to_be_added = {'id': id, 'aisle': aisle, 'number': number, 'size_type': size_type, 'is_occupied': is_occupied}
    new_parking_spots = models.ParkingSpots(**record_to_be_added)
    db.add(new_parking_spots)
    db.commit()
    db.refresh(new_parking_spots)
    parking_spots_inserted_record = new_parking_spots.to_dict()

    res = {
        'parking_spots_inserted_record': parking_spots_inserted_record,
    }
    return res

async def put_parking_spots_id(db: Session, id: int, aisle: str, number: str, is_occupied: int, size_type: str):

    parking_spots_edited_record = db.query(models.ParkingSpots).filter(models.ParkingSpots.id == id).first()
    for key, value in {'id': id, 'aisle': aisle, 'number': number, 'size_type': size_type, 'is_occupied': is_occupied}.items():
          setattr(parking_spots_edited_record, key, value)
    db.commit()
    db.refresh(parking_spots_edited_record)
    parking_spots_edited_record = parking_spots_edited_record.to_dict() 

    res = {
        'parking_spots_edited_record': parking_spots_edited_record,
    }
    return res

async def delete_parking_spots_id(db: Session, id: int):

    parking_spots_deleted = None
    record_to_delete = db.query(models.ParkingSpots).filter(models.ParkingSpots.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        parking_spots_deleted = record_to_delete.to_dict() 

    res = {
        'parking_spots_deleted': parking_spots_deleted,
    }
    return res

async def get_vehicles(db: Session):

    vehicles_all = db.query(models.Vehicles).all()
    vehicles_all = [new_data.to_dict() for new_data in vehicles_all] if vehicles_all else vehicles_all

    res = {
        'vehicles_all': vehicles_all,
    }
    return res

async def get_vehicles_id(db: Session, id: int):

    vehicles_one = db.query(models.Vehicles).filter(models.Vehicles.id == id).first() 
    vehicles_one = vehicles_one.to_dict() if vehicles_one else vehicles_one

    res = {
        'vehicles_one': vehicles_one,
    }
    return res

async def post_vehicles(db: Session, raw_data: schemas.PostVehicles):
    id:int = raw_data.id
    license_plate:str = raw_data.license_plate
    make:str = raw_data.make
    model:str = raw_data.model


    record_to_be_added = {'id': id, 'make': make, 'model': model, 'license_plate': license_plate}
    new_vehicles = models.Vehicles(**record_to_be_added)
    db.add(new_vehicles)
    db.commit()
    db.refresh(new_vehicles)
    vehicles_inserted_record = new_vehicles.to_dict()

    res = {
        'vehicles_inserted_record': vehicles_inserted_record,
    }
    return res

async def put_vehicles_id(db: Session, id: int, license_plate: str, make: str, model: str):

    vehicles_edited_record = db.query(models.Vehicles).filter(models.Vehicles.id == id).first()
    for key, value in {'id': id, 'make': make, 'model': model, 'license_plate': license_plate}.items():
          setattr(vehicles_edited_record, key, value)
    db.commit()
    db.refresh(vehicles_edited_record)
    vehicles_edited_record = vehicles_edited_record.to_dict() 

    res = {
        'vehicles_edited_record': vehicles_edited_record,
    }
    return res

async def delete_vehicles_id(db: Session, id: int):

    vehicles_deleted = None
    record_to_delete = db.query(models.Vehicles).filter(models.Vehicles.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        vehicles_deleted = record_to_delete.to_dict() 

    res = {
        'vehicles_deleted': vehicles_deleted,
    }
    return res

async def get_parking_events(db: Session):

    parking_events_all = db.query(models.ParkingEvents).all()
    parking_events_all = [new_data.to_dict() for new_data in parking_events_all] if parking_events_all else parking_events_all

    res = {
        'parking_events_all': parking_events_all,
    }
    return res

async def get_parking_events_id(db: Session, id: int):

    parking_events_one = db.query(models.ParkingEvents).filter(models.ParkingEvents.id == id).first() 
    parking_events_one = parking_events_one.to_dict() if parking_events_one else parking_events_one

    res = {
        'parking_events_one': parking_events_one,
    }
    return res

async def put_parking_events_id(db: Session, id: int, vehicle_id: int, parking_spot_id: int, start_time: str, end_time: str):

    parking_events_edited_record = db.query(models.ParkingEvents).filter(models.ParkingEvents.id == id).first()
    for key, value in {'id': id, 'end_time': end_time, 'start_time': start_time, 'vehicle_id': vehicle_id, 'parking_spot_id': parking_spot_id}.items():
          setattr(parking_events_edited_record, key, value)
    db.commit()
    db.refresh(parking_events_edited_record)
    parking_events_edited_record = parking_events_edited_record.to_dict() 

    res = {
        'parking_events_edited_record': parking_events_edited_record,
    }
    return res

async def delete_parking_events_id(db: Session, id: int):

    parking_events_deleted = None
    record_to_delete = db.query(models.ParkingEvents).filter(models.ParkingEvents.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        parking_events_deleted = record_to_delete.to_dict() 

    res = {
        'parking_events_deleted': parking_events_deleted,
    }
    return res

