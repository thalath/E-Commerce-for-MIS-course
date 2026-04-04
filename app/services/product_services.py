from typing import List, Optional
from app.models.products import Products

class ProductServices:
    
    @staticmethod
    def get_all() -> List[Products]:
        return Products.query.order_by(Products.code.asc()).all()

    @staticmethod
    def get_by_id(product_id: str) -> Optional[Products]:
        return Products.query.get(product_id)