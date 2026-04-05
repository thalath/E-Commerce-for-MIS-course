from typing import List, Optional
from app.models.employees import Employees
from extensions import db
from app.models.jobs import Jobs

class EmployeeServices:
    
    @staticmethod
    def get_all() -> List[Employees]:
        return Employees.query.order_by(Employees.id.asc()).all()
    
    
    @staticmethod
    def get_by_id(id: int) -> Optional[Employees]:
        return Employees.query.get(id)
    
    @staticmethod
    def create(data: dict, photo: str) -> Employees:
        
        emp = Employees(
            name = data['name'],
            gender = data['gender'],
            birthdate=data['birthdate'],
            job_id = data.get('job_id'),
            address = data.get("address", "_"),
            phone = data['phone'],
            salary = data['salary'],
            remarks = data['remarks'],
        )
        
        emp.photo = photo
        db.session.add(emp)
        db.session.commit()
        return emp
    
    @staticmethod
    def update(emp: Employees, data: dict, file: str, ) -> Employees:
        emp.name = data['name']
        emp.gender = data['gender']
        emp.birthdate = data['birthdate']
        emp.address = data['address']
        emp.phone = data['phone']
        emp.remarks = data['remarks']
        emp.salary = data['salary']
        emp.job_id = data.get('job_id', None)
        emp.photo = file
        db.session.commit()
        return emp
        
        
    @staticmethod
    def delete(emp: Employees) -> None:
        db.session.delete(emp)
        db.session.commit()