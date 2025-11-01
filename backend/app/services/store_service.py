from sqlalchemy.orm import Session
from app.models.store import Store
from typing import List, Optional

class StoreService:
    def __init__(self, db: Session):
        self.db = db
        
        
    def get_all_stores(self) -> List[Store]:
        stores = self.db.query(Store).all()
        return stores
    
    
    def search_stores(self, query: str) -> List[Store]:
        stores = self.db.query(Store).filter(
            Store.name.ilike(f"%{query}%")).all() 
        return stores

    
    def get_store_by_id(self, store_id: int) -> Optional[Store]:  
        store = self.db.query(Store).filter(Store.id == store_id).first()
        return store
    
    


