@echo off
REM Portable runner for Windows: creates venv (if missing), installs deps, and runs the app
SETLOCAL ENABLEDELAYEDEXPANSION
cd /d "%~dp0"
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
)
echo Activating virtual environment...
call "venv\Scripts\activate.bat"
echo Upgrading pip and installing dependencies...
python -m pip install --upgrade pip
python -m pip install flask flask-cors pandas plotly
echo Starting the app...
python src\app.py
ENDLOCAL
