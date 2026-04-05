from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, FloatField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length

from app.models.products import Products
from app.models.categories import Categories
from extensions import db

def _categories_choice():
    category_filter = db.select(Categories).order_by(Categories.name.asc())
    categories = db.session.scalars(category_filter)
    return [
        (category.id, category.name)
        for category in categories
    ]

class ProductCreateForm(FlaskForm):
    
    # ============= Instead Input products' code, i created a sequence, and trigger from oracle Rdbms =======
    # code = StringField(
    #     "Product Code",
    #     validators=[DataRequired(), Length(min=2, max=30)],
    #     render_kw={"placeholder": "Enter Product Code", "class": "form-control"}
    # )
    
    name = StringField(
        "Product Name",
        validators=[DataRequired(), Length(max=30)],
        render_kw={"placeholder": "Enter Product Name", "class": "form-control"}
    )
    
    category = SelectField(
        "Category",
        coerce=int,
        validators=[DataRequired(),],
        render_kw={"placeholder": "Choosing Category", "class": "form-select"}
    )
    
    unit_meansure = StringField(
        "Unit Meansure",
        validators=[DataRequired(), Length(max=30)],
        render_kw={"placeholder": "Enter Unit Meansure", "class": "form-control"}
    )
    
    reorder_level = FloatField(
        "Reorder Level",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Reorder Level", "class": "form-control"}
    )
    
    sell_price = FloatField(
        "Sell Price",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Reorder Level", "class": "form-control"}
    )
    
    cost_price = FloatField(
        "Cost Price",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Reorder Level", "class": "form-control"}
    )
    
    in_stock = IntegerField(
        "In Stock",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Reorder Level", "class": "form-control"}
    )
    
    images = FileField(
        "Images",
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'png', 'jpeg'], 'Image only')
        ]
    )
    
    submit = SubmitField('Save')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category.choices = _categories_choice()
        
        
class ProductEditForm(FlaskForm):
    
    # ============= Instead Input products' code, i created a sequence, and trigger from oracle Rdbms =======
    # code = StringField(
    #     "Product Code",
    #     validators=[DataRequired(), Length(min=2, max=30)],
    #     render_kw={"placeholder": "Enter Product Code", "class": "form-control"}
    # )
    
    name = StringField(
        "Product Name",
        validators=[DataRequired(), Length(max=30)],
        render_kw={"placeholder": "Enter Product Name", "class": "form-control"}
    )
    
    category = SelectField(
        "Category",
        coerce=int,
        validators=[DataRequired(),],
        render_kw={"placeholder": "Choosing Category", "class": "form-select"}
    )
    
    unit_meansure = StringField(
        "Unit Meansure",
        validators=[DataRequired(), Length(max=30)],
        render_kw={"placeholder": "Enter Unit Meansure", "class": "form-control"}
    )
    
    reorder_level = FloatField(
        "Reorder Level",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Reorder Level", "class": "form-control"}
    )
    
    sell_price = FloatField(
        "Sell Price",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Reorder Level", "class": "form-control"}
    )
    
    cost_price = FloatField(
        "Cost Price",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Reorder Level", "class": "form-control"}
    )
    
    in_stock = IntegerField(
        "In Stock",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Reorder Level", "class": "form-control"}
    )
    
    images = FileField(
        "Images",
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'png', 'jpeg'], 'Image only')
        ]
    )
    
    submit = SubmitField('Update')

    def __init__(self, original_product: Products, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_product = original_product
        self.category.choices = _categories_choice()


class ProductConfirmDeleteForm(FlaskForm):
    submit = SubmitField('Confirm Delete')