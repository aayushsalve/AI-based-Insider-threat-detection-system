# AI-Based Insider Threat Detection System

## 🎯 Overview

An advanced machine learning system designed to detect insider threats in organizations through behavioral anomaly detection and risk scoring. The system uses a **Hybrid Machine Learning approach** combining IsolationForest and RandomForest algorithms for accurate threat identification.

**Current Models**: 
- ✅ IsolationForest (Primary Detector - 70% weight)
- ✅ RandomForest (Validation Layer - 30% weight)
- ✅ Hybrid Risk Scoring System

---

## 🔑 Key Features

✅ **Hybrid Model Architecture**
- Combines unsupervised (IsolationForest) and supervised (RandomForest) learning
- Early detection of novel threats
- High-confidence threat validation

✅ **Behavioral Analysis**
- File access pattern monitoring
- Login behavior tracking
- Sensitive data access detection

✅ **Risk Scoring**
- Multi-factor risk assessment
- Real-time threat scoring (0-10 scale)
- Confidence metrics

✅ **Data Processing**
- Automated feature engineering
- Anomaly detection pipeline
- Comprehensive reporting

---

## 📊 Architecture

```
User Activity Data
    ↓
Feature Engineering
    ↓
┌─────────────────────────────────────┐
│   HYBRID ANOMALY DETECTION          │
│  ┌──────────────────────────────┐   │
│  │ IsolationForest (70%)        │   │
│  │ • Unsupervised detection     │   │
│  │ • Anomaly scoring            │   │
│  └──────────────────────────────┘   │
│  ┌──────────────────────────────┐   │
│  │ RandomForest (30%)           │   │
│  │ • Supervised validation      │   │
│  │ • Threat confirmation        │   │
│  └──────────────────────────────┘   │
│         ↓ Weighted Voting ↓         │
│   Combined Threat Score (0-1)       │
└─────────────────────────────────────┘
    ↓
Risk Scoring Engine
    ↓
Threat Report & Alerts
```

---

## 📂 Project Structure

```
Insider Threat Detection/
├── README.md                      # Main documentation
├── HYBRID_MODEL_ARCHITECTURE.md   # Detailed model documentation
├── requirements.txt               # Python dependencies
├── test_hybrid_model.py          # Hybrid model testing script
│
├── Data/
│   ├── Raw/                      # Original data
│   ├── Processed/                # Cleaned data
│   ├── Models/                   # Trained models
│   │   ├── isolation_forest_model.pkl
│   │   └── random_forest_model.pkl
│   └── *.csv                     # Dataset files
│
├── src/                          # Source code
│   ├── main.py                   # Main execution
│   ├── mode_training.py          # Hybrid model training
│   ├── anomaly_detection.py      # Hybrid anomaly detection
│   ├── model_evaluation.py       # Model evaluation
│   ├── data_processing.py        # Data preprocessing
│   ├── feature_engineering.py    # Feature creation
│   ├── risking_scoring.py        # Risk calculation
│   ├── utils.py                  # Utility functions
│   └── preprocessing.py          # Data cleaning
│
└── Notebook/
    └── exploration.ipynb         # Data exploration
```

---

## 🚀 Getting Started

### **Prerequisites**
- Python 3.8+
- pip or conda

### **Installation**

1. Clone the repository:
```bash
git clone https://github.com/aayushsalve/AI-based-Insider-threat-detection-system.git
cd "Insider Threat Detection"
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### **Training the Hybrid Model**

```bash
# Option 1: Using test script (recommended)
python test_hybrid_model.py

# Option 2: Using training script
python src/mode_training.py

# Option 3: Using main script
python src/main.py
```

### **Evaluating Models**

```bash
python src/model_evaluation.py
```

---

## 📈 Model Comparison

| Metric | IsolationForest | RandomForest | Hybrid |
|--------|-----------------|--------------|--------|
| Unsupervised Detection | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Labeled Data Handling | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Accuracy | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Confidence | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 📊 Usage Example

```python
import pandas as pd
from src.data_processing import preprocess_data
from src.anomaly_detection import detect_anomalies
from src.risking_scoring import compute_risk

# 1. Load and preprocess data
df = pd.read_csv('Data/simulated_activity.csv')
processed_df = preprocess_data(df)

# 2. Detect anomalies using hybrid model
results_df = detect_anomalies(processed_df)

# 3. Calculate risk scores
risk_df = compute_risk(results_df)

# 4. Get high-risk users
high_risk = risk_df[risk_df['risk_score'] > 7.0]
print(high_risk[['user_id', 'risk_score', 'anomaly_score', 'confidence']])
```

---

## 🔧 Configuration

### **Model Parameters**

**IsolationForest**:
```python
IsolationForest(
    contamination=0.1,      # Expected anomaly ratio
    n_estimators=100,       # Number of trees
    random_state=42         # Reproducibility
)
```

**RandomForest**:
```python
RandomForestClassifier(
    n_estimators=100,       # Number of trees
    max_depth=15,          # Maximum tree depth
    min_samples_split=5     # Minimum samples to split
)
```

### **Hybrid Weights**

Default: `70% IsolationForest + 30% RandomForest`

Adjust in `src/anomaly_detection.py`:
```python
hybrid_scores = (iso_scores_normalized * 0.7) + (rf_anomaly_prob * 0.3)
```

### **Threat Threshold**

Default: `score > 0.5` = Threat

Modify in `src/anomaly_detection.py` or `src/risking_scoring.py`

---

## 📚 Documentation

- **[HYBRID_MODEL_ARCHITECTURE.md](HYBRID_MODEL_ARCHITECTURE.md)** - Detailed technical documentation
- **[src/](src/)** - Well-commented source code
- **[Notebook/exploration.ipynb](Notebook/exploration.ipynb)** - Data exploration notebook

---

## 🧪 Testing

```bash
# Run all tests
python test_hybrid_model.py

# Test individual components
python src/model_evaluation.py
python src/main.py
```

---

## 📊 Performance Metrics

Based on test dataset (30 samples):

**IsolationForest**:
- Anomalies Detected: 3
- Average Score: 0.618

**RandomForest**:
- Average Probability: 0.304

**Hybrid Model**:
- Anomalies Detected: 9 (better coverage)
- Average Score: 0.523
- Weighted confidence: Both models' strengths

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open Pull Request

---

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details

---

## 👤 Author

**Aayush Salve**
- Email: aay.sal.rt22@dypatil.edu
- GitHub: [aayushsalve](https://github.com/aayushsalve)

---

## 🔗 Repository

[AI-based-Insider-threat-detection-system](https://github.com/aayushsalve/AI-based-Insider-threat-detection-system)

---

## 📞 Support

For issues, questions, or suggestions:
- Create an Issue on GitHub
- Email: aay.sal.rt22@dypatil.edu

---

**Status**: ✅ Active Development | Last Updated: February 16, 2026
