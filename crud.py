from sqlalchemy.orm import Session
from schemas import ProductCreate
from models import Product

def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        product_name=product.product_name,
        category=product.category,
        quantity=product.quantity,
        price=product.price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def read_product(db: Session, product_id: int):
    db_product = (db.query(Product)
                  .filter(Product.product_id == product_id)
                  .first()
    )
    
    return db_product

def read_all_products(db: Session):
    db_products = (db.query(Product)
                   .all()
    )

    return db_products

def update_product(db : Session, product_id: int, product: ProductCreate):
    db_product = read_product(db, product_id)

    if db_product is None:
        return None

    db_product.product_name = product.product_name
    db_product.category = product.category
    db_product.quantity = product.quantity
    db_product.price = product.price

    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = read_product(db, product_id)

    if db_product is None:
        return False

    db.delete(db_product)
    db.commit()
    return True

def search_products(db: Session, product_name: str):

    db_products = (db.query(Product)
                   .filter(Product.product_name.ilike(f"%{product_name}%"))
                   .all()
    )
    
    return db_products