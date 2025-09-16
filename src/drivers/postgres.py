from contextlib import asynccontextmanager
from typing import Optional, AsyncIterator

import asyncpg
from asyncpg import Pool, Connection


class PostgresDriver:
    def __init__(self, dsn: str) -> None:
        self._dsn = dsn
        self._pool: Optional[Pool] = None

    async def start(self, min_size: int = 2, max_size: int = 20, **kwargs) -> None:
        try:
            self._pool = await asyncpg.create_pool(
                dsn=self._dsn, min_size=min_size, max_size=max_size, **kwargs
            )
        except Exception:
            # giữ nguyên traceback để debug dễ
            raise

    async def stop(self) -> None:
        if self._pool:
            await self._pool.close()
            self._pool = None

    def _get_pool(self) -> Pool:
        if not self._pool:
            raise RuntimeError("PostgreSQL pool is not initialized.")
        return self._pool

    @asynccontextmanager
    async def acquire(self) -> AsyncIterator[Connection]:
        pool = self._get_pool()
        async with pool.acquire() as conn:
            yield conn

    @asynccontextmanager
    async def transaction(self) -> AsyncIterator[Connection]:
        pool = self._get_pool()
        async with pool.acquire() as conn:
            async with conn.transaction():
                yield conn
