# Hybrid Insider Threat Detection Model

## Overview
This project implements a **Hybrid Machine Learning Model** for insider threat detection, combining the strengths of two complementary algorithms:
- **IsolationForest** (70% weight) - Primary unsupervised anomaly detector
- **RandomForest** (30% weight) - Secondary supervised validator

---

## Architecture

### **Model 1: IsolationForest (Primary Detector)**

**Purpose**: Detect novel/unknown threats through unsupervised anomaly detection

**Why IsolationForest?**
- ✅ No labeled data required
- ✅ Detects behavioral anomalies automatically
- ✅ Excellent for insider threat detection (threats are often unique)
- ✅ Fast and efficient for continuous monitoring

**Configuration**:
```python
IsolationForest(
    contamination=0.1,      # Expect 10% anomalies
    random_state=42,        # Reproducibility
    n_estimators=100        # 100 isolation trees
)
```

**Output**: Anomaly scores (0-1) where higher scores indicate anomalies

---

### **Model 2: RandomForest (Validation Layer)**

**Purpose**: Validate and confirm suspicious cases detected by IsolationForest

**Why RandomForest?**
- ✅ Supervised classification for higher confidence
- ✅ Explainable (feature importance shows what triggered alert)
- ✅ Works better with labeled training data
- ✅ Provides probability scores

**Configuration**:
```python
RandomForestClassifier(
    n_estimators=100,       # 100 trees
    random_state=42,        # Reproducibility
    max_depth=15,           # Tree depth
    min_samples_split=5     # Minimum samples to split
)
```

**Output**: Probability scores (0-1) indicating threat likelihood

---

## Hybrid Decision Logic

### **Weighted Voting System**
```
Hybrid Score = (IsolationForest Score × 0.7) + (RandomForest Score × 0.3)
```

### **Decision Threshold**
- **Threat Alert**: Hybrid Score > 0.5
- **Normal Behavior**: Hybrid Score ≤ 0.5

### **Output Metrics**
For each user activity, the system calculates:
1. `anomaly_score` - Combined threat score (0-1)
2. `iso_score` - IsolationForest score (0-1)
3. `rf_score` - RandomForest probability (0-1)
4. `confidence` - Confidence level (0-1)
5. `anomaly` - Binary prediction (0=Normal, 1=Threat)

---

## Risk Scoring Integration

The hybrid model results are integrated into the overall risk score calculation:

```python
Risk Score = (Anomaly Score × 40%) + 
             (Sensitive Access × 40%) + 
             (Confidence × 20%)
```

**Components**:
- **Anomaly Score (40%)**: Primary threat indicator
- **Sensitive File Access (40%)**: File access patterns
- **Confidence (20%)**: Model certainty

**Final Score Range**: 0-10

---

## Advantages of Hybrid Approach

| Aspect | IsolationForest | RandomForest | Hybrid |
|--------|-----------------|--------------|--------|
| **Detects Unknown Threats** | ✅ Excellent | ⚠️ Good | ✅ Excellent |
| **Handles Labeled Data** | ❌ No | ✅ Yes | ✅ Yes |
| **Early Detection** | ✅ Fast | ✅ Fast | ✅ Very Fast |
| **Confidence** | ⚠️ Medium | ✅ High | ✅ Very High |
| **Explainability** | ⚠️ Limited | ✅ Good | ✅ Good |

---

## Model Files

**Location**: `Data/Models/`

1. **isolation_forest_model.pkl** (Primary Model)
   - IsolationForest trained on historical user activity data
   - Detects deviation from normal behavior patterns

2. **random_forest_model.pkl** (Validation Model)
   - RandomForest trained on labeled threat/normal data
   - Validates IsolationForest predictions

---

## Usage

### **Training Models**
```bash
python src/mode_training.py
```
Or run the test script:
```bash
python test_hybrid_model.py
```

### **Detecting Anomalies**
```python
from src.anomaly_detection import detect_anomalies

# Feature dataframe with numeric columns
results = detect_anomalies(features_df)

# Results include:
# - anomaly: Binary threat prediction
# - anomaly_score: Hybrid threat score (0-1)
# - iso_score: IsolationForest score
# - rf_score: RandomForest probability
# - confidence: Model confidence
```

### **Computing Risk Scores**
```python
from src.risking_scoring import compute_risk

risk_df = compute_risk(results)
# Returns dataframe sorted by risk score (highest first)
```

### **Evaluating Model Performance**
```bash
python src/model_evaluation.py
```

---

## Performance Metrics

From test run on 30 samples:

**IsolationForest**:
- Anomalies Detected: 3
- Average Score: 0.618

**RandomForest**:
- Average Anomaly Probability: 0.304

**Hybrid Model**:
- Anomalies Detected: 9
- Average Score: 0.523

*The hybrid model detected more potential threats by combining both methods, providing better coverage while maintaining validation through RandomForest.*

---

## Tuning Parameters

To adjust threat sensitivity, modify these parameters:

### **IsolationForest**
```python
contamination=0.1  # Increase to 0.15-0.2 for more sensitivity
n_estimators=100   # Increase for better accuracy (slower)
```

### **RandomForest**
```python
n_estimators=100   # More trees = better accuracy but slower
max_depth=15       # Shallower trees = more general decisions
```

### **Hybrid Weights**
```python
hybrid_scores = (iso_scores * 0.7) + (rf_proba * 0.3)
# Increase IsoForest weight for unsupervised detection
# Increase RandomForest weight for supervised confidence
```

### **Decision Threshold**
```python
hybrid_anomalies = [1 if score > 0.5 else 0]
# Lower threshold (0.4) = more sensitive (more false positives)
# Higher threshold (0.6) = less sensitive (more false negatives)
```

---

## Future Improvements

1. **Ensemble Methods**: Add XGBoost or LightGBM for better performance
2. **Feature Engineering**: Extract behavioral patterns (time-based, sequential)
3. **Online Learning**: Update models as new threats emerge
4. **Explainability**: Add SHAP values for interpretation
5. **Multi-class Detection**: Distinguish between threat types

---

## References

- IsolationForest: [Scikit-learn Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html)
- RandomForest: [Scikit-learn Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- Anomaly Detection: Liu et al. "Isolation Forest"

---

**Status**: ✅ Hybrid model implemented and tested
**Last Updated**: February 16, 2026
**Authors**: Aayush Salve
