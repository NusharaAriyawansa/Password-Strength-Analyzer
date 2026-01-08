# Password Strength Analyzer
A comprehensive web application that evaluates password strength in real-time with multiple security checks.

## Features
- **Real-time Analysis**: Get instant feedback as you type
- **Complexity Checking**: Validates uppercase, lowercase, numbers, and special characters
- **Length Analysis**: Recommends optimal password length
- **Pattern Detection**: Detects sequential characters and repetitions
- **Dictionary Check**: Identifies common passwords and dictionary words
- **Breach Detection**: Uses Have I Been Pwned API (k-anonymity model) to check if password was in data breaches
- **Entropy Calculation**: Calculates password entropy for security strength
- **Security Tips**: Provides actionable recommendations
- **Privacy First**: All analysis done locally, password never sent to servers (except optional breach check)

## Technical Stack
- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **API**: Have I Been Pwned API for breach checking
- **Architecture**: MVC pattern with async API calls

## Dependencies
- **Flask==2.3.3**: Web framework
- **requests==2.31.0**: HTTP library for breach checking
- **python-dotenv==1.0.0**: Environment variable management

## Project Structure

```
password_analyzer/
│
├── app.py                          # Main Flask application
├── password_checker.py             # Password validation logic
├── requirements.txt                # Python dependencies
│
├── templates/
│   └── index.html                 # Main HTML template
│
├── static/
│   ├── css/
│   │   └── style.css              # Styling
│   └── js/
│       └── script.js              # Real-time validation JavaScript
│
└── README.md                       # This file
```

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone/Create Project Directory
```bash
mkdir password_analyzer
cd password_analyzer
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

The application will start on `http://127.0.0.1:5000`

## 💻 Usage

1. Open your browser and navigate to `http://localhost:5000`
2. Enter a password in the input field
3. Get real-time feedback on:
   - Password strength (Very Weak to Very Strong)
   - Strength score (0-100)
   - What's good about the password
   - Issues that need to be fixed
   - Whether the password has been in a breach
4. Use the suggestions to improve your password

## 🔒 Security Features

### 1. Length Analysis
- Minimum: 8 characters
- Recommended: 12+ characters
- Optimal: 16+ characters

### 2. Complexity Scoring
- Uppercase letters (5 points)
- Lowercase letters (5 points)
- Numbers (5 points)
- Special symbols (10 points)

### 3. Pattern Detection
- Detects sequential characters (e.g., 123, abc)
- Identifies repeated characters (e.g., aaa)
- Checks against common passwords database

### 4. Dictionary Check
- 40+ most common passwords
- Detects passwords containing dictionary words
- Case-insensitive matching

### 5. Entropy Calculation
- Estimates password entropy in bits
- Considers character set size
- Adjusts points based on entropy level

### 6. Breach Database Check
- Uses Have I Been Pwned API
- K-anonymity model: only first 5 characters of SHA-1 hash sent
- Your full password NEVER sent to external servers

## 📊 Scoring System

| Score Range | Level | Recommendation |
|-------------|-------|-----------------|
| 80-100 | Very Strong | Excellent choice |
| 60-79 | Strong | Good, with room for improvement |
| 40-59 | Good | Acceptable, but improve it |
| 20-39 | Weak | Not recommended |
| 0-19 | Very Weak | Must improve |



