# test_db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Supplier, Product

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Query and print data
suppliers = session.query(Supplier).all()
for supplier in suppliers:
    print(f"Supplier: {supplier.name}")
    for product in supplier.products:
        print(f" - Product: {product.name}, Quantity: {product.quantity}")

session.close()
