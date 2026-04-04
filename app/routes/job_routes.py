from flask import Blueprint, render_template, flash, redirect, url_for
from app.services.job_services import  JobServices
from app.forms.job_forms import JobCreateForm


job_bp = Blueprint('jobs', __name__, url_prefix='/jobs')

@job_bp.route('/')
def index():
    jobs = JobServices.get_all()
    return render_template('jobs/index.html', jobs=jobs)


@job_bp.route('/create', methods=["GET", 'POST'])
def create():
    form = JobCreateForm()
    if form.validate_on_submit():
        data = {
            "title": form.title.data,
            "min_salary": form.min_salary.data,
            "max_salary": form.max_salary.data
        }
        
        job = JobServices.create(data)
        flash(f"Position {job.title} was created successfully", "success")
        return redirect(url_for('jobs.index'))
    return render_template('jobs/create.html', form=form)