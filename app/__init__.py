from flask import Flask, redirect, url_for
from config import Config
from extensions import db, csrf

def create_app(config_class: type[Config] = Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    
    # Init Extensions
    db.init_app(app)
    csrf.init_app(app)
    
    
    from app.routes.employee_routes import emp_bp
    from app.routes.job_routes import job_bp
    from app.routes.product_routes import product_bp
    from app.routes.customer_routes import customer_bp
    from app.routes.invoice_routes import invoice_bp
    
    app.register_blueprint(emp_bp)
    app.register_blueprint(job_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(invoice_bp)
    
    @app.route("/")
    def home():
        return redirect(url_for('employees.index'))
    
    with app.app_context():
        from app.models.employees import Employees
        from app.models.jobs import Jobs
        from app.models.categories import Categories
        from app.models.products import Products
        from app.models.customers import Customers
        from app.models.invoices import Invoices
        db.create_all()

    return app