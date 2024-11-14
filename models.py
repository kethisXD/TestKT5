from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    id: int
    username: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    userStatus: Optional[int] = Field(None, description="User Status")

class Store(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str 
    status: str
    complete: bool
