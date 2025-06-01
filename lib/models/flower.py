from sqlalchemy import Column, Integer, String, Float
from .base import Base, Session

session = Session()

class Flower(Base):
    __tablename__ = 'flowers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    color = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Flower #{self.id}: {self.name} ({self.color}) - ${self.price:.2f}>"
    
    @classmethod
    def create(cls, name, color, price):
        flower = cls(name=name, color=color, price=price)
        session.add(flower)
        session.commit()
        return flower
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    def delete(self):
        session.delete(self)
        session.commit()


