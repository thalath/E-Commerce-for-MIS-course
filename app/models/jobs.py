from extensions import db

class Jobs(db.Model):
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    min_salary = db.Column(db.Float)
    max_salary = db.Column(db.Float)
    
    def __repr__(self) -> str:
        return f"<{self.job_title}>"