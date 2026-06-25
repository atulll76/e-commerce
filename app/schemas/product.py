from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

# Manufacturer Schemas
class ManufacturerBase(BaseModel):
    manufacturer_name: str = Field(..., max_length=100)
    email: Optional[str] = Field(None, max_length=100)
    phone_number: Optional[str] = Field(None, max_length=15)
    website: Optional[str] = Field(None, max_length=255)
    address: Optional[str] = Field(None, max_length=255)
    country: Optional[str] = Field(None, max_length=50)
    is_active: bool = True

class ManufacturerCreate(ManufacturerBase):
    pass

class ManufacturerUpdate(BaseModel):
    manufacturer_name: Optional[str] = Field(None, max_length=100)
    email: Optional[str] = Field(None, max_length=100)
    phone_number: Optional[str] = Field(None, max_length=15)
    website: Optional[str] = Field(None, max_length=255)
    address: Optional[str] = Field(None, max_length=255)
    country: Optional[str] = Field(None, max_length=50)
    is_active: Optional[bool] = None

class ManufacturerResponse(ManufacturerBase):
    manufacturer_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Category Schemas
class CategoryBase(BaseModel):
    category_name: str = Field(..., max_length=100)
    category_description: Optional[str] = Field(None, max_length=255)
    is_active: bool = True

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    category_name: Optional[str] = Field(None, max_length=100)
    category_description: Optional[str] = Field(None, max_length=255)
    is_active: Optional[bool] = None

class CategoryResponse(CategoryBase):
    category_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Product Schemas
class ProductBase(BaseModel):
    manufacturer_id: int
    category_id: int
    product_name: str = Field(..., max_length=150)
    product_description: Optional[str] = None
    color: Optional[str] = Field(None, max_length=50)
    size: Optional[str] = Field(None, max_length=20)
    material: Optional[str] = Field(None, max_length=100)
    gender: str = "Unisex"
    price: float
    stock_quantity: int = 0
    image_url: Optional[str] = Field(None, max_length=255)
    is_active: bool = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    manufacturer_id: Optional[int] = None
    category_id: Optional[int] = None
    product_name: Optional[str] = Field(None, max_length=150)
    product_description: Optional[str] = None
    color: Optional[str] = Field(None, max_length=50)
    size: Optional[str] = Field(None, max_length=20)
    material: Optional[str] = Field(None, max_length=100)
    gender: Optional[str] = None
    price: Optional[float] = None
    stock_quantity: Optional[int] = None
    image_url: Optional[str] = Field(None, max_length=255)
    is_active: Optional[bool] = None

class ProductResponse(ProductBase):
    product_id: int
    created_at: datetime

    class Config:
        from_attributes = True
