from flask import Blueprint, render_template, Response, request, flash, redirect, url_for, abort
from app.services.product_services import ProductServices
from app.forms.product_forms import ProductCreateForm, ProductEditForm, ProductConfirmDeleteForm

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

@product_bp.route('/create', methods=['GET', 'POST'])
def create():
    form = ProductCreateForm()
    if form.validate_on_submit():
        data = {
            # "code": form.code.data,
            "name": form.name.data,
            "category": form.category.data,
            "unit_meansure": form.unit_meansure.data,
            "reorder_level": form.reorder_level.data,
            "sell_price": form.sell_price.data,
            "cost_price": form.cost_price.data,
            "in_stock": form.in_stock.data
        }
        
        file = request.files.get('images')
        images = None
        if file and file != '':
            images = file.read()
            
        product = ProductServices.create(data, images)

        flash(f"Product {product.name} was created successfully", "success")
        return redirect(url_for('products.index'))
    
    return render_template('products/create.html', form=form)


@product_bp.route('/edit/<product_code>', methods=["GET", "POST"])
def edit(product_code: str):
    product = ProductServices.get_by_id(product_code)
    if product is None:
        abort(404)
        
    form = ProductEditForm(original_product=product, obj=product)
    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "category": form.category.data,
            "unit_meansure": form.unit_meansure.data,
            "reorder_level": form.reorder_level.data,
            "sell_price": form.sell_price.data,
            "cost_price": form.cost_price.data,
            "in_stock": form.in_stock.data,
        }
        
        image_file = request.files.get('images')
        file = None
        if image_file and image_file != '':
            file = image_file.read()
            
        

        ProductServices.update(product, data, file)
        flash(f"Product {product.name} was updated successfuly", "success")
        return redirect(url_for('products.index'))
    
    return render_template('products/edit.html', form=form, product=product)

@product_bp.route('/delete/<product_code>', methods=["GET"])
def confirm_delete(product_code: str):
    product = ProductServices.get_by_id(product_code)
    if product is None:
        abort(404)

    form = ProductConfirmDeleteForm()
    return render_template('products/confirm_delete.html', form=form, product=product)

@product_bp.route('/delete/<product_code>', methods=["POST"])
def delete(product_code: str):
    
    product = ProductServices.get_by_id(product_code)
    if product is None:
        abort(404)
        
    ProductServices.delete(product)
    flash(f"Product: {product.code} was deleted successfully", "success")
    return redirect(url_for('products.index'))