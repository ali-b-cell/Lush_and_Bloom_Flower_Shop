from lib.models.base import Base, Session, engine
from lib.models import Customer, Product, Order

def reset_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def seed_data():
    session = Session()

    reset_db()

    marie = Customer(name="Marie", email="Marie@outlook.com")
    isaack = Customer(name="Isaack", email="zak@gmail.com")
    lucinda = Customer(name="Lucinda", email="Lc_nder@yahoo.com")

    tulip = Product(name="Tulip Bouquet", price=125.99, stock=10)
    orchid = Product(name="Mini Orchid", price= 58.99, stock=7)
    rose = Product(name="Rose Box", price=82.99, stock=5)

    order1 = Order(customer=marie, product=tulip, quantity=2)
    order2 = Order(customer=isaack, product=orchid, quantity=1)
    order3 = Order(customer=lucinda, product=rose, quantity=3)

    session.add_all([marie, isaack, lucinda, tulip, orchid, rose, order1, order2, order3])
    session.commit()
    print("Seeded database successfully!")

    if __name__ == "__main__":
     seed_data()
