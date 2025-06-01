from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base, Session


class Product(Base):  # <- was class Order(Base)
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    orders = relationship("Order", back_populates="product")

    def __repr__(self):
        return f"<Product #{self.id} - {self.name}, Price: {self.price}>"

    @classmethod
    def get_all(cls):
        return Session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return Session.query(cls).filter_by(id=id).first()

    def delete(self):
        Session.delete(self)
        Session.commit()