from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.product import ProductResponse
from app.services.product_service import ProductService

router = APIRouter()

@router.get("/", response_model=List[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):

    service = ProductService(db)
    products = service.get_all_products()
    return products

@router.get("/search", response_model=List[ProductResponse])
def search_products(
    q: str = Query(..., description="Término de búsqueda"),
    db: Session = Depends(get_db)
):
    # Busca productos por nombre o palabras claves
    service = ProductService(db)
    products = service.search_products(q)
    
    if not products:
        raise HTTPException(status_code=404, detail="No se encontraron productos")
    
    return products

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):

    service = ProductService(db)
    product = service.get_product_by_id(product_id)
    
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    return product