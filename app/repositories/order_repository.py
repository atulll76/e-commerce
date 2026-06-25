from typing import List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.order import Orders, Order_Product
from app.repositories.base import BaseRepository
from app.repositories.product_repository import product_repository
from app.schemas.order import OrderCreate, OrderUpdate

class OrderRepository(BaseRepository[Orders, OrderCreate, OrderUpdate]):
    def __init__(self):
        super().__init__(Orders)

    async def create_order_with_items(
        self, db: AsyncSession, user_id: int, address_id: int, items_in: List[Dict[str, Any]]
    ) -> Orders:
        """
        Creates an Order and associated Order_Product items atomically.
        Raises ValueError if any item runs out of stock or product is not found.
        """
        line_items = []
        total_amount = 0.0

        for item in items_in:
            product_id = item["product_id"]
            quantity = item["quantity"]

            # Try to decrement stock atomically
            stock_ok = await product_repository.check_and_update_stock(
                db, product_id, quantity
            )
            if not stock_ok:
                raise ValueError(f"Insufficient stock for product_id {product_id}")

            # Fetch product to verify pricing
            product = await product_repository.get(db, product_id)
            if not product:
                raise ValueError(f"Product with id {product_id} not found")

            unit_price = float(product.price)
            subtotal = unit_price * quantity
            total_amount += subtotal

            line_items.append(
                {
                    "product_id": product_id,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "subtotal": subtotal,
                }
            )

        # Create Order header record
        order = Orders(
            user_id=user_id,
            address_id=address_id,
            total_amount=total_amount,
            order_status="Pending",
            payment_status="Pending",
        )
        db.add(order)
        await db.flush()  # Populates order.order_id

        # Create Order_Product line item records
        for li in line_items:
            order_item = Order_Product(
                order_id=order.order_id,
                product_id=li["product_id"],
                quantity=li["quantity"],
                unit_price=li["unit_price"],
                subtotal=li["subtotal"],
            )
            db.add(order_item)

        await db.flush()
        return order

order_repository = OrderRepository()
