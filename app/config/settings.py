import os
from pydantic import BaseModel

class Settings(BaseModel):
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "3306"))
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "atulatul")
    DB_NAME: str = os.getenv("DB_NAME", "e_commerce")

    @property
    def DATABASE_URL(self) -> str:
        """
        Asynchronous connection string for MySQL using aiomysql driver.
        """
        return f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()
