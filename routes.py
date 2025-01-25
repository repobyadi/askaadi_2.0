from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, Product, Supplier

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/query")
def query_database(query: str, db: Session = Depends(get_db)):
    if "products" in query.lower():
        products = db.query(Product).all()
        return [{"id": p.id, "name": p.name, "brand": p.brand, "price": p.price} for p in products]
    elif "suppliers" in query.lower():
        suppliers = db.query(Supplier).all()
        return [{"id": s.id, "name": s.name, "categories": s.categories} for s in suppliers]
    else:
        return {"message": "Query not recognized"}
