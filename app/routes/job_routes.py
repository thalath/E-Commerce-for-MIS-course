from flask import Blueprint, render_template, flash, redirect, url_for, abort
from app.services.job_services import  JobServices
from app.forms.job_forms import JobCreateForm, JobEditForm, JobConfirmDeleteForm
from sqlalchemy.exc import IntegrityError

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
            "max_salary": form.max_salary.data,
        }
        
        try:
            JobServices.create(data)
            flash("Job position was created successfully", "success")
            return redirect(url_for('jobs.index'))

        except IntegrityError as e:
            # rollback is VERY important
            from extensions import db
            db.session.rollback()

            flash("Salary range is invalid (min must be less than max)", "danger")
            return render_template('jobs/create.html', form=form)

        except Exception as e:
            from extensions import db
            db.session.rollback()

            flash(f"Something went wrong! {e}", "danger")
            return render_template('jobs/create.html', form=form)

    return render_template('jobs/create.html', form=form)


@job_bp.route('/<int:job_id>/edit', methods=["GET","POST"])
def edit(job_id: int):
    
    job = JobServices.get_by_id(job_id)
    if job is None:
        abort(404)
        
    form = JobEditForm(original_job=job, obj=job)
    if form.validate_on_submit():
        data = {
            "title": form.title.data,
            "min_salary": form.min_salary.data,
            "max_salary": form.max_salary.data
        }
        
        try:
            JobServices.update(job, data)
            flash("Job position was updated successfully", "success")
            return redirect(url_for('jobs.index'))

        except IntegrityError as e:
            # rollback is VERY important
            from extensions import db
            db.session.rollback()

            flash("Salary range is invalid (min must be less than max)", "danger")
            return render_template('jobs/edit.html', form=form, job=job)
        
        except Exception as e:
            from extensions import db
            db.session.rollback()

            flash(f"Something went wrong! {e}", "danger")
            return render_template('jobs/edit.html', form=form, job=job)
                    
    return render_template('jobs/edit.html', form=form, job=job)

@job_bp.route('/<int:job_id>/delete', methods=["GET"])
def confirm_delete(job_id: int):
    job = JobServices.get_by_id(job_id)
    if job is None:
        abort(404)
    
    form = JobConfirmDeleteForm()
    return render_template('jobs/confirm_delete.html', form=form, job=job)

@job_bp.route('/<int:job_id>/delete', methods=["POST"])
def delete(job_id: int):
    job = JobServices.get_by_id(job_id)
    if job is None:
        abort(404)
    
    JobServices.delete(job)
    flash(f"Position: {job.title} was deleted successfully", "success")
    return redirect(url_for('jobs.index'))