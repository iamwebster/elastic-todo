from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession, 
    async_sessionmaker,
    create_async_engine
)

from .database_config import mysql_config


class DbHelper:
    def __init__(
        self, 
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
        pool_size: int = 5, 
        max_overflow: int = 10
    ):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False
        )

    async def dispose(self):
        await self.engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory as session:
            yield session


db_helper = DbHelper(
    url=mysql_config.get_url(),
    echo=True,
    echo_pool=True
)