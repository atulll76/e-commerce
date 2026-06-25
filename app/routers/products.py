from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.services.product_service import product_service
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(obj_in: ProductCreate, db: AsyncSession = Depends(get_db)):
    """Create a new product record."""
    return await product_service.create(db, obj_in=obj_in)

@router.get("", response_model=List[ProductResponse])
async def list_products(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    """List products with pagination."""
    return await product_service.get_multi(db, skip=skip, limit=limit)

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieve product details by ID."""
    product = await product_service.get(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, obj_in: ProductUpdate, db: AsyncSession = Depends(get_db)):
    """Update an existing product record."""
    product = await product_service.get(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return await product_service.update(db, db_obj=product, obj_in=obj_in)

@router.delete("/{product_id}", response_model=ProductResponse)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    """Delete a product record by ID."""
    product = await product_service.get(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    deleted_product = await product_service.remove(db, product_id=product_id)
    return deleted_product
