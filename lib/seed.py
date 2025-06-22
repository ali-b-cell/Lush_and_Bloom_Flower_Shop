from lib.models.base import Base, Session, engine
from lib.models.customer import Customer
from lib.models.flower import Flower
from lib.models.order import Order

def reset_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def seed_data():
    session = Session()
    reset_db()
    try:
        marie = Customer(name="Marie", email="Marie@outlook.com")
        isaack = Customer(name="Isaack", email="zak@gmail.com")
        lucinda = Customer(name="Lucinda", email="Lc_nder@yahoo.com")

        tulip = Flower(name="Tulip Bouquet", price=125.99, stock=10)
        orchid = Flower(name="Mini Orchid", price=58.99, stock=7)
        rose = Flower(name="Rose Box", price=82.99, stock=5)

        order1 = Order(customer=marie, flower=tulip, quantity=2)
        order2 = Order(customer=isaack, flower=orchid, quantity=1)
        order3 = Order(customer=lucinda, flower=rose, quantity=3)

        session.add_all([marie, isaack, lucinda, tulip, orchid, rose, order1, order2, order3])
        session.commit()
        print("Seeded database successfully!")
    finally:
        session.close()

if __name__ == "__main__":
    seed_data()