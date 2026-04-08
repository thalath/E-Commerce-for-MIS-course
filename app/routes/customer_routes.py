from flask import Blueprint, render_template, redirect, url_for, abort, flash
from sqlalchemy.exc import IntegrityError

from app.services.customer_services import CustomerServices
from app.forms.customer_forms import CustomerCreateForm

from extensions import db


customer_bp = Blueprint('customers', __name__, url_prefix=('/customers'))

@customer_bp.route('/')
def index():
    customers = CustomerServices.get_all()
    return render_template('customers/index.html', customers=customers)

@customer_bp.route('/create', methods=["GET", "POST"])
def create():
    form = CustomerCreateForm()
    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "address": form.address.data,
            "email": form.email.data,
            "phone_number": form.phone_number.data,
            "discount": form.discount.data
        }
        
        password = form.password.data
        
        try:
            customer = CustomerServices.create(data, password)
            flash(f"Customer {customer.name} create Successfully", "success")
            return redirect(url_for('customers.index'))
        except IntegrityError as e:
            db.session.rollback()
            flash(f"Database ERROR: {e}")
            return render_template('customers/create.html', form=form)
        except Exception as e:
            flash(f"Logic Code Error: {e}", "warning")
            return render_template(f"customers/create.html", form=form)

    return render_template("customers/create.html", form=form)