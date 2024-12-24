from sqlalchemy import select

from src.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).where(id = model_id)
            result = await session.execute(query)

            return result.scalar_one_or_none()
    