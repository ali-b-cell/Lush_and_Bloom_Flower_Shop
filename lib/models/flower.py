from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base

class Flower(Base):
    __tablename__ = "flowers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    orders = relationship("Order", back_populates="flower", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Flower #{self.id}: {self.name}, ${self.price}, Stock: {self.stock}>"
