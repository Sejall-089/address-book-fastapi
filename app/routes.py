from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import get_db
from . import crud, schemas
from .logger import logger

router = APIRouter()


@router.post("/addresses", response_model=schemas.AddressResponse)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    logger.info("Creating address")
    return crud.create_address(db, address)


@router.get("/addresses", response_model=list[schemas.AddressResponse])
def get_addresses(db: Session = Depends(get_db)):
    return crud.get_all_addresses(db)


@router.put("/addresses/{address_id}")
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):

    updated = crud.update_address(db, address_id, address)

    if not updated:
        raise HTTPException(status_code=404, detail="Address not found")

    return updated


@router.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):

    deleted = crud.delete_address(db, address_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Address not found")

    return {"message": "Address deleted successfully"}


@router.get("/addresses/search")
def search_addresses(lat: float, lon: float, radius: float, db: Session = Depends(get_db)):
    logger.info("Searching addresses within radius")
    return crud.search_within_radius(db, lat, lon, radius)