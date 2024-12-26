from sqlalchemy import select, insert

from src.database import async_session_maker
from src.wishlists.models import Wishlists
from src.wishlists.schemas import SWishlist


class WishlistDAO:
    model = Wishlists

    @classmethod
    async def get_wishlists(cls, user_id: int):
        async with async_session_maker() as session:
            query = select(Wishlists).where(user_id == Wishlists.user_id)
            result = await session.execute(query)

            return result.scalars().all()
        
    @classmethod
    async def create_wishlist(cls, *data: SWishlist):
        async with async_session_maker() as session:
            query = insert(Wishlists).values(
                name = data.name,
                description = data.description,
                on_what_date = data.on_what_date
            )
            result = await session.execute(query)

            return result.scalars()
