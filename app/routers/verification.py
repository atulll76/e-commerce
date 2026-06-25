from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.services import user_service, product_service, order_service
from app.schemas.user import UserResponse
from app.schemas.product import ProductResponse
from app.schemas.order import OrderResponse, OrderCreate

router = APIRouter(prefix="/verify", tags=["Verification"])

@router.get("/users/{user_id}", response_model=UserResponse)
async def verify_get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieve user detail by ID via user_service."""
    user = await user_service.get(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/products/{product_id}", response_model=ProductResponse)
async def verify_get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieve product detail by ID via product_service."""
    product = await product_service.get(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/orders", response_model=OrderResponse)
async def verify_create_order(order_data: OrderCreate, db: AsyncSession = Depends(get_db)):
    """Create order and decrement stock atomically using order_service."""
    try:
        items_dict = [
            {"product_id": item.product_id, "quantity": item.quantity}
            for item in order_data.items
        ]
        # Execute the multi-step checkout operation
        order = await order_service.create_order_with_items(
            db, order_data.user_id, order_data.address_id, items_dict
        )
        return order
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
