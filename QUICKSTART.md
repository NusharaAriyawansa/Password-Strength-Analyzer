# Quick Start Guide

Get the Password Strength Analyzer running in 5 minutes!

## ⚡ The Fastest Way

### On macOS/Linux:
```bash
# 1. Navigate to project directory
cd password_analyzer

# 2. Make run script executable
chmod +x run.sh

# 3. Run the startup script
./run.sh
```

### On Windows:
```bash
# 1. Navigate to project directory
cd password_analyzer

# 2. Double-click run.bat
# OR run in terminal:
run.bat
```

## 🔧 Manual Setup (If Scripts Don't Work)

### Step 1: Create Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python app.py
```

### Step 4: Open in Browser
```
http://127.0.0.1:5000
```

## 🧪 Test It Immediately

Try these passwords to see the analyzer in action:

**Very Weak Passwords** (Should score < 20):
- `abc`
- `password`
- `123456`

**Weak Passwords** (Should score 20-40):
- `Password1`
- `Admin123`
- `Qwerty12`

**Good Passwords** (Should score 40-60):
- `MyPass@123`
- `SecureP@ss2024`

**Strong Passwords** (Should score 60-80):
- `MySecure@Pass2024!`
- `C0mpl3x!Password#2024`

**Very Strong Passwords** (Should score 80-100):
- `D$fJk9@mL2#pQwR!vNx3$yZaB4&cEdFg5`
- `Tr0pic@lThund3r!Storm2024$Secure`

## 📁 Project Structure

```
password_analyzer/
├── app.py                    ← Main application (start here)
├── password_checker.py       ← Validation logic
├── requirements.txt          ← Dependencies
├── run.sh                    ← Startup script (macOS/Linux)
├── run.bat                   ← Startup script (Windows)
│
├── templates/
│   └── index.html           ← Web page
│
└── static/
    ├── css/style.css        ← Styling
    └── js/script.js         ← Real-time validation
```

## 🔌 How It Works

1. **User Types Password** → Triggers JavaScript event
2. **JavaScript Sends Request** → POST to `/api/check-password`
3. **Flask Backend Analyzes** → Runs validation algorithms
4. **Returns JSON Response** → Contains score, feedback, issues
5. **JavaScript Displays Results** → Updates UI in real-time

## 🛠️ Common Issues & Solutions

### Issue: "Port 5000 is already in use"
**Solution**: Change port in `app.py`:
```python
app.run(debug=True, host='127.0.0.1', port=5001)
```

### Issue: "Module not found" error
**Solution**: Make sure virtual environment is activated:
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Issue: "No module named 'flask'"
**Solution**: Install requirements:
```bash
pip install -r requirements.txt
```

### Issue: JavaScript not loading
**Solution**: Check Flask is running and open browser console (F12)

## 🚀 What to Try Next

1. **Edit Styling**: Modify `static/css/style.css` colors
2. **Add More Passwords**: Update `common_passwords` in `password_checker.py`
3. **Change Messages**: Edit feedback messages in `password_checker.py`
4. **Add Features**: Implement password generator (bonus!)

## 🎓 Learn More

- Read `README.md` for detailed documentation
- Read `CV_PROJECT_GUIDE.md` for portfolio tips
- Check `password_checker.py` to understand validation logic
- Check `static/js/script.js` to understand frontend logic

## 💡 Pro Tips

1. **Test in Incognito Mode**: Avoid cached versions
2. **Use Browser DevTools**: F12 to debug JavaScript
3. **Check Network Tab**: See API requests/responses
4. **Read Console Errors**: JavaScript errors logged here
5. **Restart Server**: If changes don't show, restart Flask

## 🆘 Still Having Issues?

1. Make sure Python 3.8+ is installed
2. Verify all files are in correct directories
3. Check that port 5000 is not in use
4. Try a different port (5001, 5002, etc.)
5. Delete `__pycache__` folder and try again

## 🎉 You're All Set!

The application is now running. Start typing passwords and watch the real-time analysis!

---

**Questions?** Check the README.md or review the code with comments.
