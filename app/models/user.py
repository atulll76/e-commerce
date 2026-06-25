import datetime
from typing import List, Optional
from sqlalchemy import String, Integer, Date, Boolean, DateTime, ForeignKey, Enum, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class User(Base):
    __tablename__ = "User"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    phone_number: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
    date_of_birth: Mapped[Optional[datetime.date]] = mapped_column(Date, nullable=True)
    disabled: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )

    # Relationship to Address table
    addresses: Mapped[List["Address"]] = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

class Address(Base):
    __tablename__ = "Address"

    address_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("User.user_id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    add_line_one: Mapped[str] = mapped_column(String(50), nullable=False)
    add_line_two: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    landmark: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    city: Mapped[str] = mapped_column(String(50), nullable=False)
    state: Mapped[str] = mapped_column(String(50), nullable=False)
    country: Mapped[str] = mapped_column(
        String(50), server_default="India", default="India", nullable=False
    )
    postal_code: Mapped[str] = mapped_column(String(10), nullable=False)
    address_type: Mapped[str] = mapped_column(
        Enum("Home", "Office", "Other", name="address_type_enum"),
        server_default="Home",
        default="Home",
        nullable=False,
    )
    is_default: Mapped[bool] = mapped_column(
        Boolean, server_default="0", default=False, nullable=False
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )

    # Relationship back to User
    user: Mapped["User"] = relationship("User", back_populates="addresses")
