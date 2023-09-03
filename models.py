# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    products = relationship('Product', back_populates='supplier')

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)

    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship('Supplier', back_populates='products')
