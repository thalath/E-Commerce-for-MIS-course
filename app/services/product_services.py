from typing import List, Optional
from app.models.products import Products
from extensions import db

class ProductServices:
    
    @staticmethod
    def get_all() -> List[Products]:
        return Products.query.order_by(Products.code.asc()).all()

    @staticmethod
    def get_by_id(product_id: str) -> Optional[Products]:
        return Products.query.get(product_id)
    
    @staticmethod
    def create(data: dict, image: str) -> Products:
        product = Products(
            # code = data['code'],
            name = data['name'],
            category = data.get('category', None),
            unit_meansure = data['unit_meansure'],
            reorder_level = data['reorder_level'],
            sell_price = data['sell_price'],
            cost_price = data['cost_price'],
            in_stock = data['in_stock'],
        )
        
        product.images = image
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update(product: Products, data: dict, image_file: str) -> Products:

        # product.code = data['code']
        product.name = data['name']
        product.category = data.get('category', None)
        product.unit_meansure = data['unit_meansure']
        product.reorder_level = data['reorder_level']
        product.sell_price = data['sell_price']
        product.cost_price = data['cost_price']
        product.in_stock = data['in_stock']

        product.images = image_file
        
        if image_file is not None:
            product.images = image_file

        db.session.commit()
        return product

    @staticmethod
    def delete(product: Products) -> None:
        db.session.delete(product)
        db.session.commit()