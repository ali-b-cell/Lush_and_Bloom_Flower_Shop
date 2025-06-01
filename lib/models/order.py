from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base, Session

session = Session()


class Order(Base):
      __tablename__ = 'orders' 

      id = Column(Integer, primary_key=True)
      customer_id = Column(Integer, ForeignKey('customers.id'))
      product_id = Column(Integer, ForeignKey('products.id'))
      quantity = Column(Integer)

      customer = relationship("Customer", back_populates="orders")
      flower = relationship("Flower", back_populates="orders")
      orders = relationship("Order", back_populates="flower")

      def __repr__(self):
            return f"<Order #{self.id} - Customer {self.customer_id}, Flower {self.flower_id}, Time {self.timestamp}>"
      
      @classmethod
      def get_all(cls):
          return Session.query(cls).all()
      
      @classmethod
      def find_by_id(cls, id):
           return Session.query(cls).filter_by(id=id).first()
      
      def delete(self):
           Session.delete(self)
           Session.commit()