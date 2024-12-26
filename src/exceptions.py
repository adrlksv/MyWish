from fastapi import HTTPException, status


class WishListException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class TokenExpiredException(WishListException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token has expired"

class TokenAbsentException(WishListException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token is missing"

class IncorrectTokenFormatException(WishListException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"

class UserIsNotPresentException(WishListException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = ""

class UserAlreadyExistsException(WishListException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"

class IncorrectEmailOrPasswordException(WishListException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect email or password"

class InternalServerErrorException(WishListException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Internal server error"
