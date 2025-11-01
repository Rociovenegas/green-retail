from sqlalchemy import Column, Integer, String, Numeric, Text
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    stock = Column(Integer, default=0)
    keywords = Column(Text)
    pollution_score = Column(Numeric(10, 2))
    social_score = Column(Numeric(10, 2))
    economic_score = Column(Numeric(10, 2))
    sustainability_score = Column(Numeric(10, 2))
    
    
