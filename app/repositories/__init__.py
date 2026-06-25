from app.repositories.base import BaseRepository
from app.repositories.user_repository import user_repository, UserRepository
from app.repositories.product_repository import product_repository, ProductRepository
from app.repositories.order_repository import order_repository, OrderRepository

__all__ = [
    "BaseRepository",
    "user_repository",
    "UserRepository",
    "product_repository",
    "ProductRepository",
    "order_repository",
    "OrderRepository",
]
