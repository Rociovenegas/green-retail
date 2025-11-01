from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.store import StoreResponse
from app.services.store_service import StoreService

router = APIRouter()

@router.get("/", response_model=List[StoreResponse])  
def get_all_stores(db: Session = Depends(get_db)):
    service = StoreService(db)
    stores = service.get_all_stores()
    return stores



@router.get("/search", response_model=List[StoreResponse])
def search_stores(
    q: str = Query(..., description="Término de busqueda"),
    db: Session = Depends(get_db)
):
    service = StoreService(db)
    Stores = service.search_stores(q)
    
    if not Stores:
        raise HTTPException(status_code=404, detail="No se encontraron tiendas")
    
    return Stores


@router.get("/{store_id}", response_model=StoreResponse)
def get_store(store_id: int, db: Session = Depends(get_db)):
    service = StoreService(db)
    store = service.get_store_by_id(store_id)
    
    if not store:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")
    
    return store
