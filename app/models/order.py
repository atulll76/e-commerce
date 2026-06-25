import datetime
from typing import List
from sqlalchemy import Integer, DateTime, ForeignKey, Enum, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Orders(Base):
    __tablename__ = "Orders"

    order_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("User.user_id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    address_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Address.address_id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    order_date: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )
    total_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    order_status: Mapped[str] = mapped_column(
        Enum(
            "Pending",
            "Confirmed",
            "Packed",
            "Shipped",
            "Out for Delivery",
            "Delivered",
            "Cancelled",
            "Returned",
            name="order_status_enum",
        ),
        server_default="Pending",
        default="Pending",
        nullable=False,
    )
    payment_status: Mapped[str] = mapped_column(
        Enum("Pending", "Paid", "Failed", "Refunded", name="payment_status_enum"),
        server_default="Pending",
        default="Pending",
        nullable=False,
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )

    # Relationships
    user: Mapped["User"] = relationship("User")
    address: Mapped["Address"] = relationship("Address")
    items: Mapped[List["Order_Product"]] = relationship(
        "Order_Product", back_populates="order", cascade="all, delete-orphan"
    )

class Order_Product(Base):
    __tablename__ = "Order_Product"

    order_product_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Orders.order_id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Product.product_id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    subtotal: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )

    # Relationships
    order: Mapped["Orders"] = relationship("Orders", back_populates="items")
    product: Mapped["Product"] = relationship("Product")
