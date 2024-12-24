from sqlalchemy import Column, String, Integer
from sqlalchemy.types import Date

from src.database import Base


class Wishlists(Base):
    __tablename__ = "wishlist"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), index=True)
    description = Column(String)
    on_what_date = Column(Date, nullable=True)
