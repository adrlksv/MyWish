from pydantic import BaseModel


class SUserCreate(BaseModel):
    name: str
    username: str
    email: str
    password: str

class SUserLogin(BaseModel):
    email: str
    password: str
