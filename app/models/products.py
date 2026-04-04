from extensions import db

class Products(db.Model):
    __tablename__ = 'products'
    code = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    unit_meansure = db.Column(db.String(30), nullable=False)
    reorder_level = db.Column(db.Integer, nullable=False)
    sell_price = db.Column(db.Float, nullable=False)
    cost_price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Integer)
    images = db.Column(db.LargeBinary)
    
    def __repr__(self) -> str:
        return f"<Product {self.name}>"
    