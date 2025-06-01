
from models import Customer, Product, Order
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///flower_shop.db')
Session = sessionmaker(bind=engine)
session = Session()


customers = session.query(Customer).all()
for customer in customers:
    print(customer)
