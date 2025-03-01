from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./students.db"

engine = create_async_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}, #disables this restriction, allowing the connection to be used across multiple threads.
    echo=True  # Prints SQL queries to console - helpful for debugging
)

SessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


'''
SQLite by default prevents multiple threads from sharing the same database connection.
Since FastAPI handles requests asynchronously, multiple requests might need access to the same DB connection.
'''