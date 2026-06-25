from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field

class AddressBase(BaseModel):
    add_line_one: str = Field(..., max_length=50)
    add_line_two: Optional[str] = Field(None, max_length=100)
    landmark: Optional[str] = Field(None, max_length=100)
    city: str = Field(..., max_length=50)
    state: str = Field(..., max_length=50)
    country: str = Field("India", max_length=50)
    postal_code: str = Field(..., max_length=10)
    address_type: str = "Home"
    is_default: bool = False

class AddressCreate(AddressBase):
    pass

class AddressUpdate(BaseModel):
    add_line_one: Optional[str] = Field(None, max_length=50)
    add_line_two: Optional[str] = Field(None, max_length=100)
    landmark: Optional[str] = Field(None, max_length=100)
    city: Optional[str] = Field(None, max_length=50)
    state: Optional[str] = Field(None, max_length=50)
    country: Optional[str] = Field(None, max_length=50)
    postal_code: Optional[str] = Field(None, max_length=10)
    address_type: Optional[str] = None
    is_default: Optional[bool] = None

class AddressResponse(AddressBase):
    address_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    username: str = Field(..., max_length=50)
    email: str = Field(..., max_length=100)
    phone_number: Optional[str] = Field(None, max_length=15)
    date_of_birth: Optional[date] = None
    disabled: bool = False

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=255)

class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    username: Optional[str] = Field(None, max_length=50)
    email: Optional[str] = Field(None, max_length=100)
    phone_number: Optional[str] = Field(None, max_length=15)
    date_of_birth: Optional[date] = None
    disabled: Optional[bool] = None
    password: Optional[str] = Field(None, min_length=6, max_length=255)

class UserResponse(UserBase):
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
