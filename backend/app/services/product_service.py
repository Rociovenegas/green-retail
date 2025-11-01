from sqlalchemy.orm import Session
from app.models.product import Product
from app.algorithms.scoring import calculate_sustainability_score
from typing import List, Optional

class ProductService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_products(self) -> List[Product]:

        products = self.db.query(Product).all()
        
        # Calcular score para cada producto
        for product in products:
            if product.sustainability_score  is None:
                product.sustainability_score  = calculate_sustainability_score(
                    product.pollution_score or 0,
                    product.social_score or 0,
                    product.economic_score or 0
                )
        
        return products
    
    
    
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
      
        product = self.db.query(Product).filter(Product.id == product_id).first()
        
        if product and product.sustainability_score is None:
            product.sustainability_score = calculate_sustainability_score(
                product.sustainability_score or 0,
                product.social_score or 0,
                product.economic_score or 0
            )
        
        return product
    
    def search_products(self, query: str) -> List[Product]:

        products = self.db.query(Product).filter(
            (Product.nombre.ilike(f"%{query}%")) |
            (Product.palabras_claves.ilike(f"%{query}%"))
        ).all()
        
       
        for product in products:
            if product.sustainability_score is None:
                product.sustainability_score = calculate_sustainability_score(
                    product.sustainability_score or 0,
                    product.social_score or 0,
                    product.economic_score or 0
                )
        
        return products