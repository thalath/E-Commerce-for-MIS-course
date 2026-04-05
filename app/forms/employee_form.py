from extensions import db
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms import StringField, DateField, SelectField, TextAreaField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models.jobs import Jobs

def _position_choices():
    jobs = db.select(Jobs).order_by(Jobs.title)
    
    return [
        (job.id, job.title)
        for job in db.session.scalars(jobs)
    ]

class EmployeeCreateForm(FlaskForm):
    
    name = StringField(
        "Employee Name",
        validators=[DataRequired(), Length(min=3, max=50)],
        render_kw={"placeholder": "Enter your name"}
    )
    
    gender = StringField(
        "Select Gender",
        validators=[Length(max=6)],
        render_kw={"placeholder": "Enter your gender"},
    )
    
    birthdate = DateField(
        "Pick Your birth date",
        validators=[DataRequired()],
    )
    
    job_id = SelectField(
        "Select Your Position",
        coerce=int,
        validators=[DataRequired()],
        render_kw={"placeholder": "Select position"}
    )
    
    address = TextAreaField(
        "Address",
        validators=[Length(max=150)],
        render_kw={"placeholder": "Enter your address"}
    )
    
    phone = StringField(
        "Number",
        validators=[DataRequired(), Length(max=15)],
        render_kw={"placeholder": "Enter your phone number"}
    )
    
    salary = FloatField(
        "Salary",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter your salart"}
    )
    
    remarks = StringField(
        "Remarks",
        render_kw={"placeholder": "Enter your the remarks", }
    )
    
    
    photo = FileField(
        "PHOTO",
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'png', 'jpeg'], 'image')
        ]
    )
    
    submit = SubmitField("Save")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_id.choices = _position_choices()
        
class EmployeeEditForm(FlaskForm):
    
    name = StringField(
        "Employee Name",
        validators=[DataRequired(), Length(min=3, max=50)],
        render_kw={"placeholder": "Enter your name"}
    )
    
    gender = StringField(
        "Select Gender",
        validators=[Length(max=6)],
        render_kw={"placeholder": "Enter your gender"},
    )
    
    birthdate = DateField(
        "Pick Your birth date",
        validators=[DataRequired()],
    )
    
    job_id = SelectField(
        "Select Your Position",
        coerce=int,
        validators=[DataRequired()],
        render_kw={"placeholder": "Select position"}
    )
    
    address = TextAreaField(
        "Address",
        validators=[Length(max=150)],
        render_kw={"placeholder": "Enter your address"}
    )
    
    phone = StringField(
        "Number",
        validators=[DataRequired(), Length(max=15)],
        render_kw={"placeholder": "Enter your phone number"}
    )
    
    salary = FloatField(
        "Salary",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter your salary"}
    )
    
    remarks = StringField(
        "Remarks",
        render_kw={"placeholder": "Enter your the remarks"}
    )
    
    
    photo = FileField(
        "PHOTO",
        validators=[
            # FileRequired(),
            FileAllowed(['jpg', 'png', 'jpeg'], 'image only')
        ]
    )
    
    submit = SubmitField("Update")
    
    def __init__(self, original_employee, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_employee = original_employee
        self.job_id.choices = _position_choices()

class EmployeeConfirmDeleteForm(FlaskForm):
    submit = SubmitField('Confirm Delete')