from flask import Blueprint, request, jsonify
from ..models import Expense
from ..extensions import db

expenses_bp = Blueprint(
    "expenses",
    __name__,
    url_prefix="/api/expenses"
)
