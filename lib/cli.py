from lib.models.base import Session
from lib import Flower, Customer, Order

session = Session()

customers = session.query(Customer).all()
for c in customers:
    print(c)

session.close()
