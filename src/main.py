from fastapi import FastAPI

from src.users.router import router as users_router
from src.wishlists.router import router as wishlist_router


app = FastAPI()

app.include_router(users_router)
app.include_router(wishlist_router)
