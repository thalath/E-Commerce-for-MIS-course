from flask import Blueprint, render_template, Response
from app.services.product_services import ProductServices

product_bp = Blueprint('products', __name__, url_prefix='/products')


@product_bp.route('/images/<p_code>')
def image(p_code: str):
    p = ProductServices.get_by_id(p_code)
    if p and p.images:
        return Response(p.images, mimetype='image/jpg')

    return 'No image', 404

@product_bp.route('/')
def index():
    products = ProductServices.get_all()
    return render_template('products/index.html', products=products)