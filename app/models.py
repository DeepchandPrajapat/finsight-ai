from datetime import datetime
from .extensions import db
from sqlalchemy.sql import func

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)

    # relationships
    expenses = db.relationship("Expense", backref="user", lazy=True, foreign_keys="Expense.user_id")
    budgets = db.relationship("Budget", backref="user", lazy=True, foreign_keys="Budget.user_id")

class Expense(db.Model):
    __tablename__="expenses"
    
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    amount = db.Column(db.Float,nullable=False)
    category = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime,default=func.now(),nullable=False)
    updated_at = db.Column(db.DateTime,default=func.now(),onupdate=func.now(),nullable=False)
    
class Budget(db.Model):
    __tablename__ = "budgets"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('month', 'year', name='unique_month_year'),
    )    

