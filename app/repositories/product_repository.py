from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.product import Product
from app.repositories.base import BaseRepository
from app.schemas.product import ProductCreate, ProductUpdate

class ProductRepository(BaseRepository[Product, ProductCreate, ProductUpdate]):
    def __init__(self):
        super().__init__(Product)

    async def get_active_by_category(
        self, db: AsyncSession, category_id: int, skip: int = 0, limit: int = 20
    ) -> List[Product]:
        """Retrieve active products under a specific category."""
        query = (
            select(self.model)
            .filter(self.model.category_id == category_id, self.model.is_active == True)
            .offset(skip)
            .limit(limit)
        )
        result = await db.execute(query)
        return result.scalars().all()

    async def check_and_update_stock(
        self, db: AsyncSession, product_id: int, quantity: int
    ) -> bool:
        """
        Checks if enough stock is available and decrements it.
        Returns True if successful, False otherwise.
        """
        result = await db.execute(
            select(self.model).filter(self.model.product_id == product_id)
        )
        product = result.scalars().first()
        if not product or product.stock_quantity < quantity:
            return False

        product.stock_quantity -= quantity
        db.add(product)
        await db.flush()  # Reserve stock inside the active transaction block
        return True

product_repository = ProductRepository()
