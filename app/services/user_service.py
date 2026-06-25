from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User, Address
from app.repositories.user_repository import user_repository
from app.schemas.user import UserCreate, UserUpdate

class UserService:
    async def get(self, db: AsyncSession, user_id: int) -> Optional[User]:
        """Retrieve user detail by ID."""
        return await user_repository.get(db, user_id)

    async def get_by_email(self, db: AsyncSession, email: str) -> Optional[User]:
        """Retrieve user by unique email address."""
        return await user_repository.get_by_email(db, email)

    async def get_by_username(self, db: AsyncSession, username: str) -> Optional[User]:
        """Retrieve user by unique username."""
        return await user_repository.get_by_username(db, username)

    async def get_user_addresses(self, db: AsyncSession, user_id: int) -> List[Address]:
        """Retrieve all shipping/billing addresses for a given user."""
        return await user_repository.get_user_addresses(db, user_id)

    async def create(self, db: AsyncSession, obj_in: UserCreate) -> User:
        """Create a new user entry with transaction commit/rollback."""
        try:
            db_obj = await user_repository.create(db, obj_in=obj_in)
            await db.commit()
            return db_obj
        except Exception:
            await db.rollback()
            raise

    async def update(self, db: AsyncSession, db_obj: User, obj_in: UserUpdate) -> User:
        """Update an existing user entry with transaction commit/rollback."""
        try:
            updated_obj = await user_repository.update(db, db_obj=db_obj, obj_in=obj_in)
            await db.commit()
            return updated_obj
        except Exception:
            await db.rollback()
            raise

    async def remove(self, db: AsyncSession, user_id: int) -> Optional[User]:
        """Remove a user entry with transaction commit/rollback."""
        try:
            deleted_obj = await user_repository.remove(db, id=user_id)
            await db.commit()
            return deleted_obj
        except Exception:
            await db.rollback()
            raise

    async def get_multi(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[User]:
        """Retrieve multiple user profiles with pagination."""
        return await user_repository.get_multi(db, skip=skip, limit=limit)

user_service = UserService()
