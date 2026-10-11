from sqlalchemy import Column, Integer, String, Float
from database import Base


class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    category = Column(String, index=True)
    quantity = Column(Integer, index=True)
    price = Column(Float, index=True)

