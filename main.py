from fastapi import Depends, Query, FastAPI, HTTPException, Response
from schemas import ProductCreate, ProductResponse
from database import Base, engine, get_db
from sqlalchemy.orm import Session
from typing import List
import crud

app = FastAPI(title= "Inventory Management API")

Base.metadata.create_all(bind=engine)

@app.post("/products/", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products/search", response_model=List[ProductResponse])
def search_products(product_name: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    search_results = crud.search_products(db, product_name)

    return search_results
@app.get("/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.read_product(db, product_id)
    
    if db_product is None:
        raise HTTPException(
            status_code=404, 
            detail="Product not found"
        )
    
    return db_product

@app.get("/products/", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    return crud.read_all_products(db)

@app.put("/products/{product_id}", response_model = ProductResponse)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    updated_product = crud.update_product(db, product_id, product)

    if updated_product is None:
        raise HTTPException(
            status_code=404, 
            detail="Product not found"
        )

    return updated_product

@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = crud.delete_product(db, product_id)

    if not deleted_product:
        raise HTTPException(
            status_code=404, 
            detail="Product not found"
        )

    return Response(status_code=204, content=None)


