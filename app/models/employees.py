from extensions import db


class Employees(db.Model):
    __tablename__ = "EMPLOYEES"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(6))
    birthdate = db.Column(db.DATE)
    job_id = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(150))
    phone = db.Column(db.String(15), nullable=False)
    salary = db.Column(db.Integer)
    remarks = db.Column(db.String(20))
    photo = db.Column(db.LargeBinary)
    
    def __repr__(self) -> str:
        return f"<{self.name}>"
    