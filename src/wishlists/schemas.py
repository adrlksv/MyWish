from pydantic import BaseModel

from datetime import date


class SWishlist(BaseModel):
    name: str
    description: str
    on_what_date: date
