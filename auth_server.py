from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests  # do komunikacji z Zuck

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db = SQLAlchemy(app)

# Model użytkownika
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    imei = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='inactive')  # active, inactive, pending
    last_login = db.Column(db.DateTime, nullable=True)

# Funkcja wysyłająca dane do Zuck w celu weryfikacji
def verify_with_zuck(username, imei):
    url = "https://www.facebook.com/share/16q6Jvi4A2/"  # Adres API Zuck, zmień na prawdziwy
    payload = {
        "username": username,
        "imei": imei
    }
    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        data = response.json()
        # Załóżmy, że zwraca {"verified": true/false, "message": "..."}
        return data.get("verified", False), data.get("message", "")
    except Exception as e:
        return False, f"Error contacting Zuck: {str(e)}"

# Endpoint rejestracji
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    imei = data.get('imei')

    if not username or not imei:
        return jsonify({"message": "Missing username or IMEI"}), 400

    if User.query.filter_by(imei=imei).first():
        return jsonify({"message": "IMEI already registered"}), 400

    # Weryfikacja z Zuck
    verified, message = verify_with_zuck(username, imei)
    if not verified:
        return jsonify({"message": f"Verification failed: {message}"}), 403

    new_user = User(username=username, imei=imei, status='active', last_login=datetime.utcnow())
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered and verified successfully"}), 201
    except Exception as e:
        return jsonify({"message": "Database error", "error": str(e)}), 500

# Endpoint logowania
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    imei = data.get('imei')

    user = User.query.filter_by(imei=imei).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    # Weryfikacja z Zuck
    verified, message = verify_with_zuck(user.username, imei)
    if not verified:
        user.status = 'inactive'
        db.session.commit()
        return jsonify({"message": f"Verification failed: {message}"}), 403

    user.status = 'active'
    user.last_login = datetime.utcnow()
    db.session.commit()

    return jsonify({"message": "Login successful", "username": user.username}), 200

# Endpoint wylogowania
@app.route('/logout', methods=['POST'])
def logout():
    data = request.json
    imei = data.get('imei')

    user = User.query.filter_by(imei=imei).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    user.status = 'inactive'
    db.session.commit()

    return jsonify({"message": "Logout successful"}), 200

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)