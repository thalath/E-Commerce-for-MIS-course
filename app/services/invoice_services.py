from extensions import db
from typing import List, Optional

from app.models.invoices import Invoices
from app.models.employees import Employees
from app.models.customers import Customers


class InvoiceServices:
    
    @staticmethod
    def get_all() -> List[Invoices]:
        return  Invoices.query.order_by(Invoices.inv_date.asc()).all()
    
    @staticmethod
    def get_by_id(inv_no) -> Optional[Invoices]:
        return Invoices.query.get(inv_no)
    
    
    @staticmethod
    def create( data: dict, employees: Optional[int] = None, customers: Optional[int] = None) -> Invoices:
        invoice = Invoices(
            inv_status = data.get("inv_status", "Processing")
        )

        if employees:
            emp = db.session.get(Employees, employees)
            if emp:
                invoice.employee_id = emp.id
                
        if customers:
            csm = db.session.get(Customers, customers)
            if csm:
                invoice.customer_id = csm.id
                
        db.session.add(invoice)
        db.session.commit()
        
        return invoice