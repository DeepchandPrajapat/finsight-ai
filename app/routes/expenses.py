from flask import Blueprint, request, jsonify
from ..models import Expense
from ..extensions import db

expenses_bp = Blueprint(
    "expenses",
    __name__,
    url_prefix="/api/expenses"
)

@expenses_bp.route("/", methods=["POST"])
def create_expense():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    amount = data.get("amount")
    category = data.get("category")
    description = data.get("description")

    if not amount or not category:
        return jsonify({"error": "Amount and category are required"}), 400

    expense = Expense(
        amount=amount,
        category=category,
        description=description
    )

    db.session.add(expense)
    db.session.commit()

    return jsonify({
        "message": "Expense created successfully",
        "id": expense.id
    }), 201