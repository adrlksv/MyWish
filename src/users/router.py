from fastapi import APIRouter

from src.users.dao import UsersDAO
from src.users.schemas import SUserCreate
from src.users.auth import get_password_hash

from src.exceptions import UserAlreadyExistsException


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/register")
async def register_user(user_data: SUserCreate):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)

    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)

    await UsersDAO.add(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_password,
    )
