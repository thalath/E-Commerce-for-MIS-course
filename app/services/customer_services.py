from typing import Optional, List

from app.models.customers import Customers

from extensions import db


class CustomerServices:
    
    @staticmethod
    def get_all() -> List[Customers]:
        return Customers.query.order_by(Customers.id.asc()).all()

    @staticmethod
    def get_by_id(customer_id: int) -> Optional[Customers]:
        return Customers.query.get(customer_id)

        
    @staticmethod
    def create(data: dict, password: str) -> Customers:
        customer = Customers(
            name=data['name'],
            address=data['address'],
            email=data['email'],
            phone_number=data['phone_number'],
            discount=data['discount'],
        )
        
        customer.set_password(password)
        
        db.session.add(customer)
        db.session.commit()
        return customer