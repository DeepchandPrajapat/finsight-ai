from flask import Blueprint, request, jsonify,current_app
from ..models import Expense
from ..extensions import db
import json
from google import genai

expenses_bp = Blueprint(
    "expenses",
    __name__,
    url_prefix="/api/expenses"
)

budget_bp = Blueprint("budget", __name__)

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
    
@expenses_bp.route("/",methods=["GET"])
def get_all_expenses():
    expenses = Expense.query.order_by(Expense.created_at.desc()).all()

    result = []
    for expense in expenses:
        result.append({
            "id": expense.id,
            "amount": expense.amount,
            "category": expense.category,
            "description": expense.description,
            "created_at": expense.created_at.isoformat(),
            "updated_at": expense.updated_at.isoformat()
        })

    return jsonify(result), 200

@expenses_bp.route("/<int:expense_id>",methods=["GET"])
def get_expense(expense_id):
    expense = Expense.query.get(expense_id)
    
    if not expense:
        return jsonify({"error": "Expense not found"}), 404
    
    return jsonify({
    "id": expense.id,
    "amount": expense.amount,
    "category": expense.category,
    "description": expense.description,
    "created_at": expense.date.isoformat(),
    "updated_at": expense.date.isoformat()
}), 200

@expenses_bp.route("/<int:expense_id>", methods=["PATCH"])
def update_expense(expense_id):
    expense = Expense.query.get(expense_id)

    if not expense:
        return jsonify({"error": "Expense not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    expense.amount = data.get("amount", expense.amount)
    expense.category = data.get("category", expense.category)
    expense.description = data.get("description", expense.description)

    db.session.commit()

    return jsonify({"message": "Expense updated successfully"}), 200

@expenses_bp.route("/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)
    
    if not expense:
        return jsonify({"error": "Expense not found"}), 404
    
    db.session.delete(expense)
    db.session.commit()
    
    return jsonify({"message": "Expense deleted successfully"}), 200


@expenses_bp.route("/ai-insights", methods=["GET"])
def get_ai_insights():
    expenses = Expense.query.all()

    if not expenses:
        return jsonify({"error": "No expenses found"}), 404

    expense_text = ""
    for expense in expenses:
        expense_text += f"Category: {expense.category}, Amount: {expense.amount}, Description: {expense.description}, Date: {expense.created_at.strftime('%Y-%m-%d')}\n"

    client = genai.Client(api_key=current_app.config['GEMINI_API_KEY'])

    prompt = f"""
        Here are my expenses in Indian Rupees (INR):
        {expense_text}

        Analyse these expenses and respond ONLY with a JSON object like this:
        {{
            "insight": "one sentence about spending pattern",
            "recommendation": "one sentence tip to save money",
            "alert": "one sentence about any unusual or high spending"
        }}

        Rules:
        - respond with ONLY the JSON object
        - no extra text before or after
        - no markdown or code blocks
        - keep each value to ONE sentence
        - use INR (₹) for amounts
    """


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    try:
        data = json.loads(response.text)
        return jsonify({
            "insight": data["insight"],
            "recommendation": data["recommendation"],
            "alert": data["alert"]
        }), 200
    except:
        return jsonify({
            "insight": "Could not analyse expenses.",
            "recommendation": "Please try again.",
            "alert": "No alerts at this time."
        }), 200
        
