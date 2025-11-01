from pydantic import BaseModel
from typing import Optional


class ProductResponse(BaseModel):
    id: int
    name: str
    stock: int
    keywords: Optional[str] = None
    pollution_score: Optional[float] = None
    social_score: Optional[float] = None
    economic_score: Optional[float] = None
    sustainability_score : Optional[float] = None
    
    class Config:
        from_attributes = True  


class ProductSearch(BaseModel):
    query: str
    
    
