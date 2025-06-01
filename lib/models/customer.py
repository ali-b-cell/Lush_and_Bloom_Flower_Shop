from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base, Session 

class Customer(Base):
  __tablename__ = "customers"

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=False, unique=True)

  orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")

  def __repr__(self):
    return f"<Customer #{self.id}: {self.name}, {self.email}>"
  
  @classmethod
  def find_by_id(cls, id):
     return Session.query(cls).filter_by(id=id).first()
  

      