from datetime import datetime
from .extensions import db
from sqlalchemy.sql import func

class Expense(db.Model):
    __tablename__="expenses"
    
    id = db.Column(db.Integer,primary_key=True)
    amount = db.Column(db.Float,nullable=False)
    category = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime,default=func.now(),nullable=False)
    updated_at = db.Column(db.DateTime,default=func.now(),onupdate=func.now(),nullable=False)