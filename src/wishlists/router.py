from fastapi import APIRouter, Depends

from src.users.dependencies import get_current_user
from src.wishlists.dao import WishlistDAO
from src.wishlists.schemas import SWishlist

from src.exceptions import InternalServerErrorException


router = APIRouter(
    prefix="/wishlists",
    tags=["wishlists"],
)


@router.get("")
async def get_wishlists(user = Depends(get_current_user)):
    return await WishlistDAO.get_wishlists(user.id)


@router.post("/add-wishlist")
async def add_wishlist(*data: SWishlist, user = Depends(get_current_user)):
    try:
        await WishlistDAO.create_wishlist(*data)
    except Exception:
        raise InternalServerErrorException
    
    return {
        "message": "..."
    }
