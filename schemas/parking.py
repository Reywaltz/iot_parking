from pydantic import BaseModel

class Parking(BaseModel):
    id: int
    occupied: bool

    class Config:
        orm_mode = True
