from sqlalchemy.orm import Session
from . import models, schemas

def create_form_data(db: Session, data: schemas.FormDataCreate):
    form = models.FormData(**data.dict())
    db.add(form)
    db.commit()
    db.refresh(form)
    return form

def get_form_data(db: Session, data_id: int):
    return db.query(models.FormData).filter(models.FormData.id == data_id).first()
