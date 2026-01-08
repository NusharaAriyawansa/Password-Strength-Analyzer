@echo off
REM Password Strength Analyzer - Windows Startup Script

echo.
echo 0x1F510 Password Strength Analyzer
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo + Python found: %PYTHON_VERSION%
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Preparing virtual environment...
    python -m venv venv
    echo + Virtual environment created
)

REM Activate virtual environment
echo 2699 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo 1F4E5 Installing dependencies...
pip install -r requirements.txt -q
echo + Dependencies installed

echo.
echo ================================
echo 1F680 Starting application...
echo 1F4F1 Open your browser and go to: http://127.0.0.1:5000
echo 2328 Press Ctrl+C to stop the server
echo ================================
echo.

REM Run the Flask app
python app.py

pause
