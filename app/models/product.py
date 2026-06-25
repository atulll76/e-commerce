import datetime
from typing import List, Optional
from sqlalchemy import String, Integer, DateTime, ForeignKey, Enum, Numeric, Boolean, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Manufacturer(Base):
    __tablename__ = "Manufacturer"

    manufacturer_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    manufacturer_name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(100), unique=True, nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
    website: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    address: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    country: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, server_default="1", nullable=False)

    # Relationships
    products: Mapped[List["Product"]] = relationship("Product", back_populates="manufacturer")

class Category(Base):
    __tablename__ = "Category"

    category_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    category_description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, server_default="1", nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )

    # Relationships
    products: Mapped[List["Product"]] = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "Product"

    product_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    manufacturer_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Manufacturer.manufacturer_id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Category.category_id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    product_name: Mapped[str] = mapped_column(String(150), nullable=False)
    product_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    color: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    size: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    material: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    gender: Mapped[str] = mapped_column(
        Enum("Men", "Women", "Kids", "Unisex", name="gender_enum"),
        server_default="Unisex",
        default="Unisex",
        nullable=False,
    )
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    stock_quantity: Mapped[int] = mapped_column(Integer, default=0, server_default="0", nullable=False)
    image_url: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, server_default="1", nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )

    # Relationships
    manufacturer: Mapped["Manufacturer"] = relationship("Manufacturer", back_populates="products")
    category: Mapped["Category"] = relationship("Category", back_populates="products")
