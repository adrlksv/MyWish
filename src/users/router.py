from fastapi import APIRouter, Response

from src.users.dao import UsersDAO
from src.users.schemas import SUserCreate, SUserLogin
from src.users.auth import get_password_hash, create_access_token, authenticate_user

from src.exceptions import (UserAlreadyExistsException, IncorrectEmailOrPasswordException,
                            InternalServerErrorException)


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/register", summary="Registration of user")
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


@router.post("/login", summary="User Authorization")
async def login_user(response: Response, user_data: SUserLogin):
    try:
        user = await authenticate_user(user_data.email, user_data.password)
        if not user:
            raise IncorrectEmailOrPasswordException
        access_token = create_access_token({"sub": str(user.id)})
        response.set_cookie("access_token", access_token, httponly=True)
        return access_token
    except Exception:
        raise InternalServerErrorException
    

@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("access_token")
