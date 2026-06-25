from typing import List, Dict, Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.order import Orders
from app.repositories.order_repository import order_repository
from app.schemas.order import OrderCreate, OrderUpdate

class OrderService:
    async def get(self, db: AsyncSession, order_id: int) -> Optional[Orders]:
        """Fetch a single order record by ID."""
        return await order_repository.get(db, order_id)

    async def create_order_with_items(
        self, db: AsyncSession, user_id: int, address_id: int, items_in: List[Dict[str, Any]]
    ) -> Orders:
        """
        Creates an Order and associated Order_Product items atomically.
        Commits the transaction on success, or rolls back on any failure.
        """
        try:
            order = await order_repository.create_order_with_items(
                db, user_id, address_id, items_in
            )
            await db.commit()
            return order
        except Exception:
            await db.rollback()
            raise

    async def create(self, db: AsyncSession, obj_in: OrderCreate) -> Orders:
        """Create a new order entry (generic) with transaction commit/rollback."""
        try:
            db_obj = await order_repository.create(db, obj_in=obj_in)
            await db.commit()
            return db_obj
        except Exception:
            await db.rollback()
            raise

    async def update(self, db: AsyncSession, db_obj: Orders, obj_in: OrderUpdate) -> Orders:
        """Update an existing order entry with transaction commit/rollback."""
        try:
            updated_obj = await order_repository.update(db, db_obj=db_obj, obj_in=obj_in)
            await db.commit()
            return updated_obj
        except Exception:
            await db.rollback()
            raise

    async def remove(self, db: AsyncSession, order_id: int) -> Optional[Orders]:
        """Remove an order entry with transaction commit/rollback."""
        try:
            deleted_obj = await order_repository.remove(db, id=order_id)
            await db.commit()
            return deleted_obj
        except Exception:
            await db.rollback()
            raise

    async def get_multi(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Orders]:
        """Retrieve multiple orders with pagination."""
        return await order_repository.get_multi(db, skip=skip, limit=limit)

order_service = OrderService()
