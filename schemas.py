from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class BookCreate(BaseModel):
    code: str
    title: str
    price: Decimal
    pages: int


class BookResponse(BookCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)