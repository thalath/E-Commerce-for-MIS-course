from flask import render_template, url_for, redirect, Blueprint, Response, flash, request, abort
from app.services.employee_services import EmployeeServices
from app.forms.employee_form import EmployeeCreateForm, EmployeeEditForm, EmployeeConfirmDeleteForm

emp_bp = Blueprint("employees", __name__, url_prefix="/employees")

@emp_bp.route("/photo/<int:id>")
def employee_photo(id):
    employee = EmployeeServices.get_by_id(id)

    if employee and employee.photo:
        return Response(employee.photo, mimetype='image/jpeg')

    return "No Image", 404

@emp_bp.route("/")
def index():
    users = EmployeeServices.get_all()
        
    return render_template("employees/index.html", users=users)

@emp_bp.route("/card")
def card():
    emps = EmployeeServices.get_all()
    return render_template("employees/card.html", emps=emps)


@emp_bp.route("/create", methods=["GET", "POST"])
def create():
    
    form = EmployeeCreateForm()
    if form.validate_on_submit():
        
        data = {
            "name": form.name.data,
            "gender": form.gender.data,
            "birthdate": form.birthdate.data,
            "job_title": form.job_id.data,
            "address": form.address.data,
            "phone": form.phone.data,
            "salary": form.salary.data,
            "remarks": form.remarks.data,
        }
        
        file = request.files.get('photo')
        if file:
            photo = file.read()
        
        emp = EmployeeServices.create(data, photo)
        flash(f"Employee {emp.name} Created Successfully", "success")
        return redirect(url_for('employees.card'))
    
    return render_template("employees/create.html", form=form)

@emp_bp.route('/<int:emp_id>/edit', methods=["GET", "POST"])
def edit(emp_id: int):
    emp = EmployeeServices.get_by_id(emp_id)

    if emp is None:
        abort(404)
        
    form = EmployeeEditForm(original_employee=emp, obj=emp)
    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "gender": form.gender.data,
            "address": form.address.data,
            "salary": form.salary.data,
            "photo": form.photo.data,
            "phone": form.phone.data,
            "remarks": form.remarks.data,
            "birthdate": form.birthdate.data,
            "job_id": form.job_id.data or None
        }
        
        
        image = None
        photo = request.files['photo']
        if photo:
            image = photo.read()
        
        EmployeeServices.update(emp, data, image)
        flash(f"Employee {emp} was updated successfully", "success")
        return redirect(url_for('employees.index'))
    
    return render_template('employees/edit.html', form=form, emp=emp)


@emp_bp.route('/<int:emp_id>/delete', methods=['GET'])
def confirm_delete(emp_id: int):
    emp = EmployeeServices.get_by_id(emp_id)
    
    if emp is None:
        abort(404)

    form = EmployeeConfirmDeleteForm()
    return render_template('employees/confirm_delete.html', form=form, emp=emp)

@emp_bp.route('/<int:emp_id>/delete', methods=["POST"])
def delete(emp_id: int):
    emp = EmployeeServices.get_by_id(emp_id)
    if emp is None:
        abort(404)

    EmployeeServices.delete(emp)
    flash(f"Employee {emp.name} was deleted successfully", 'success')
    return redirect(url_for('employees.index'))

