from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length


class JobCreateForm(FlaskForm):
    
    title = StringField(
        "Job Title",
        validators=[DataRequired(), Length(max=20)],
        render_kw={"placeholder": "Enter The job title"}
    )
    
    min_salary = FloatField(
        "Minimum Salary",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the Minimum Salary Ranges"}
    )
    
    max_salary = FloatField(
        "Maximum Salary",
        validators=[DataRequired()],
        render_kw={"placeholder": "enter The maximum Range of Salary"}
    )
    submit = SubmitField("Save")
    
    
class JobEditForm(FlaskForm):

    title = StringField(
        "Job Title",
        validators=[DataRequired(), Length(max=20)],
        render_kw={"placeholder": "Enter The job title"}
    )
    
    min_salary = FloatField(
        "Minimum Salary",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the Minimum Salary Ranges"}
    )
    
    max_salary = FloatField(
        "Maximum Salary",
        validators=[DataRequired()],
        render_kw={"placeholder": "enter The maximum Range of Salary"}
    )
    submit = SubmitField("Update")
    
    def __init__(self, original_job, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_job = original_job
        
class JobConfirmDeleteForm(FlaskForm):
    submit = SubmitField("ConfirmDelete")