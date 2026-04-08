from extensions import db

employee_invoice = db.Table(
    'employee_invoice',
    db.Column('employee_id', db.Integer, db.ForeignKey('employees.id'), primary_key=True),
    db.Column('invoice_id', db.Integer, db.ForeignKey('invoices.inv_no'), primary_key=True)
)


customer_invoice = db.Table(
    'customer_invoices',
    db.Column('customer_id', db.Integer, db.ForeignKey('customers.id'), primary_key=True),
    db.Column('invoice_id', db.Integer, db.ForeignKey('invoices.inv_no'), primary_key=True)
)