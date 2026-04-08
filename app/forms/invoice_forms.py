from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

from app.models.customers import Customers
from app.models.employees import Employees
from extensions import db

STATUS = [
    ('Pending', 'Pending'),
    ('Processing', 'Processing'),
    ('Completed', 'Completed')
]


def _employee_choice():
    emp_list = db.select(Employees).order_by(Employees.name)
    emps = db.session.scalars(emp_list)

    return [
        (emp.id, emp.name)
        for emp in emps
    ]


def _customer_choice():
    customer_list = db.select(Customers).order_by(Customers.name)
    customers = db.session.scalars(customer_list)
    return [
        (customer.id, customer.name)
        for customer in customers
    ]

class InvoiceCreateForm(FlaskForm):
    
    customer_id = SelectField(
        "Select Customer",
        coerce=int,
        validators=[DataRequired()],
        render_kw={
            "placeholder": "Select Customer name",
            "class": "form-select"
        }
    )
    
    employee_id = SelectField(
        "Select Saler Name",
        validators=[DataRequired()],
        coerce=int,
        render_kw={
            "placeholder": "Select Saler Name", 
            "class": "form-select"
        }
    )
    
    inv_status = SelectField(
        "Status",
        choices=STATUS,
        default="Processing",
        render_kw={
            "placeholder": "Select Invoice Status",
            "class": "form-select",
        }
    )
    
    submit = SubmitField("Save")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customer_id.choices = _customer_choice()
        self.employee_id.choices = _employee_choice()