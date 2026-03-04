from sqlalchemy.orm import Session
from geopy.distance import geodesic
from . import models, schemas


def create_address(db: Session, address: schemas.AddressCreate):
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def get_all_addresses(db: Session):
    return db.query(models.Address).all()


def update_address(db: Session, address_id: int, address: schemas.AddressUpdate):
    db_address = db.query(models.Address).filter(models.Address.id == address_id).first()

    if not db_address:
        return None

    for key, value in address.dict().items():
        setattr(db_address, key, value)

    db.commit()
    db.refresh(db_address)

    return db_address


def delete_address(db: Session, address_id: int):
    db_address = db.query(models.Address).filter(models.Address.id == address_id).first()

    if not db_address:
        return None

    db.delete(db_address)
    db.commit()

    return db_address


def search_within_radius(db: Session, lat: float, lon: float, radius: float):
    addresses = db.query(models.Address).all()
    result = []

    for addr in addresses:
        distance = geodesic((lat, lon), (addr.latitude, addr.longitude)).km

        if distance <= radius:
            result.append(addr)

    return result