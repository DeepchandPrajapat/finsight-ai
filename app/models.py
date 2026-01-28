from datetime import datetime
from .extensions import db

class Expense(db.model):
    __tablename__="expenses"
    
    id = db.Column(db.Integer,primary_key=True)
    amount = db.Column(db.Float,nullable=False)
    category = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(255))
    date = db.Column(db.DateTime,default=datetime.utcnow)