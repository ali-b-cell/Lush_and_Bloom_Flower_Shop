from lib.models import Customer, Product, Order
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///lib/flower_shop.db')
Session = sessionmaker(bind=engine)
session = Session()

def view_products():
    products = session.query(Product).all()
    for p in products:
        print(f"{p.id}. {p.name} - ${p.price} (Stock: {p.stock})")

def main_menu():
    while True:
        print("\n--- Lush & Leaf Flower Shop ---")
        print("1. View Products")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_products()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")



cli

from lib.helpers import main_menu

if __name__ == "__main__":
    main_menu()

