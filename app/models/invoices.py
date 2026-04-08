from extensions import db
from sqlalchemy import Identity
from datetime import datetime

from app.models.associations import employee_invoice, customer_invoice

class Invoices(db.Model):
    __tablename__ = 'invoices'
    inv_no = db.Column(db.Integer, Identity(start=1, increment=1, always=True), primary_key=True)
    inv_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    inv_update = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='CASCADE'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id', ondelete='CASCADE'))
    inv_status = db.Column(db.String(50))
    description = db.Column(db.String(200))
    
    
    employee_id = db.relationship('Employees', secondary=employee_invoice, back_populates="invoice_id")
    customer_id = db.relationship('Customers', secondary=customer_invoice, back_populates='invoice_id')
    
    def __repr__(self) -> str:
        return f"<Date: {self.inv_date}>"