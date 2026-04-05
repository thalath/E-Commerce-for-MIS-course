from typing import List, Optional
from app.models.jobs import Jobs
from extensions import db

class JobServices:
    
    @staticmethod
    def get_all() -> List[Jobs]:
        return Jobs.query.order_by(Jobs.id.asc()).all()
    
    @staticmethod
    def get_by_id(id: int) -> Optional[Jobs]:
        return Jobs.query.get(id)
    
    
    @staticmethod
    def create(data: dict) -> Jobs:

        job = Jobs(
            title = data['title'],
            min_salary = data['min_salary'],
            max_salary = data['max_salary']
        )
        
        db.session.add(job)
        db.session.commit()
        return job


    @staticmethod
    def update(job: Jobs, data: dict) -> Jobs:
        
        job.title = data['title']
        job.min_salary = data['min_salary']
        job.max_salary = data['max_salary']

        db.session.commit()
        return job

    @staticmethod
    def delete(job: Jobs) -> None:
        db.session.delete(job)
        db.session.commit()
        
        