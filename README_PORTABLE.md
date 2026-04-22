# Portable Run Instructions

This explains how to run the Insider Threat Detection demo from removable media (USB/pendrive) on another machine.

Prerequisites
- Python 3.8 or newer installed on the target machine and available on `PATH`.

Windows (recommended):

1. Copy the whole project folder to the target machine (or insert the USB drive).
2. Open Command Prompt and change directory to the project root (where `run_app.bat` is located):

```powershell
cd "D:\path\to\Insider Threat Detection"
```

3. Run the helper script which will create a virtualenv, install dependencies, and start the app:

```powershell
run_app.bat
```

4. Open a browser at `http://127.0.0.1:5000`.

Linux / macOS (manual):

1. Copy the project to the machine.
2. In a terminal, create and activate a venv, install deps, and run:

```bash
cd "/path/to/Insider Threat Detection"
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install flask flask-cors pandas plotly
python src/app.py
```

Notes & tips
- The `run_app.bat` installs minimal dependencies used by the demo; if you extend the project, update the `pip install` line accordingly.
- For presentations, create a small screenshot or list of demo accounts (Aayush / aayushpass is admin).
- Bundling into a single executable is possible (PyInstaller) but not included here to keep the USB small and cross-platform.
