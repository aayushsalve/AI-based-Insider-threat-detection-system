# INSIDER THREAT DETECTION SYSTEM

An academic and deployment-oriented prototype for insider threat detection using hybrid machine learning, weighted risk scoring, report generation, and a Flask-based SOC dashboard.

## Project Status

This repository currently reflects a working project state with:

- a hybrid anomaly detection concept built around IsolationForest and RandomForest
- a dashboard application for demo monitoring and response simulation
- generated model, threshold, and reporting artifacts
- viva, report, and black-book documentation for the current submission stage

Current validated metrics referenced by the reporting pipeline:

- Precision: 88.0%
- Recall: 78.2%
- F1-score: 82.0%
- Accuracy: 92.0%

## Core Capabilities

### Hybrid Detection Logic

- anomaly-oriented detection with IsolationForest
- supervised validation with RandomForest
- weighted hybrid scoring for stronger prioritization

### Risk Scoring

- 0-10 risk score output
- four-factor weighted scoring model
- Critical, High, Medium, and Low risk classification

### Dashboard and Demo Operations

- Flask dashboard with login-based access
- live risk leaderboard and recent activity view
- admin controls for restrict, block, unblock, and role updates
- JSON endpoints for demo integrations

### Reporting and Evaluation

- cross-validation summaries
- threshold optimization outputs
- executive summary generation
- exportable recommendation and performance reports

## Current Architecture

```text
User Activity and Security Signals
    -> preprocessing and feature engineering
    -> anomaly detection and supervised validation
    -> weighted hybrid score
    -> 0-10 risk scoring engine
    -> dashboard, reports, and API responses
```

The current dashboard implementation in `src/app.py` uses a four-component weighted risk model:

- Anomaly: 40%
- Sensitive access: 30%
- Login anomaly: 20%
- Behavioral signal: 10%

## Repository Layout

```text
Insider Threat Detection/
├── app.py                         # Root Flask launcher
├── demo_server.py                 # LAN demo launcher
├── run_app.bat                    # Windows helper to start the app
├── train_models.py                # Model training script
├── run_detection.py               # Detection runner
├── test_hybrid_model.py           # Hybrid model test script
├── HYBRID_MODEL_ARCHITECTURE.md   # Architecture notes
├── README_PORTABLE.md             # Portable/demo run guide
├── Data/
│   ├── Models/                    # Trained model artifacts
│   ├── Processed/                 # Processed datasets
│   ├── production_models/         # Production-oriented outputs
│   └── *.csv                      # Project datasets
├── docs/
│   ├── SOC_USER_GUIDE.md          # Current operator guide
│   ├── generate_final_viva_ppt.py # Viva presentation generator
│   └── *.md                       # Project documentation
├── reports/                       # Generated metrics and summaries
└── src/
    ├── app.py                     # Main dashboard app
    ├── model_training.py          # Training logic
    ├── model_evaluation.py        # Evaluation logic
    ├── generate_final_report.py   # Final reporting utility
    ├── optimize_threshold.py      # Threshold tuning
    ├── data_processing.py         # Data preparation
    ├── feature_engineering.py     # Feature engineering
    ├── drift_monitor.py           # Drift monitoring helpers
    ├── enhanced_risk_scoring.py   # Risk scoring implementation
    └── templates/                 # Dashboard templates
```

## Running The Project

### Option 1: Start The Dashboard

```powershell
python app.py
```

This launches the Flask application exposed by the project root entry point.

### Option 2: Start The LAN Demo Server

```powershell
python demo_server.py
```

Use this when you want to access the dashboard from another device on the same network.

### Option 3: Use The Windows Helper

```powershell
run_app.bat
```

This script creates `venv` if needed, installs minimal demo dependencies, and starts the application.

## Recommended Manual Environment Setup

```powershell
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install flask flask-cors pandas numpy scikit-learn joblib plotly python-pptx
```

## Demo Access

The current demo accounts defined in the Flask application are:

- Admin: `aayush` / `aayushadminpass`
- User: `amit` / `adminpass`
- User: `priya` / `analystpass`

Default dashboard URL:

```text
http://127.0.0.1:5000
```

## Active Demo API Surface

The current Flask app exposes:

- `GET /api/v1/risk`
- `GET /api/v1/threats`

These endpoints are demo-oriented and currently do not enforce API-key authentication.

## Training, Detection, and Reporting Commands

Examples of useful current commands:

```powershell
python train_models.py
python run_detection.py
python test_hybrid_model.py
python src\generate_final_report.py
python src\optimize_threshold.py
```

## Key Documentation

- `HYBRID_MODEL_ARCHITECTURE.md`
- `README_PORTABLE.md`
- `docs/SOC_USER_GUIDE.md`
- `docs/generate_final_viva_ppt.py`

## Author

Aayush Salve

- Email: aayushsalve15@gmail.com
- GitHub: https://github.com/aayushsalve

## Support

For repository questions, documentation corrections, or project review requests:

- create an issue in the GitHub repository
- contact: aayushsalve15@gmail.com

## Repository

https://github.com/aayushsalve/AI-based-Insider-threat-detection-system
