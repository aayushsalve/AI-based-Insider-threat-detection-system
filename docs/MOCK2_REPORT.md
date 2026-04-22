# Major Project Mock 2 Report

## Project Title
AI-Based Insider Threat Detection System Using Hybrid Machine Learning

## Student Details
- Name: [Aayush Salve]
- Roll Number: [22CC1007]
- Department: [Computer Science Engineering Cybersecurity]
- Guide: [Dr. Dhananjay Dhakane]
- Institution: [RAIT]
- Date: April 4 2026

---

## 1. Refined Problem Statement and Objectives

### 1.1 Problem Statement
Organizations face significant risk from insider threats, including data theft, credential misuse, and unauthorized access by trusted users. Traditional rule-based security systems often generate high false positives and fail to detect gradual or novel behavioral deviations. There is a need for an intelligent system that can continuously analyze user behavior, detect suspicious patterns early, and prioritize high-risk users for rapid SOC response.

### 1.2 Refined Objectives
1. Build a hybrid insider threat detection framework using both unsupervised and supervised learning.
2. Detect unknown anomalies as well as known malicious behavior patterns.
3. Generate interpretable user risk scores for security analyst triage.
4. Validate model performance with cross-validation and threshold tuning.
5. Deliver a deployment-ready prototype with dashboard/API support and retraining recommendations.

---

## 2. Methodology and Implementation Progress

### 2.1 Methodology Overview
The implemented methodology follows a multi-stage pipeline:
1. Data ingestion and preprocessing from user activity, login behavior, and sensitive access logs.
2. Feature engineering for security-relevant behavioral indicators.
3. Hybrid anomaly detection using Isolation Forest and Random Forest.
4. Weighted hybrid scoring and risk computation.
5. Threat categorization and analyst-facing outputs (reports/dashboard/API).

### 2.2 Progress Achieved So Far
- Data pipeline implemented for loading, cleaning, and transforming activity datasets.
- Hybrid model architecture implemented and tested.
- Risk scoring engine integrated with anomaly outputs.
- Evaluation pipeline completed with 5-fold cross-validation.
- Reporting artifacts generated (performance, recommendations, summaries).
- Dashboard and API endpoints implemented for operational visibility.

Current status: Deployment-ready prototype completed for Mock 2.

---

## 3. Implementation Details: Tools and Technologies

### 3.1 Programming and Frameworks
- Python
- Flask (web dashboard and APIs)
- Pandas, NumPy (data processing)
- Scikit-learn (machine learning)
- Joblib (model persistence)

### 3.2 Models Used
- IsolationForest (primary unsupervised anomaly detector, weighted 70%)
- RandomForestClassifier (supervised validation layer, weighted 30%)

### 3.3 Scoring Logic
Hybrid score:

Hybrid Score = (0.7 x IsolationForest Score) + (0.3 x RandomForest Score)

Risk score composition:

Risk Score = (0.4 x Anomaly Score) + (0.4 x Sensitive Access) + (0.2 x Confidence)

Final risk is represented on a 0 to 10 scale for SOC prioritization.

### 3.4 Supporting Artifacts
- Trained model files
- Threat reports and executive summaries
- Threshold optimization output
- Operational guide for SOC usage

---

## 4. Innovation and Novelty Achieved So Far

1. Hybrid detection architecture combining anomaly discovery and supervised validation.
2. Weighted fusion approach that balances sensitivity and confidence.
3. SOC-friendly risk scoring instead of binary-only anomaly labels.
4. Focus on high-value behavioral indicators such as:
   - Sensitive after-hours access
   - Failed login patterns
   - Unusual location behavior
   - Abnormal download activity
5. Deployment-oriented design integrating model outputs with dashboard/API workflows.

---

## 5. Intermediate Results and Validation Approach

### 5.1 Validation Approach
- 5-fold cross-validation used to evaluate generalization stability.
- Class balancing and threshold optimization applied for better threat capture.
- Performance tracked across precision, recall, F1-score, and accuracy.

### 5.2 Intermediate Results
Based on latest generated summary and performance reports:

- Precision: 88.0% +/- 12.2%
- Recall: 78.2% +/- 16.0%
- F1-Score: 82.0% +/- 11.8%
- Accuracy: 92.0% +/- 3.0%

Dataset progression:
- Original: 100 users (10 threats)
- Enhanced: 126 users (36 threats via balancing)

Threshold tuning result:
- Optimal threshold approximately 0.539

### 5.3 Interpretation
- High precision indicates reduced false alarms.
- Strong recall indicates effective threat capture capability.
- F1-score confirms good precision-recall balance for SOC operations.

---

## 6. Outcomes and Impact

### 6.1 Technical Outcomes
- End-to-end insider threat detection prototype completed.
- Hybrid model validated and integrated with risk scoring workflow.
- Analyst-readable outputs generated for decision support.

### 6.2 Operational Impact
- Supports prioritized investigation of high-risk users.
- Improves early identification of suspicious insider behavior.
- Provides a repeatable framework for periodic retraining and monitoring.

### 6.3 Academic and Industry Relevance
- Aligned with practical SOC requirements.
- Suitable as a foundation for advanced research publication and enterprise deployment.

---

## 7. Publication, Patent, and Copyright Status

### 7.1 Paper Publication
- Status: In progress
- Planned contribution: Hybrid insider threat detection framework with validated SOC-focused risk scoring.

### 7.2 Patent
- Status: Not filed yet
- Potential patentable element: Weighted hybrid threat scoring framework combining unsupervised anomaly detection and supervised validation for insider threat analytics.

### 7.3 Copyright
- Status: Eligible for software and documentation copyright registration.
- Scope: Source code, model pipeline implementation, report templates, and operational documentation.

---

## 8. Challenges Faced and Mitigation

1. Limited labeled insider threat data.
   - Mitigation: Data balancing and hybrid architecture combining unsupervised + supervised learning.
2. Trade-off between high detection sensitivity and false positives.
   - Mitigation: Threshold optimization and weighted scoring.
3. Need for operational usability.
   - Mitigation: Dashboard/API outputs and risk-level based categorization.

---

## 9. Future Work Before Final Review

1. Improve explainability using feature-level reason codes or SHAP.
2. Expand dataset with more realistic and adversarial scenarios.
3. Integrate real-time streaming detection.
4. Conduct pilot evaluation with SOC feedback.
5. Complete manuscript submission and IP decision workflow.

---

## 10. Conclusion

The project has successfully progressed to a deployment-ready hybrid insider threat detection prototype. The implemented system combines unsupervised anomaly discovery with supervised validation, delivers SOC-oriented risk scoring, and demonstrates strong intermediate performance. The current outcomes indicate technical feasibility, operational relevance, and clear potential for publication and intellectual property generation in subsequent project phases.

---

## Annexure (Optional for Final Submission)
- Performance table snapshots
- Architecture diagram
- API endpoint summary
- Dashboard screenshots
- Sample threat report excerpts
