from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://username:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Supplier(Base):
    __tablename__ = "Suppliers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    contact_info = Column(Text, nullable=False)
    categories = Column(Text, nullable=False)

class Product(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    brand = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    supplier_id = Column(Integer, ForeignKey("Suppliers.id"))
