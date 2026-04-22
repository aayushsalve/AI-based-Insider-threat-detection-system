# Portable Run Guide

This guide explains how to run the current project demo on another Windows machine or from removable media.

## Recommended Use Case

Use the portable flow when you want to:

- demonstrate the dashboard during viva or review sessions
- run the app on another laptop without recreating the setup manually from scratch
- expose the demo over local Wi-Fi using `demo_server.py`

## Windows Quick Start

1. Copy the full project folder to the target machine.
2. Open PowerShell or Command Prompt in the project root.
3. Run:

```powershell
run_app.bat
```

This script will:

- create `venv` if it does not already exist
- activate the environment
- install the minimal packages used by the dashboard flow
- start the Flask app

After startup, open:

```text
http://127.0.0.1:5000
```

## Demo Credentials

The current demo accounts are:

- Admin: `aayush` / `aayushadminpass`
- User: `amit` / `adminpass`
- User: `priya` / `analystpass`

## Local Network Demo

If you want another device on the same network to open the dashboard, run:

```powershell
python demo_server.py
```

Or use a custom port:

```powershell
python demo_server.py --port 8080
```

The script prints both local and LAN URLs.

## Manual Setup

If you do not want to use `run_app.bat`, set the environment up manually:

```powershell
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install flask flask-cors pandas numpy scikit-learn joblib plotly python-pptx
python app.py
```

## Notes

- The repository currently includes generated reports, trained models, notebooks, and presentation material alongside the source code.
- `run_app.bat` installs only the packages needed for the dashboard demo path. If you plan to execute training or reporting scripts, install the broader package set shown above.
- Before carrying the project to another machine, confirm that the `Data`, `docs`, and `reports` directories contain the artifacts you want to present.

## Support

For setup issues or demo preparation help, contact `aayushsalve15@gmail.com`.
