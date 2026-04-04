from extensions import db

class Categories(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    remarks = db.Column(db.String(255))

    def __repr__(self) -> str:
        return f"<category {self.name}>"
