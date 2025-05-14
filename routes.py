from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/parking_spots/')
async def get_parking_spots(db: Session = Depends(get_db)):
    try:
        return await service.get_parking_spots(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_spots/id')
async def get_parking_spots_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parking_spots_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking_events/')
async def post_parking_events(raw_data: schemas.PostParkingEvents, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_events(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking_spots/')
async def post_parking_spots(raw_data: schemas.PostParkingSpots, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_spots(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/parking_spots/id/')
async def put_parking_spots_id(id: int, aisle: str, number: str, is_occupied: int, size_type: str, db: Session = Depends(get_db)):
    try:
        return await service.put_parking_spots_id(db, id, aisle, number, is_occupied, size_type)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/parking_spots/id')
async def delete_parking_spots_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_parking_spots_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/vehicles/')
async def get_vehicles(db: Session = Depends(get_db)):
    try:
        return await service.get_vehicles(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/vehicles/id')
async def get_vehicles_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_vehicles_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/vehicles/')
async def post_vehicles(raw_data: schemas.PostVehicles, db: Session = Depends(get_db)):
    try:
        return await service.post_vehicles(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/vehicles/id/')
async def put_vehicles_id(id: int, license_plate: str, make: str, model: str, db: Session = Depends(get_db)):
    try:
        return await service.put_vehicles_id(db, id, license_plate, make, model)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/vehicles/id')
async def delete_vehicles_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_vehicles_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_events/')
async def get_parking_events(db: Session = Depends(get_db)):
    try:
        return await service.get_parking_events(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_events/id')
async def get_parking_events_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parking_events_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/parking_events/id/')
async def put_parking_events_id(id: int, vehicle_id: int, parking_spot_id: int, start_time: str, end_time: str, db: Session = Depends(get_db)):
    try:
        return await service.put_parking_events_id(db, id, vehicle_id, parking_spot_id, start_time, end_time)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/parking_events/id')
async def delete_parking_events_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_parking_events_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

