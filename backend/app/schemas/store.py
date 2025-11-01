from pydantic import BaseModel
from typing import Optional


class StoreResponse(BaseModel):
    id: int
    name: str
    address: Optional[str] = None
    
    class Config:
        from_attributes = True  
        

# Schema para búsqueda
class StoreSearch(BaseModel):
    query: str
    
    
