from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.services.order_service import order_service
from app.schemas.order import OrderCreate, OrderUpdate, OrderResponse

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(obj_in: OrderCreate, db: AsyncSession = Depends(get_db)):
    """Create a new order atomically, checking and updating stock."""
    try:
        items_dict = [
            {"product_id": item.product_id, "quantity": item.quantity}
            for item in obj_in.items
        ]
        return await order_service.create_order_with_items(
            db, obj_in.user_id, obj_in.address_id, items_dict
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("", response_model=List[OrderResponse])
async def list_orders(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    """List orders with pagination."""
    return await order_service.get_multi(db, skip=skip, limit=limit)

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieve order details by ID."""
    order = await order_service.get(db, order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order

@router.put("/{order_id}", response_model=OrderResponse)
async def update_order(order_id: int, obj_in: OrderUpdate, db: AsyncSession = Depends(get_db)):
    """Update order status or payment status."""
    order = await order_service.get(db, order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return await order_service.update(db, db_obj=order, obj_in=obj_in)

@router.delete("/{order_id}", response_model=OrderResponse)
async def delete_order(order_id: int, db: AsyncSession = Depends(get_db)):
    """Delete an order by ID."""
    order = await order_service.get(db, order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    deleted_order = await order_service.remove(db, order_id=order_id)
    return deleted_order
