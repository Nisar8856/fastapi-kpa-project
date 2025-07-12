from pydantic import BaseModel

class FormDataBase(BaseModel):
    name: str
    phone: str
    address: str

class FormDataCreate(FormDataBase):
    pass

class FormDataOut(FormDataBase):
    id: int

    class Config:
        orm_mode = True
