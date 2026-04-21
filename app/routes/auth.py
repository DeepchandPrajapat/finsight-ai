from flask import Blueprint, request, jsonify
from ..models import User
from ..extensions import db, bcrypt
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/auth/register", methods=["POST"])
def register():
    data = request.json

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    # check if all fields provided
    if not name or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    # check if user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "Email already registered"}), 400

    # hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    # create new user
    user = User(name=name, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Registration successful"}), 201


@auth_bp.route("/api/auth/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    # find user
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Invalid email or password"}), 401

    # verify password
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Invalid email or password"}), 401

    # create JWT token
    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token,
        "name": user.name,
        "email": user.email
    }), 200