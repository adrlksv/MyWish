from sqlalchemy import Column, Integer, String, ForeignKey

from src.database import Base

from src.wishlists.models import Wishlists


class Gifts(Base):
    __tablename__ = "gift"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String)
    wishlist_id = Column(ForeignKey(Wishlists.id), nullable=False)
    img_url = Column(String, nullable=True)
    gift_url = Column(String, nullable=False)
    price = Column(Integer)
