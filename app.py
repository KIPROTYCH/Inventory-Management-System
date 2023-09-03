# app.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Supplier, Product

# Create a database connection
engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Add data to the database
def add_supplier(name):
    supplier = Supplier(name=name)
    session.add(supplier)
    session.commit()

def add_product(name, quantity, supplier_id):
    product = Product(name=name, quantity=quantity, supplier_id=supplier_id)
    session.add(product)
    session.commit()

# Test the functions
if __name__ == '__main__':
    add_supplier("Supplier A")
    add_supplier("Supplier B")

    add_product("Product 1", 100, 1)
    add_product("Product 2", 50, 1)
    add_product("Product 3", 75, 2)
