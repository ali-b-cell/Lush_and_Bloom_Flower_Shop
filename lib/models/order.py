from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    flower_id = Column(Integer, ForeignKey("flowers.id"))
    quantity = Column(Integer, nullable=False)

    customer = relationship("Customer", back_populates="orders")
    flower = relationship("Flower", back_populates="orders")

    def __repr__(self):
        return f"<Order #{self.id}: Customer {self.customer_id}, Flower {self.flower_id}, Quantity: {self.quantity}>"
