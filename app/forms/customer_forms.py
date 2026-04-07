from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
import re
from extensions import db

from app.models.customers import Customers

def strong_password(form, field):
    "Requirement: min 8 chars, upper, lower, digit, special char"
    
    password = field.data or ""
    if len(password) < 8:
        raise ValidationError("password must be greater than 8.")
    
    if not re.search(r"[a-z]", password):
        raise ValidationError("Password must contain at least one lowercase character")

    if not re.search(r"[A-Z]", password):
        raise ValidationError('Password Must container at least one Uppercase character.')

    if not re.search(r"[0-9]", password):
        raise ValidationError("Password must container at least one digit.")
    
    if not re.search(r"[!@#$%^&*()_+`~=-[\]\\;':\",./<>?]", password):
        raise ValidationError("Password must container at least one special character.")
        


class CustomerCreateForm(FlaskForm):
    
    name = StringField(
        "Full Name",
        validators=[DataRequired(), Length(min=3, max=50)],
        render_kw={"placeholder": "Enter First anad Last Name"}
    )
    
    
    address = StringField(
        "Address",
        validators=[DataRequired(), Length(max=100)],
        render_kw={"placeholder": "Enter Address"}
    )
    
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(), Length(min=4, max=100)],
        render_kw={"placeholder": "Enter Email"}
    )
    
    phone_number = StringField(
        "Phone Number",
        validators=[DataRequired(), Length(max=15)],
        render_kw={"placeholder": "Enter Phone Number"},
    )
    
    discount = FloatField(
        "Discount",
        render_kw={"placeholder": "Discount"}
    )
    
    password = PasswordField(
        "Password",
        validators = [Optional(), strong_password,],
        render_kw={"placeholder": "Strong Password"}
    )
    
    
    confirm_password = PasswordField(
        "Comfirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwrod must be matched."),
        ],
        
        render_kw={"placeholder": "Confirm Password"}
    )
    
    submit = SubmitField("Save")
    
    
    def validate_email(self, field):
        exists = db.session.scalar(
            db.select(Customers).filter(Customers.email == field.data)
        )
        
        if exists:
            raise ValidationError("This email is already registered.")
    