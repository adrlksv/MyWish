from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.types import Date

from src.database import Base

from src.users.models import Users


class Wishlists(Base):
    __tablename__ = "wishlist"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), index=True)
    user_id = Column(Integer, ForeignKey(Users.id))
    description = Column(String)
    on_what_date = Column(Date, nullable=True)
