from flask import Blueprint, request, jsonify
from ..models import Budget
from ..extensions import db

budget_bp = Blueprint("budget", __name__)

@budget_bp.route("/api/budget", methods=["POST"])
def set_budget():
    data = request.json

    amount = data.get("amount")
    month = data.get("month")
    year = data.get("year")

    budget = Budget.query.filter_by(month=month, year=year).first()

    if budget:
        budget.amount = amount
    else:
        budget = Budget(amount=amount, month=month, year=year)
        db.session.add(budget)

    db.session.commit()

    return jsonify({"message": "Budget saved"})      

@budget_bp.route("/api/budget", methods=["GET"])
def get_budget():
    month = request.args.get("month", type=int)
    year = request.args.get("year", type=int)

    budget = Budget.query.filter_by(month=month, year=year).first()

    if budget:
        return jsonify({"amount": budget.amount})
    else:
        return jsonify({"amount": 0})  