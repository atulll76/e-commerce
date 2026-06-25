from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

# Order Item (Order_Product) Schemas
class OrderItemBase(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemResponse(OrderItemBase):
    order_product_id: int
    order_id: int
    unit_price: float
    subtotal: float
    created_at: datetime

    class Config:
        from_attributes = True

# Orders Schemas
class OrderBase(BaseModel):
    user_id: int
    address_id: int
    order_status: str = "Pending"
    payment_status: str = "Pending"

class OrderCreate(BaseModel):
    user_id: int
    address_id: int
    items: List[OrderItemCreate]

class OrderUpdate(BaseModel):
    order_status: Optional[str] = None
    payment_status: Optional[str] = None

class OrderResponse(OrderBase):
    order_id: int
    order_date: datetime
    total_amount: float
    created_at: datetime
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True
