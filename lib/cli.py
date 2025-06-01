from lib.models.base import Session
from lib.models import Customer, Product, Order

def main_menu():
    session = Session()
    print("\n Welcome to Lush & Bloom \n")
    
    session.close()

if __name__ == "__main__":
    main_menu()