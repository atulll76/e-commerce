from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product
from app.repositories.product_repository import product_repository
from app.schemas.product import ProductCreate, ProductUpdate

class ProductService:
    async def get(self, db: AsyncSession, product_id: int) -> Optional[Product]:
        """Retrieve product detail by ID."""
        return await product_repository.get(db, product_id)

    async def get_active_by_category(
        self, db: AsyncSession, category_id: int, skip: int = 0, limit: int = 20
    ) -> List[Product]:
        """Retrieve active products under a specific category."""
        return await product_repository.get_active_by_category(
            db, category_id, skip=skip, limit=limit
        )

    async def check_and_update_stock(
        self, db: AsyncSession, product_id: int, quantity: int
    ) -> bool:
        """Checks if enough stock is available and decrements it."""
        return await product_repository.check_and_update_stock(db, product_id, quantity)

    async def create(self, db: AsyncSession, obj_in: ProductCreate) -> Product:
        """Create a new product entry with transaction commit/rollback."""
        try:
            db_obj = await product_repository.create(db, obj_in=obj_in)
            await db.commit()
            return db_obj
        except Exception:
            await db.rollback()
            raise

    async def update(self, db: AsyncSession, db_obj: Product, obj_in: ProductUpdate) -> Product:
        """Update an existing product entry with transaction commit/rollback."""
        try:
            updated_obj = await product_repository.update(db, db_obj=db_obj, obj_in=obj_in)
            await db.commit()
            return updated_obj
        except Exception:
            await db.rollback()
            raise

    async def remove(self, db: AsyncSession, product_id: int) -> Optional[Product]:
        """Remove a product entry with transaction commit/rollback."""
        try:
            deleted_obj = await product_repository.remove(db, id=product_id)
            await db.commit()
            return deleted_obj
        except Exception:
            await db.rollback()
            raise

    async def get_multi(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Product]:
        """Retrieve multiple products with pagination."""
        return await product_repository.get_multi(db, skip=skip, limit=limit)

product_service = ProductService()
