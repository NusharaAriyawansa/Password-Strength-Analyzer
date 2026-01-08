from flask import Flask, render_template, request, jsonify
import hashlib
import requests
from password_checker import PasswordChecker
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
password_checker = PasswordChecker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/check-password', methods=['POST'])
def check_password():
    """
    API endpoint to analyze password strength
    Returns: JSON with strength score, feedback, and vulnerabilities
    """
    data = request.get_json()
    password = data.get('password', '')
    
    if not password:
        return jsonify({
            'strength': 0,
            'score': 0,
            'message': 'Password is empty',
            'feedback': [],
            'breached': False
        })
    
    # Check password strength
    result = password_checker.check_strength(password)
    
    # Check if password is in breach database (optional, can be slow)
    is_breached = password_checker.check_breach(password)
    result['breached'] = is_breached
    
    return jsonify(result)

@app.route('/api/common-passwords', methods=['GET'])
def get_common_passwords():
    """
    Returns list of common passwords for client-side checking
    """
    common_passwords = password_checker.get_common_passwords()
    return jsonify({'common_passwords': common_passwords})

@app.route('/api/password-tips', methods=['GET'])
def get_tips():
    """
    Returns password security tips
    """
    tips = [
        "Use at least 12 characters for better security",
        "Mix uppercase, lowercase, numbers, and symbols",
        "Avoid using dictionary words or personal information",
        "Don't reuse passwords across different sites",
        "Use a password manager to store your passwords securely",
        "Avoid common patterns like 'password123' or 'abc123'",
        "Enable two-factor authentication when available"
    ]
    return jsonify({'tips': tips})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
