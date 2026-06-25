from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User, Address
from app.repositories.base import BaseRepository
from app.schemas.user import UserCreate, UserUpdate

class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):
    def __init__(self):
        super().__init__(User)

    async def get_by_email(self, db: AsyncSession, email: str) -> Optional[User]:
        """Retrieve user by unique email address."""
        result = await db.execute(select(self.model).filter(self.model.email == email))
        return result.scalars().first()

    async def get_by_username(self, db: AsyncSession, username: str) -> Optional[User]:
        """Retrieve user by unique username."""
        result = await db.execute(select(self.model).filter(self.model.username == username))
        return result.scalars().first()

    async def get_user_addresses(self, db: AsyncSession, user_id: int) -> List[Address]:
        """Retrieve all shipping/billing addresses for a given user."""
        result = await db.execute(select(Address).filter(Address.user_id == user_id))
        return result.scalars().all()

user_repository = UserRepository()
