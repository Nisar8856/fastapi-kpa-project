from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/formdata/", response_model=schemas.FormDataOut)
def create_form_data(form: schemas.FormDataCreate, db: Session = Depends(get_db)):
    return crud.create_form_data(db, form)

@app.get("/formdata/{id}", response_model=schemas.FormDataOut)
def read_form_data(id: int, db: Session = Depends(get_db)):
    data = crud.get_form_data(db, id)
    if not data:
        raise HTTPException(status_code=404, detail="Form not found")
    return data
