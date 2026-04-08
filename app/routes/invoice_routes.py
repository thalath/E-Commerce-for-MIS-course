from flask import Blueprint, flash, render_template, redirect, abort, url_for
from sqlalchemy.exc import IntegrityError

from app.models.employees import Employees
from app.models.customers import Customers
from app.services.invoice_services import InvoiceServices
from app.forms.invoice_forms import InvoiceCreateForm
from extensions import db

invoice_bp = Blueprint("invoices", __name__, url_prefix="/invoices")

@invoice_bp.route('/')
def index():
    invoices = InvoiceServices.get_all()
    return render_template('invoices/index.html', invoices=invoices)


@invoice_bp.route('/create', methods=["GET", "POST"])
def create():
    form = InvoiceCreateForm()
    if form.validate_on_submit():
        data = {
            "inv_status": form.inv_status.data
        }
        
        employee = form.employee_id.data or None
        customer = form.customer_id.data or None

        try:
            invoice = InvoiceServices.create(data=data, employees=employee, customers=customer)
            flash(f"Invoice {invoice.inv_date} was created successfully", "success")
            return redirect(url_for('invoices.index'))
        
        except IntegrityError as e:
            
            db.session.rollback()
            flash(f"Databse: Problem: {e}", "warning")
            return render_template('invoices/create', form=form)

        except Exception as e:
            flash(f"Logic Code Problems: {e}")
            return render_template('invoices/create', form=form)

    return render_template('invoices/create.html', form=form)
