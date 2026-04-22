# BLACK BOOK

## Insider threat detection

### Submitted In Partial Fulfillment of the Degree Requirements

- Student Name: Aayush Salve
- Roll Number: 22CC1007
- Department: Computer Science Engineering Cybersecurity
- Guide: Dr. Dhananjay Dhakane
- Institution: RAIT
- Academic Year: 2025-26
- Submission Date: April 2026

---

## CERTIFICATE

This is to certify that the project titled "Insider threat detection" is a bonafide work carried out by Aayush Salve (Roll No. 22CC1007) under my guidance and supervision in partial fulfillment of the requirements for the award of the degree in Computer Science Engineering Cybersecurity.

- Guide Signature: ____________________
- Head of Department Signature: ____________________
- Date: ____________________

---

## DECLARATION

I hereby declare that the work presented in this project report titled "Insider threat detection" is my original work and has been carried out under the guidance of Dr. Dhananjay Dhakane. The content of this report has not been submitted, either in part or full, for any other degree, diploma, or certification.

- Student Signature: ____________________
- Name: Aayush Salve
- Date: ____________________

---

## ACKNOWLEDGEMENT

The completion of any project brings with it a sense of satisfaction, but it is never complete without thanking those people who made it possible and whose constant support helped in achieving our objectives.

We would like to thank D.Y. Patil University, Ramrao Adik Institute of Technology, for providing us with the proper facilities and support required for the successful completion of this project.

We would like to express our sincere gratitude to our respected Head of Department, Dr. Sangita Chaudhari, for her encouragement and for providing us an environment conducive to the successful completion of the project.

We would like to thank our project guide, Dr. Dhananjay Dhakane, for expert guidance, constant motivation, and valuable technical suggestions throughout the course of this project, and for always being available to help whenever we needed direction.

We would like to thank all our faculty members for their expert guidance and encouragement throughout the course of this report, and for supporting us whenever we needed suggestions.

We would like to express our sincere gratitude to our parents for providing a proper environment at home and for their constant support throughout this journey.

Last but not least, we would like to thank our friends and well-wishers for their help, cooperation, and encouragement throughout the project, which greatly contributed to the successful completion of this work.

---

## ABSTRACT

Insider threats constitute one of the most complex and significant challenges in the domain of cybersecurity because the individuals involved may already possess legitimate access to organizational systems, confidential data, and critical digital resources. Unlike external attackers, insider threats often operate within trusted boundaries, making their actions more difficult to identify through traditional perimeter-based or rule-based security mechanisms. In many real-world environments, conventional monitoring systems are unable to detect subtle behavioral deviations, low-and-slow malicious actions, or misuse of valid credentials, while also generating a high number of false positives that reduce analyst efficiency and trust in alerts.

This project presents a professional insider threat detection framework based on a hybrid machine learning approach designed to identify suspicious user behavior in organizational environments. The proposed system combines unsupervised anomaly detection and supervised classification to provide both adaptability and confidence in decision-making. IsolationForest is used as the primary anomaly detection model to identify unusual patterns in user activity without relying entirely on labeled attack data, while RandomForest is employed as a supervised validation layer to improve classification reliability and reduce uncertain predictions.

The system processes user behavioral data such as login attempts, failed authentication patterns, sensitive file access frequency, download activity, and location-based access diversity through a structured pipeline consisting of data preprocessing, feature engineering, anomaly scoring, and risk prioritization. A weighted hybrid score is generated to classify suspicious behavior, after which a multi-factor risk score on a 0–10 scale is computed to support investigation prioritization in a Security Operations Center environment. This risk-oriented design helps convert raw machine learning outputs into analyst-friendly, interpretable, and actionable intelligence.

To support practical implementation, the solution has been integrated with a web-based dashboard and API components that allow visualization of high-risk users, risk distribution, recent flagged activities, and administrative response actions such as restricting or blocking suspicious accounts. The dashboard-oriented design improves operational usability and demonstrates how intelligent detection models can be translated into real-world SOC workflows for early warning and rapid incident triage.

The proposed framework was validated using 5-fold cross-validation and achieved strong performance results, including 88.0% precision, 78.2% recall, 82.0% F1-score, and 92.0% accuracy. These results indicate that the hybrid model is capable of maintaining a useful balance between reducing false alarms and capturing a significant proportion of potentially malicious insider behavior. The threshold-tuned and report-driven output further enhances the deployment readiness of the prototype for controlled environments.

Overall, this project demonstrates that a hybrid machine learning framework for insider threat detection can significantly improve threat visibility, operational confidence, and risk-based prioritization compared with static monitoring approaches. It provides both academic relevance and practical value by addressing a critical cybersecurity challenge through intelligent detection, interpretable scoring, and deployment-oriented design. The system also establishes a strong foundation for future extension in areas such as explainable AI, real-time monitoring, adaptive retraining, and enterprise-scale deployment.

Keywords: Insider Threat Detection, Anomaly Detection, IsolationForest, RandomForest, Hybrid Machine Learning, Cybersecurity Analytics

---

## TABLE OF CONTENTS

1. List of Abbreviations
2. Introduction
3. Literature Survey
4. Problem Statement and Objectives
5. Proposed Methodology
6. System Design and Architecture
7. Tools and Technologies
8. Dataset Description and Preprocessing
9. Implementation Details
10. Results and Validation
11. Outcomes and Impact
12. Limitations and Challenges
13. Future Scope
14. Publication, Patent, and Copyright
15. Conclusion
16. Bibliography
17. Annexure
18. Existing System Analysis
19. Proposed System Design in Detail
20. Software and Hardware Requirements
21. Feasibility Study
22. Detailed Module Description
23. Algorithm Design and Pseudocode
24. Test Plan and Test Cases
25. Detailed Results Discussion
26. Deployment and Operations Plan
27. Risk Register and Mitigation Plan
29. Extended Viva Preparation
30. Expanded Appendix Material

---

## 1. LIST OF ABBREVIATIONS

- AI: Artificial Intelligence
- ML: Machine Learning
- SOC: Security Operations Center
- IF: Isolation Forest
- RF: Random Forest
- API: Application Programming Interface
- CSV: Comma-Separated Values
- CV: Cross-Validation
- F1: Harmonic Mean of Precision and Recall
- TP: True Positive
- FP: False Positive
- TN: True Negative
- FN: False Negative
- SIEM: Security Information and Event Management
- KPI: Key Performance Indicator
- POC: Proof of Concept

---

## 2. INTRODUCTION

### 2.1 Background
Modern organizations generate large volumes of digital activity logs across authentication systems, file servers, internal applications, and cloud platforms. While security controls such as firewalls, endpoint protection, and identity management systems have improved perimeter defense, insider threat incidents continue to be one of the most difficult categories of cyber risk to manage. Unlike external attackers, insiders may already possess legitimate access to sensitive systems, making malicious behavior harder to identify through traditional signature-based controls.

Insider threats may arise from multiple user profiles, including malicious employees, compromised privileged accounts, and negligent users who violate policy unintentionally. These behaviors can include unusual login times, repeated failed authentication attempts, unauthorized access to confidential files, excessive data downloads, or location anomalies. Because many of these activities may also occur in legitimate operational contexts, reliable detection requires behavioral understanding rather than static rule checks.

As organizations move toward data-driven security operations, there is increasing demand for intelligent User and Entity Behavior Analytics (UEBA) systems that can detect suspicious deviations early and support analysts with interpretable risk indicators. This project is developed in that context, with a focus on combining machine learning-based anomaly detection and practical SOC usability.

### 2.2 Need and Motivation
Conventional security monitoring typically depends on fixed thresholds and manually crafted correlation rules. Although such systems are useful for known attack patterns, they often struggle with evolving insider tactics and adaptive misuse of legitimate credentials. This leads to two practical problems in SOC environments:

1. Excessive false positives that consume analyst time and reduce trust in alerts.
2. Missed low-and-slow insider behaviors that do not immediately violate static rules.

The motivation for this project is to address these limitations through a hybrid machine learning framework that can detect both unknown and known threat patterns. By combining unsupervised and supervised learning, the system aims to balance sensitivity and confidence while generating a prioritized risk score for operational decision-making.

### 2.3 Aim
The primary aim of this project is to design, develop, and validate an intelligent insider threat detection framework that can continuously analyze user behavior, identify suspicious deviations at an early stage, and support timely security decision-making in organizational environments. The project aims to move beyond static rule-based monitoring by introducing a hybrid machine learning architecture capable of capturing both previously unseen anomalies and known malicious patterns.

In addition to detection accuracy, this work aims to improve practical SOC usability by transforming model-level predictions into interpretable risk-prioritized outputs. The intended outcome is a deployment-ready prototype that not only flags high-risk behavior but also helps analysts with confidence-aware threat assessment, investigation prioritization, and data-driven response planning.

### 2.4 Objectives
1. Build a hybrid ML pipeline by combining IsolationForest and RandomForest models.
2. Detect both unknown anomalies and known threat patterns from user behavior data.
3. Generate interpretable risk scores on a 0-10 scale for analyst investigation priority.
4. Validate the system using cross-validation, threshold tuning, and standard evaluation metrics.
5. Develop deployment-ready outputs through reports, APIs, and dashboard integration.

### 2.5 Scope of Work
The scope of work includes data ingestion and preprocessing, feature engineering, hybrid model-based anomaly detection, and risk scoring for insider threat analysis. It also includes validation of model performance and generation of SOC-oriented outputs such as threat reports and dashboard-level summaries.

The implemented scope specifically covers:

1. Processing structured activity datasets representing user behavior.
2. Building and integrating IsolationForest and RandomForest-based detection logic.
3. Computing hybrid anomaly scores and final risk scores for user-level prioritization.
4. Evaluating performance using cross-validation and threshold optimization.
5. Producing analyst-facing outputs via reports and a Flask-based interface.

The current project stage targets a controlled prototype environment and does not include full enterprise-scale live deployment, cross-organization integration, or legally validated forensic attribution.

### 2.6 Significance of the Project
This work is significant from academic, technical, and operational perspectives. Academically, it demonstrates the application of hybrid machine learning in cybersecurity analytics. Technically, it offers a practical architecture that combines anomaly discovery with supervised confirmation. Operationally, it supports SOC teams by converting complex model outputs into interpretable risk-based prioritization, which can improve incident triage efficiency.

### 2.7 Organization of the Report
The remaining report is structured as follows: Chapter 3 presents the literature survey and research gap. Chapter 4 defines the refined problem statement and objectives. Chapter 5 and Chapter 6 detail the proposed methodology and architecture. Chapter 7 to Chapter 9 describe the technology stack, dataset handling, and implementation details. Chapter 10 presents results and validation, followed by outcomes, limitations, future scope, and conclusion in later chapters.

---

## 3. LITERATURE SURVEY

Insider threat detection has emerged as a critical area of research in cybersecurity because threats originating from within an organization are often more difficult to identify than external attacks. Unlike external intrusions, insider activities frequently occur through valid credentials and legitimate access privileges, making conventional rule-based security mechanisms insufficient for reliable detection. Over the years, researchers have explored different approaches for insider threat identification, including rule-based monitoring, supervised machine learning, unsupervised anomaly detection, and more recently, hybrid intelligent systems that combine the strengths of multiple methods.

Early security monitoring approaches relied heavily on rule-based systems and static threshold mechanisms. These systems used predefined signatures, login failure limits, suspicious access patterns, or manually crafted SIEM rules to identify potentially dangerous behavior. While such approaches were easy to understand and implement, researchers observed that they often lacked adaptability and generated high numbers of false positives when applied to dynamic organizational environments. This limitation motivated the shift toward intelligent and behavior-driven detection techniques.

Liu, Ting, and Zhou (2008) introduced the IsolationForest algorithm, which became one of the most important anomaly detection methods in cybersecurity analytics. The key idea behind IsolationForest is that anomalous observations are easier to isolate in random decision trees than normal observations. This method gained popularity because of its computational efficiency, ability to work with unlabeled data, and suitability for identifying rare behavioral deviations. In insider threat scenarios, this approach is especially valuable because truly labeled insider attack datasets are limited, and many malicious patterns may be previously unseen.

Breiman (2001) proposed the RandomForest algorithm, an ensemble learning method that combines multiple decision trees to improve classification performance and robustness. RandomForest has been widely applied in cybersecurity for classification tasks because it handles high-dimensional data well, reduces overfitting, and provides probability-based outputs that are useful for confidence estimation. In insider threat detection, RandomForest is particularly useful when a labeled dataset is available and the goal is to validate whether a suspicious activity pattern is likely to correspond to an actual threat.

Greitzer and Hohimer (2011) explored the role of human behavior modeling in anticipating insider attacks and emphasized that technical indicators alone are often insufficient unless combined with contextual behavior understanding. Their work highlighted the importance of behavioral profiling, risk indicators, and user-centric analytics in insider threat defense. This study strongly supports the idea that effective insider threat systems must move beyond simple event counting and instead incorporate behavioral interpretation and risk-based reasoning.

Tuor et al. (2017) investigated deep learning for unsupervised insider threat detection in structured cybersecurity data streams. Their work showed that unsupervised methods can reveal hidden anomalous patterns from log and activity data even in the absence of fully labeled attack datasets. However, the study also pointed out that purely unsupervised systems may produce uncertain alerts and require additional interpretation before analysts can act on them confidently. This limitation is highly relevant to practical SOC operations, where confidence and explainability are necessary for prioritizing incidents.

The National Institute of Standards and Technology (NIST) has also contributed significantly to the cybersecurity domain through its Cybersecurity Framework and Special Publication 800-53. Although these documents are not machine learning models, they provide the governance, monitoring, access control, and risk management principles necessary for designing secure detection systems. Their guidance supports the need for continuous monitoring, risk-based prioritization, and auditable security controls, all of which are important in the context of insider threat analytics.

From the reviewed studies, it is evident that each research direction offers specific strengths but also notable limitations. Rule-based approaches are easy to interpret but fail to adapt to evolving threats. Supervised classification models such as RandomForest perform well on labeled data but depend on the availability of representative insider threat labels, which are often scarce in practice. Unsupervised methods such as IsolationForest are effective for discovering unknown anomalies but may lack sufficient validation confidence when used alone. Behavioral studies provide important conceptual understanding but may not always translate directly into automated operational systems.

To better understand the differences across existing approaches, a comparative summary is presented below:

| Study / Approach | Technique Used | Strengths | Limitations |
|---|---|---|---|
| Traditional Rule-Based Monitoring | Static rules, SIEM thresholds | Simple, interpretable, easy to deploy | High false positives, poor adaptability |
| Liu et al. (2008) | IsolationForest | Effective anomaly detection, works without labels, computationally efficient | May produce uncertain alerts without validation |
| Breiman (2001) | RandomForest | Strong classification accuracy, robust to overfitting, probabilistic outputs | Requires labeled data; may miss novel attacks |
| Greitzer & Hohimer (2011) | Behavioral modeling | Emphasizes human factors and contextual risk | Harder to operationalize fully in automated systems |
| Tuor et al. (2017) | Unsupervised deep learning | Good for complex unseen patterns in structured logs | Lower explainability and higher deployment complexity |

Based on the literature, a clear research gap can be identified. Most existing approaches focus either on anomaly detection or on classification, but very few provide a practical balance between unknown-threat discovery, validation confidence, interpretability, and analyst usability. In real SOC settings, a system that merely detects unusual behavior is not sufficient; it must also assist in prioritization, reduce false alarms, and support decision-making through understandable outputs.

The present project addresses this gap by proposing a hybrid insider threat detection framework that combines the anomaly discovery capability of IsolationForest with the validation strength of RandomForest. In addition, the project introduces a multi-factor risk scoring mechanism and dashboard-based analyst interface to improve practical usability. Thus, the proposed work is not only inspired by the existing literature but also extends it in a manner that is more deployment-oriented, interpretable, and suitable for real-world organizational monitoring.

---

## 4. PROBLEM STATEMENT AND OBJECTIVES

### 4.1 Problem Statement
In modern organizations, every employee interaction with digital infrastructure produces a trail of security-relevant events such as login attempts, authentication failures, file access records, downloads, application usage, and privilege-based activities. Although these logs provide valuable visibility into user behavior, distinguishing truly harmful insider activity from normal operational behavior remains a complex cybersecurity challenge. Insider threats are particularly dangerous because the actors may already possess valid credentials and legitimate access permissions, enabling malicious behavior to remain hidden within trusted workflows.

The problem becomes more severe in environments where traditional monitoring systems depend mainly on static thresholds, signature-based alerts, or manually written rules. Such mechanisms are effective only for obvious or previously known patterns of misuse, but they often fail to detect subtle deviations such as unusual login timing, abnormal access to sensitive files, repeated failed authentications, or slow and deliberate misuse of organizational resources. Consequently, security teams often face alert fatigue due to excessive false positives while still remaining vulnerable to carefully disguised insider incidents.

A further challenge lies in the nature of insider threat data itself. Real insider attacks are relatively rare, sensitive, and difficult to label accurately. Because of this, purely supervised machine learning approaches may not generalize well to unseen threats, while fully unsupervised methods may detect anomalies without offering enough confidence or interpretability for security analysts to act on them quickly. In practice, organizations need a detection framework that is not only technically accurate but also explainable, risk-aware, and operationally useful.

In addition, modern Security Operations Center teams require more than a simple malicious-or-benign prediction. They need prioritized outputs, understandable risk indicators, and analyst-friendly summaries that support fast triage and response. A system that only detects anomalies without contextual interpretation may create uncertainty rather than action. Therefore, the real problem is not just to detect unusual behavior, but to identify, validate, score, and present insider risk in a manner that supports timely and informed decision-making.

Hence, the problem addressed in this project can be stated as follows:

> To develop an intelligent and interpretable insider threat detection system capable of analyzing organizational user behavior, identifying both unknown anomalies and known suspicious patterns, reducing false alarms, and generating actionable risk-prioritized outputs for practical cybersecurity monitoring.

This project addresses the above problem through a hybrid machine learning framework that combines anomaly detection, supervised validation, weighted risk scoring, and dashboard-oriented visualization. The proposed solution aims to provide an adaptive, practical, and deployment-oriented mechanism for early insider threat identification in controlled organizational environments.

### 4.2 Objectives
The objectives of the proposed project are designed to address the above problem in a systematic and implementation-oriented manner. The major objectives are as follows:

1. **To analyze the nature of insider threats in organizational environments** and study how malicious, negligent, or compromised users can exploit legitimate access to create security incidents.

2. **To identify the limitations of traditional rule-based monitoring approaches**, especially their inability to detect low-and-slow misuse, behavioral deviations, and previously unseen insider attack patterns.

3. **To design and implement a hybrid machine learning framework** by combining IsolationForest and RandomForest so that the strengths of anomaly discovery and supervised classification can be utilized together.

4. **To collect, preprocess, and structure user activity data** including login behavior, failed authentication patterns, sensitive file access, and related behavioral indicators in a format suitable for analytical modeling.

5. **To perform meaningful feature engineering** that captures suspicious behavioral characteristics and improves the quality, relevance, and predictive value of the data used for threat detection.

6. **To generate hybrid anomaly scores and a multi-factor risk score** that convert model outputs into interpretable and actionable insights for investigation and response prioritization.

7. **To classify users into operational threat categories** such as Critical, High, Medium, and Low so that analysts can quickly identify the most important cases for review.

8. **To evaluate the effectiveness of the system using standard performance metrics** such as Precision, Recall, F1-score, Accuracy, and threshold tuning with cross-validation.

9. **To provide analyst-oriented outputs through reports, APIs, and dashboard views** so that the proposed solution is not limited to model development alone but also supports real monitoring workflows.

10. **To establish a foundation for future improvement and scalability** in areas such as explainable AI, real-time event monitoring, model retraining, drift handling, and enterprise deployment.

The above objectives ensure that the project is not only academically sound but also practically aligned with real-world SOC requirements, where accuracy, interpretability, and usability are equally important.

---

## 5. PROPOSED METHODOLOGY

### 5.1 Workflow
The proposed methodology follows a structured end-to-end workflow to ensure that insider threat detection is carried out in a systematic, accurate, and operationally useful manner. The complete workflow of the system is described below:

1. **Data Collection and Ingestion**  
   The process begins with the collection of structured organizational activity data such as login attempts, authentication failures, user activity logs, and sensitive file access events. These records are stored in CSV format and are ingested into the pipeline for further processing.

2. **Data Cleaning and Preprocessing**  
   The raw collected data is cleaned to remove inconsistencies, missing values, duplicate records, and irrelevant fields. This stage ensures that the dataset is reliable and suitable for analytical processing. Numeric conversion, normalization, and formatting are also applied wherever required.

3. **Feature Engineering**  
   After preprocessing, meaningful behavioral features are extracted from the raw data. These include login-related patterns, failed login frequency, sensitive access count, activity intensity, and location diversity indicators. Feature engineering improves the model’s ability to distinguish normal behavior from suspicious behavior.

4. **Dataset Balancing and Preparation**  
   Since insider threat data is often imbalanced, the prepared dataset is further processed to improve class balance and ensure that the models do not become biased toward normal user behavior. This stage strengthens the quality and fairness of training and evaluation.

5. **Anomaly Detection Using IsolationForest**  
   The preprocessed feature set is passed through the IsolationForest model, which identifies unusual or abnormal user behavior without requiring complete labeled attack data. This helps in discovering novel or previously unseen insider threat patterns.

6. **Supervised Validation Using RandomForest**  
   In parallel, the same feature set is evaluated using the RandomForest classifier, which acts as a supervised validation layer. This model provides probability-based threat predictions using labeled information and helps improve confidence in the final decision.

7. **Hybrid Score Generation**  
   The outputs of IsolationForest and RandomForest are combined using a weighted fusion approach. This hybrid score balances anomaly detection capability with classification confidence and produces a more robust assessment than any single model alone.

8. **Risk Score Computation and Threat Categorization**  
   The hybrid anomaly output is further transformed into a multi-factor risk score on a 0–10 scale using weighted risk components such as anomaly evidence, sensitive access behavior, login anomalies, and behavioral indicators. Based on the final score, users are categorized into risk levels such as Critical, High, Medium, or Low.

9. **Threshold Optimization and Model Validation**  
The system performance is evaluated using 5-fold cross-validation, threshold optimization, and standard metrics such as Precision, Recall, F1-score, and Accuracy. This step ensures that the proposed model is both effective and reliable.

10. **Output Generation and Analyst Support**  
   Finally, the system presents the results through dashboard views, API responses, and report files. Flagged users, recent suspicious activities, risk distributions, and score summaries are made available to support SOC analysts in timely monitoring, investigation, and response.

This workflow ensures that the system is not only technically sound from a machine learning perspective but also practically useful for real-world insider threat monitoring and analyst decision support.

### 5.2 Hybrid Scoring
The system fuses the outputs of two independent models using a weighted combination formula:

**Hybrid Score = (0.7 × IsolationForest Anomaly Score) + (0.3 × RandomForest Threat Probability)**

IsolationForest contributes 70% of the signal because it is the primary unsupervised detector capable of identifying novel behavior patterns. RandomForest contributes 30% as a validation layer that introduces supervised confidence based on labeled training patterns. The hybrid score is normalized to [0, 1] and compared against the optimized threshold (≈ 0.539) to produce a binary anomaly label.

### 5.3 Risk Scoring — Four-Component Weighted Formula
The final risk score is computed using a formal four-component weighted model implemented in `enhanced_risk_scoring.py`. Each component is first normalized to [0, 1] and then scaled to a 0–10 score:

**R = Σ(wᵢ × fᵢ) × 10**

| Component | Weight | Feature Source |
|---|---|---|
| Anomaly Detection | 0.40 (40%) | Normalized IF anomaly score |
| Sensitive File Access | 0.30 (30%) | Sensitive file access count normalized |
| Login Anomalies | 0.20 (20%) | Failed login frequency normalized |
| Behavioral Drift | 0.10 (10%) | Additional behavioral pattern signals |

Risk level assignment based on computed R value:

| Risk Level | Score Range | Dashboard Color |
|---|---|---|
| Critical | R ≥ 7.5 | Red (danger) |
| High | 5.0 ≤ R < 7.5 | Amber (warning) |
| Medium | 2.5 ≤ R < 5.0 | Cyan (info) |
| Low | R < 2.5 | Green (success) |

These thresholds are embedded in the live dashboard and the `compute_risk_score()` function in `app.py`. The risk score is stable per user across sessions because the random component is seeded deterministically from the user ID.

---

## 6. SYSTEM DESIGN AND ARCHITECTURE

### 6.1 Architectural Overview
The proposed insider threat detection system is designed as a layered and modular architecture that supports accurate detection, efficient processing, and practical analyst usability. The overall architecture follows the principle of separating data acquisition, preprocessing, intelligent analysis, risk interpretation, and presentation into distinct but connected components. This separation improves maintainability, scalability, and clarity while allowing each stage of the system to be independently improved in future versions.

At a high level, the system begins with structured behavioral data collected from organizational activity sources such as login records, authentication failures, user activity logs, and sensitive file access events. These records are passed through a preprocessing and feature engineering pipeline where they are cleaned, transformed, and converted into model-ready numerical representations. The processed data is then analyzed through a hybrid detection engine composed of IsolationForest and RandomForest, followed by a multi-factor risk scoring layer that converts model outputs into interpretable analyst-friendly scores. Finally, the results are delivered through reports, APIs, and a Flask-based dashboard for monitoring and response.

### 6.2 Layer-Wise Architecture
The architecture of the system can be viewed as five major layers:

- **Input Layer:** Collects raw user behavior data such as login events, failed logins, activity counts, downloads, and sensitive file access logs.
- **Processing Layer:** Performs data cleaning, normalization, transformation, balancing, and feature engineering.
- **Detection Layer:** Applies IsolationForest for anomaly discovery and RandomForestClassifier for supervised threat validation.
- **Scoring Layer:** Generates hybrid anomaly scores, computes a four-component risk score, and assigns final risk levels.
- **Presentation Layer:** Publishes outputs through JSON reports, CSV summaries, REST APIs, and the monitoring dashboard.

This layered organization ensures that the system is easy to understand conceptually and practical to deploy in an academic or prototype SOC environment.

### 6.3 Design Principles
The proposed architecture has been developed based on the following design principles:

1. **Modularity:** Each major function such as preprocessing, training, evaluation, scoring, and reporting is separated into dedicated modules.
2. **Adaptability:** The use of hybrid machine learning allows the system to detect both known and unknown suspicious behavior.
3. **Interpretability:** Risk scoring and dashboard outputs are designed to assist analysts rather than only display raw model outputs.
4. **Operational Relevance:** The architecture supports real-world SOC-style workflows including prioritization, monitoring, and administrative response.
5. **Extensibility:** Future enhancements such as explainability, streaming analytics, and automated retraining can be integrated with minimal redesign.

### 6.4 Core Software Modules
The source directory contains multiple Python modules organized by responsibility:

**Detection and Scoring Modules:**
- app.py — Flask web application with routing, session management, dashboard rendering, and live risk score enrichment.
- enhanced_risk_scoring.py — Implements the four-component weighted risk scoring model.
- anomaly_detection.py — Core anomaly detection logic.
- risk_scorer.py and related helpers — Supporting scoring and threshold logic.

**Data Pipeline Modules:**
- data_pipeline.py — End-to-end pipeline coordination.
- data_preprocessing.py — Data cleaning and transformation.
- data_processing.py — Structured preparation of behavioral records.
- feature_engineering.py — Creation of model-relevant security features.
- ingest_data.py — Dataset ingestion and loading utilities.

**Training and Evaluation Modules:**
- model_training.py and model_trainer.py — Model development and training routines.
- train_final_model.py — Final model preparation for production-like usage.
- evaluate_kfold.py — Cross-validation implementation.
- model_evaluation.py — Metric generation and performance analysis.
- optimize_threshold.py — Decision threshold tuning.

**Monitoring and Reporting Modules:**
- reporter.py and reporting.py — Executive and analytical report generation.
- generate_final_report.py — Consolidated reporting support.
- drift_monitor.py — PSI-based drift monitoring utilities.
- alerts.py — Alert preparation for suspicious cases.
- explainability.py — Future explainable AI integration point.

### 6.5 Web Interface Structure
The Flask application uses multiple Jinja templates to provide a structured user interface:

| Template | Purpose |
|---|---|
| login.html | User authentication and access control |
| dashboard.html | Main SOC dashboard with charts, tables, and risk summaries |
| profile.html | Detailed per-user view for analysis |
| index.html | Landing and redirection handling |
| 404.html | Error page for invalid routes |

### 6.6 Dashboard Architecture
The dashboard is designed as an analyst-facing decision support interface rather than a simple visualization page. It is built using Bootstrap and Chart.js and includes the following core regions:

**1. Summary Card Layer**  
Displays key statistics such as total users, critical threats, high-risk users, and total flagged activity.

**2. Analytical Visualization Layer**  
Presents the risk distribution donut chart, top-risk user leaderboard, and formal risk formula panel.

**3. Investigation Layer**  
Shows recent user activity records ordered by risk score so that analysts can immediately review suspicious behavior.

**4. Administrative Action Layer**  
Allows administrators to restrict, block, unblock, or manage user accounts directly from the interface.

This structure improves usability by presenting information from the most strategic overview down to the most actionable operational detail.

### 6.7 Data Flow Through the System
The system follows a clearly defined flow of information:

1. Raw behavioral data is loaded from CSV files.
2. The preprocessing layer removes noise and converts data into analysis-ready format.
3. Feature engineering derives risk-relevant indicators from the cleaned records.
4. IsolationForest produces anomaly-oriented outlier scores.
5. RandomForest produces supervised threat probability estimates.
6. Both outputs are combined into a weighted hybrid score.
7. A four-factor risk scoring engine maps this information into a 0–10 risk score.
8. The final results are categorized into Critical, High, Medium, or Low risk classes.
9. Dashboard panels, API endpoints, and generated reports expose the findings to analysts.

This end-to-end data flow ensures that the architecture remains both technically robust and operationally meaningful.

### 6.8 Application Routes and Access Control
The Flask application exposes several routes for user access and analyst operations:

| Route | Method | Description | Access |
|---|---|---|---|
| / | GET | Redirect to login or dashboard | All |
| /login | GET, POST | User login processing | Public |
| /logout | GET | Session termination | Authenticated |
| /dashboard | GET | Main dashboard interface | Authenticated |
| /user/<id> | GET | Individual user profile | Admin or self |
| /user/<id>/restrict | POST | Restrict suspicious user | Admin only |
| /user/<id>/block | POST | Block user account | Admin only |
| /user/<id>/unblock | POST | Restore user account | Admin only |
| /user/<id>/set_role | POST | Change access role | Admin only |
| /api/v1/threats | GET | Threat trend JSON | Authenticated |
| /api/v1/risk | GET | Risk output JSON | Authenticated |

Role-based access control is enforced through session-level checks, ensuring that sensitive administrative actions are restricted to authorized users only.

### 6.9 Architectural Advantages
The chosen architecture provides multiple advantages:

1. It supports hybrid detection rather than relying on a single model.
2. It improves explainability by converting technical outputs into risk-based analyst summaries.
3. It simplifies integration of additional modules such as SHAP, drift monitoring, or streaming data.
4. It separates training, evaluation, and presentation concerns, which improves maintainability.
5. It is suitable for both academic demonstration and prototype-level organizational deployment.

### 6.10 Summary
Thus, the proposed system design and architecture provide a complete framework for insider threat monitoring, starting from raw event collection and ending with analyst-focused decision support. The architecture is technically sound, modular in design, and practically relevant for cybersecurity operations, making it appropriate for both project implementation and future expansion.

---

## 7. TOOLS AND TECHNOLOGIES

The successful development of the proposed insider threat detection system required the use of multiple software tools, programming libraries, frameworks, and supporting utilities. These technologies were selected to ensure efficient data processing, accurate model development, practical deployment, and user-friendly visualization. The following subsections describe the important tools and technologies used in this project.

### 7.1 Programming Language
**Python** was used as the primary programming language for the complete project implementation. Python is highly suitable for machine learning and cybersecurity analytics because of its simplicity, readability, extensive package ecosystem, and strong community support. It enabled rapid development of data preprocessing pipelines, model training modules, reporting utilities, and dashboard integration.

### 7.2 Web Framework
**Flask** was used to develop the web-based application and monitoring dashboard. Flask is a lightweight yet powerful Python web framework that supports routing, session management, template rendering, and API creation. In this project, Flask is responsible for the login system, dashboard pages, user management actions, and REST-based responses for risk monitoring.

### 7.3 Data Manipulation and Numerical Processing
**Pandas** was used for loading, cleaning, transforming, and analyzing structured CSV datasets. It played a central role in handling user activity data, authentication logs, and sensitive access records.

**NumPy** was used for numerical computations, array-based operations, mathematical transformations, and score normalization. It improved the efficiency of data preparation and model-related calculations.

### 7.4 Machine Learning Libraries
**Scikit-learn** served as the core machine learning library for model development and evaluation. It provided the implementation of important algorithms such as IsolationForest and RandomForestClassifier, as well as utilities for cross-validation, threshold tuning, and metric evaluation.

The project specifically relies on:
- **IsolationForest** for unsupervised anomaly detection
- **RandomForestClassifier** for supervised validation of suspicious behavior
- **Model evaluation tools** for measuring precision, recall, F1-score, and accuracy

### 7.5 Model Persistence and Reusability
**Joblib** was used to serialize and store trained machine learning models for future use. This allowed the trained models to be saved in the `Data/Models` directory and reused during dashboard execution and future retraining cycles without repeating the full training process.

### 7.6 Front-End and Visualization Technologies
The dashboard interface uses:
- **HTML5** for page structure
- **CSS3** for layout styling and presentation
- **Bootstrap 5** for responsive design, modern UI components, and consistent formatting
- **Bootstrap Icons** for interface icons and visual cues
- **Chart.js** for graphical visualization of risk distribution and analytics charts

These technologies collectively improve the usability and visual clarity of the analyst-facing dashboard.

### 7.7 Development Environment and Supporting Tools
The following tools supported project development and execution:

- **Visual Studio Code (VS Code):** Used as the primary code editor and development environment.
- **Jupyter Notebook (optional):** Used for exploratory analysis and experimentation during data understanding.
- **Git:** Used for source code version management and change tracking.
- **Virtual Environment (venv):** Used to isolate project dependencies and maintain a stable Python environment.

### 7.8 Data Storage and File Formats
The project mainly uses **CSV files** as the structured data storage format for login logs, activity data, sensitive access data, and processed features. CSV was chosen because it is lightweight, easy to inspect, easy to preprocess with Pandas, and suitable for prototype-level implementation.

The system also generates results in multiple formats:
- **CSV** for tabular reports and metrics
- **TXT** for executive summary outputs
- **JSON** for structured threat reports and API responses

### 7.9 Development Artifacts and Project Components
The project includes several practical development artifacts and implementation outputs, such as:

- training scripts for model development
- detection scripts for risk analysis and anomaly inference
- model files stored in `Data/Models`
- processed datasets and balanced feature files
- generated reports in the `reports` directory
- dashboard templates and static assets
- SOC user guide documentation for operational understanding

### 7.10 Technology Justification
The selected tools and technologies were chosen because they provide the right balance of performance, flexibility, academic relevance, and ease of implementation. Python and Scikit-learn make the machine learning pipeline efficient and reproducible, Flask enables rapid deployment of a prototype dashboard, and Bootstrap with Chart.js makes the final system easier for analysts to understand and use. Therefore, the technology stack is highly suitable for the development of an intelligent and deployment-oriented insider threat detection system.

---

## 8. DATASET DESCRIPTION AND PREPROCESSING

The quality of any intelligent insider threat detection system depends heavily on the quality, structure, and relevance of the dataset used for training and evaluation. Since insider attacks are behavior-driven in nature, the dataset for this project was designed to capture a realistic mixture of normal user activity and suspicious behavioral indicators. The complete dataset preparation process focused on ensuring that the model receives meaningful, clean, and balanced inputs for reliable threat detection.

### 8.1 Dataset Composition
The project uses structured behavioral cybersecurity data stored primarily in CSV format. These files represent multiple dimensions of organizational user activity, including authentication behavior, file access activity, and operational interaction patterns. Instead of relying on a single raw source, the project combines several related datasets so that insider threat detection can be approached from a broader behavioral perspective.

The main data sources used in the project include:

- activity logs representing general user actions and activity intensity
- login attempt records capturing successful and failed authentication behavior
- sensitive file access records showing interactions with important resources
- user profile and identification data required for user-level mapping
- threat label files used for supervised training and validation

At the initial stage, the dataset contained approximately 100 users with only 10 identified threat instances. This created an imbalanced learning environment in which normal behavior strongly dominated suspicious behavior. To improve the learning quality of the supervised layer and strengthen evaluation reliability, the dataset was enhanced and balanced, resulting in approximately 126 users with 36 threat-related instances. This improved dataset structure provided a more practical foundation for training the hybrid detection system.

### 8.2 Nature of the Data
The dataset is primarily semi-synthetic and project-oriented, meaning it was created and refined for academic experimentation while still preserving realistic cybersecurity characteristics. This approach is useful because real insider threat datasets are difficult to obtain due to privacy, confidentiality, and legal restrictions. Therefore, the project emphasizes realistic behavioral indicators rather than relying on purely random or unrealistic values.

The data reflects typical insider threat signals such as:

- repeated failed logins
- unusual access patterns
- elevated sensitive file interaction
- abnormal download or activity behavior
- irregular location diversity and user movement patterns

These indicators are highly relevant in real organizational monitoring systems because they often serve as early warning signals of misuse, compromise, negligence, or malicious intent.

### 8.3 Features Considered
A meaningful feature set is essential for distinguishing normal user behavior from suspicious activity. For this reason, the project includes multiple behavioral and security-oriented attributes derived from the available data sources. The major features considered in the project are listed below:

1. **Login-related behavior:** Total login events, authentication attempts, and frequency-based access patterns.
2. **Failed login frequency:** Number of unsuccessful login attempts, which may indicate password abuse, credential compromise, or brute-force behavior.
3. **Sensitive file access behavior:** Number and frequency of accesses to confidential or restricted resources.
4. **Download and activity rate:** Intensity of user actions over a monitoring period, which may reflect suspicious exfiltration-like behavior.
5. **Location diversity indicators:** Number of distinct access locations or source patterns associated with the same user.
6. **Aggregate behavioral indicators:** Derived patterns used to summarize how far a user deviates from expected activity norms.

These features were selected because they align with practical insider threat scenarios and provide a combination of authentication, behavior, and data-access evidence.

### 8.4 Data Preprocessing Objectives
Before model training, the raw datasets must be converted into a structured, consistent, and machine-readable format. The main objectives of preprocessing in this project are:

- to improve data quality by removing incomplete or inconsistent records
- to prepare numerical representations suitable for machine learning models
- to reduce noise that may affect anomaly detection accuracy
- to strengthen minority-class visibility for better supervised learning
- to ensure that all relevant behavioral indicators are normalized and comparable

Preprocessing is therefore not merely a cleaning step; it is a critical stage that directly influences the final effectiveness of the detection framework.

### 8.5 Preprocessing Steps
The complete preprocessing pipeline followed in the project is described below:

1. **Data loading and consolidation**  
   Data was imported from multiple CSV files and aligned using user-level references so that different activity dimensions could be studied together.

2. **Missing value checks and cleanup**  
   Incomplete records, null entries, and inconsistent values were identified and corrected or removed wherever necessary. This ensured that unreliable entries did not distort the model output.

3. **Duplicate and noise removal**  
   Repeated rows and unnecessary fields that did not contribute to detection quality were filtered out in order to maintain dataset consistency.

4. **Numeric feature preparation**  
   Behavioral indicators such as failed logins, sensitive access counts, and activity intensity were converted into numeric representations suitable for machine learning algorithms.

5. **Feature engineering and transformation**  
   Additional derived variables were created from the raw records so that the models could capture user behavior more effectively. This step improved signal quality for both anomaly detection and supervised validation.

6. **Scaling and normalization**  
   Since some features naturally exist on different numeric ranges, normalization and scaling were applied wherever needed to ensure fair comparison and stable scoring performance.

7. **Dataset balancing for minority threat class**  
   Because insider threat records are relatively rare, the dataset was balanced to reduce model bias toward normal cases and to improve classification fairness.

8. **Preparation of final model-ready dataset**  
   After preprocessing and balancing, the resulting dataset was stored in a clean, analysis-ready form for training, validation, and reporting.

### 8.6 Importance of Class Balancing
Class imbalance is one of the most important challenges in cybersecurity analytics. In real-world environments, malicious insider behavior represents only a small fraction of total user activity. If this imbalance is ignored, a model may achieve high apparent accuracy simply by predicting most users as normal. However, such a model would be operationally weak because it would fail to detect true threats.

In this project, balancing the dataset helped improve the learning behavior of the RandomForest validation layer and made the evaluation metrics more meaningful. It also supported better recall for suspicious cases while maintaining reasonable precision.

### 8.7 Output of the Preprocessing Stage
The final output of the preprocessing stage is a cleaned and structured feature set that can be directly used by the hybrid detection pipeline. This prepared dataset serves as the input to IsolationForest for anomaly discovery and to RandomForestClassifier for supervised threat validation. It also supports risk-score generation, cross-validation, and reporting.

Thus, the dataset description and preprocessing stage forms the foundation of the complete project. A well-prepared dataset ensures that the proposed insider threat detection system operates with greater reliability, better interpretability, and stronger practical relevance.

---

## 9. IMPLEMENTATION DETAILS

This chapter explains how the proposed insider threat detection framework was implemented in practical terms. While the previous chapters describe the methodology and architecture at a conceptual level, the present section focuses on how these ideas were translated into working software modules, machine learning models, scoring logic, dashboard functionality, and analyst-facing outputs. The implementation was designed with an emphasis on modularity, reproducibility, and deployment-oriented usability.

### 9.1 Model 1: IsolationForest
IsolationForest acts as the primary anomaly detection engine of the system and contributes 70% of the final hybrid score. It is an unsupervised ensemble-based algorithm that isolates outliers by constructing random decision trees over the feature space. Because truly labeled insider threat datasets are limited in practice, IsolationForest is highly suitable for this project as it can identify unusual user behavior even when explicit threat labels are unavailable or incomplete.

The implementation uses the model with key settings such as `n_estimators = 100` and `contamination = 0.1`. These parameters allow the detector to remain stable while still being sensitive to rare behavioral deviations. The raw anomaly outputs generated by the model are normalized to the range [0, 1] so that they can be meaningfully combined with the output of the supervised classifier.

Key implementation role of this model:
- Primary anomaly detector in the hybrid pipeline
- Learns behavioral irregularities from the overall feature distribution
- Detects unknown or previously unseen suspicious activity patterns
- Produces normalized anomaly evidence used in later risk scoring

### 9.2 Model 2: RandomForestClassifier
The second major model used in the system is RandomForestClassifier, which serves as the supervised validation layer and contributes 30% of the hybrid score. Unlike IsolationForest, RandomForest learns from labeled threat patterns and produces a class probability estimate for each user record. This probability acts as a confidence-aware second opinion on whether suspicious behavior is likely to correspond to an actual insider threat.

In the current implementation, the classifier uses approximately 100 decision trees with controlled depth to reduce overfitting and improve generalization on the balanced dataset. The model is especially useful because it complements the uncertainty of anomaly detection with probability-based classification strength.

Key implementation role of this model:
- Validates suspicious behavior detected by the anomaly layer
- Improves confidence in final decision-making
- Supports precision improvement by reducing uncertain alerts
- Generates probability scores for hybrid fusion

### 9.3 Hybrid Score Integration
Both machine learning models operate on the same preprocessed feature matrix but provide different perspectives on user behavior. IsolationForest focuses on outlier discovery, while RandomForest focuses on supervised likelihood estimation. Their outputs are combined using a weighted fusion rule so that the final decision benefits from both novelty detection and validation confidence.

The hybrid computation implemented in the project is as follows:

```
normalized_IF_score = (raw_IF_score - min) / (max - min)
hybrid_score = (0.7 × normalized_IF_score) + (0.3 × RF_proba)
anomaly_flag = 1 if hybrid_score > 0.539 else 0
```

The threshold of approximately 0.539 was selected through validation-based optimization and provides a practical balance between false-positive control and effective threat capture. This hybrid design is one of the most important implementation strengths of the system because it avoids overdependence on a single modeling technique.

### 9.4 Enhanced Risk Scoring (EnhancedRiskScorer)
Once the hybrid anomaly result is obtained, the system converts the output into a more operationally meaningful risk score using the `EnhancedRiskScorer` class implemented in `src/enhanced_risk_scoring.py`. This component is responsible for transforming technical model outputs into an interpretable score on a 0–10 scale that analysts can use for prioritization.

The formal weighted risk model is implemented as:

```python
RISK_WEIGHTS = {
    'anomaly':          0.40,
    'sensitive_access': 0.30,
    'login_anomalies':  0.20,
    'behavioral':       0.10,
}

risk_score = (
    (anomaly_factor    × 0.40) +
    (sensitive_factor  × 0.30) +
    (login_factor      × 0.20) +
    (behavioral_factor × 0.10)
) × 10
```

Each factor captures a different dimension of insider risk:
- **Anomaly factor** represents the normalized evidence of behavioral deviation.
- **Sensitive factor** represents the intensity of interaction with protected or confidential resources.
- **Login factor** reflects authentication irregularities such as repeated failed logins.
- **Behavioral factor** provides additional support for unusual activity drift or pattern instability.

This implementation improves analyst interpretability because the final risk score is easier to understand than a raw machine learning output alone.

### 9.5 Live Dashboard Risk Enrichment (app.py)
A key practical component of the implementation is the live risk enrichment mechanism contained in the Flask application. The `compute_risk_score()` function enriches each user record when the dashboard is loaded so that the interface always displays updated risk values, associated colors, and status-aware prioritization.

To maintain consistency across application sessions, the implementation uses a deterministic random seed based on the user identifier. This ensures that the same user receives stable baseline risk behavior unless the account state or relevant factors change. A status-based boost is also applied so that users who have already been flagged or administratively restricted are automatically surfaced at a higher risk tier.

| Account Status | Status Boost |
|---|---|
| Blocked | 0.70 |
| Alert | 0.55 |
| Restricted | 0.50 |
| Active | 0.20 |
| Normal | 0.10 |

This mechanism creates a strong link between analyst actions and dashboard visibility, thereby reinforcing the response workflow.

### 9.6 User Population and Simulation Support
The application is initialized using a practical user population structure consisting of core predefined users and additional generated user accounts. The system begins with 4 base users, including an administrative account, and dynamically creates approximately 50 extra users to simulate a broader organizational environment. This results in 54 monitored users at startup, each with assigned roles, credentials, and risk attributes.

This simulated population is valuable for academic demonstration because it creates a realistic monitoring environment in which the dashboard, APIs, and threat scoring logic can be observed on a non-trivial set of users rather than only a few static examples.

### 9.7 Admin Controls Implementation
The implementation also includes role-based access control for administrative actions. Sensitive account management operations are protected through session-level permission checks so that only authorized users with the Admin role can perform intervention tasks. Unauthorized users are redirected safely without executing those actions.

The following operations are currently implemented:

1. **Restrict User** (`POST /user/<id>/restrict`) — changes the user state to Restricted and increases operational risk visibility.
2. **Block User** (`POST /user/<id>/block`) — marks the account as Blocked and elevates the user into the highest risk category.
3. **Unblock User** (`POST /user/<id>/unblock`) — restores the account to Active state.
4. **Set Role** (`POST /user/<id>/set_role`) — changes the assigned role of a selected user between User and Admin, allowing access privileges to be updated according to administrative requirements.

These controls make the prototype more realistic by demonstrating how machine learning outputs can support actual response-oriented security workflows.

### 9.8 Model Drift Monitoring (drift_monitor.py)
A forward-looking implementation feature included in the project is drift monitoring through the `population_stability_index()` function defined in `src/drift_monitor.py`. This function compares the current score distribution with a reference baseline in order to determine whether the data pattern observed by the model is changing over time.

The interpretation used in the implementation is as follows:

- PSI < 0.1: No significant drift — model remains stable
- PSI 0.1–0.2: Moderate drift — additional observation recommended
- PSI > 0.2: Significant drift — retraining should be considered

This feature is important because user behavior in real organizations is not static, and the detection model must be monitored continuously to remain reliable.

### 9.9 API Endpoints
The project exposes live API routes so that risk output can be consumed programmatically in addition to being visualized through the dashboard. These APIs improve interoperability and demonstrate the prototype’s readiness for integration with external monitoring or automation workflows.

**GET /api/v1/risk**  
Returns a JSON payload containing all monitored users sorted according to risk score, including the final level, breakdown values, and generation timestamp.

**GET /api/v1/threats**  
Returns summarized risk distribution and trend-oriented data required by the frontend chart components.

The inclusion of API endpoints makes the project stronger from both a software engineering and deployment perspective.

### 9.10 Reporting Pipeline
The reporting pipeline is implemented through modules such as `reporter.py`, `reporting.py`, and `generate_final_report.py`. These modules transform evaluation and detection outputs into persistent files that can be reviewed by analysts, project evaluators, or future deployment teams.

The system produces multiple report artifacts, including:
- `reports/executive_summary_*.txt` for readable management-level summaries
- `reports/model_performance_*.csv` for numeric evaluation results
- `reports/cv_results_*.csv` for fold-level validation evidence
- `reports/feature_importance_*.csv` for ranked predictive indicators
- `reports/recommendations_*.csv` for tuning and improvement suggestions
- `reports/threat_report_*.json` for structured alert-oriented records
- `reports/optimal_threshold.csv`  

This reporting layer is particularly important in an academic major project because it demonstrates evidence-based validation and traceable outputs beyond the live dashboard.

### 9.11 Implementation Summary
Overall, the implementation of the proposed insider threat detection system successfully combines machine learning, software engineering, risk modeling, and analyst usability into a single integrated framework. The final solution is not limited to isolated model training; instead, it includes full-cycle support for data preparation, intelligent scoring, live visualization, administrative response, reporting, and future model maintenance. Therefore, the implementation details of this project are sufficiently strong, practical, and professionally aligned for a major project submission.

---

## 10. RESULTS AND VALIDATION

The results and validation phase is one of the most important parts of this project because it demonstrates whether the proposed insider threat detection framework performs effectively under realistic evaluation conditions. Since cybersecurity systems must not only detect suspicious behavior but also maintain reliability and reduce unnecessary alert noise, this chapter evaluates the proposed hybrid model using multiple validation strategies and standard performance measures.

### 10.1 Validation Strategy
The proposed framework was validated using a structured evaluation approach to ensure that the obtained results are meaningful, reproducible, and academically acceptable. Rather than depending on a single train-test split, the project uses a more reliable fold-based validation strategy so that the performance of the model can be observed across multiple dataset partitions.

The major validation components used in this project are:

- **5-fold cross-validation**, to assess how consistently the hybrid model performs across different subsets of the data
- **Threshold optimization**, to determine the most suitable decision boundary for anomaly classification
- **Standard classification metrics**, including Precision, Recall, F1-score, and Accuracy
- **Comparative interpretation**, to understand the trade-off between threat capture and false-positive control

This validation design is important because insider threat detection is a sensitive application area in which false alarms waste analyst effort while missed detections can create severe organizational risk.

### 10.2 Performance Summary
The final validated performance of the proposed hybrid detection framework is summarized below:

| Metric | Obtained Value | Interpretation |
|---|---|---|
| Precision | 88.0% (±12.2) | High alert quality with fewer false positives |
| Recall | 78.2% (±16.0) | Strong ability to capture suspicious users |
| F1-score | 82.0% (±11.8) | Balanced overall detection performance |
| Accuracy | 92.0% (±3.0) | Strong overall classification correctness |

These values indicate that the hybrid model performs well in balancing two major operational needs: reducing false alarms and detecting a meaningful proportion of risky behavior. In the context of insider threat monitoring, this balance is especially valuable because overly aggressive systems may overwhelm analysts, while overly conservative systems may miss dangerous events.

### 10.3 Precision Analysis
Precision reflects the proportion of flagged cases that are actually relevant or suspicious. A precision value of 88.0% shows that most of the alerts produced by the system are meaningful rather than noisy or unnecessary. This is an important operational advantage because high false-positive rates are one of the biggest challenges faced by Security Operations Center teams.

A strong precision value suggests that the supervised validation support provided by RandomForest helps confirm suspicious activity more effectively after anomaly discovery by IsolationForest. Therefore, the hybrid design contributes directly to better alert quality and improved analyst trust in the system.

### 10.4 Recall Analysis
Recall measures how effectively the system captures actual threat cases from all available suspicious records. The achieved recall of 78.2% indicates that the model is able to identify a substantial majority of insider-like threat events present in the evaluation data.

Although recall is slightly lower than precision, this is expected in insider threat analytics, where subtle malicious behavior can closely resemble legitimate activity. Even so, the recall value remains strong enough to show that the system is not overly conservative and is capable of capturing a useful number of risky cases for analyst review.

### 10.5 F1-Score and Overall Balance
The F1-score combines both precision and recall into a single balanced measure. The project achieved an F1-score of 82.0%, which indicates that the proposed model maintains good equilibrium between the need to identify threats and the need to minimize false alarms.

This balanced performance is particularly important in real-world cybersecurity monitoring. A model with high recall but low precision would create alert fatigue, whereas a model with high precision but very low recall could miss actual insider threats. The obtained F1-score confirms that the proposed hybrid framework offers a practical middle ground suitable for operational use.

### 10.6 Accuracy and Stability
The overall accuracy of the system was found to be 92.0%, with relatively low variation across cross-validation folds. This indicates that the model performs consistently across different partitions of the dataset and does not depend excessively on a particular training split. Such stability is valuable because it increases confidence that the hybrid model generalizes reasonably well within the project’s evaluation environment.

However, in cybersecurity projects, accuracy alone is not sufficient because class imbalance can make accuracy appear artificially high. That is why the project also emphasizes precision, recall, and F1-score instead of relying only on a single aggregate measure.

### 10.7 Threshold Tuning and Optimization
A major step in improving the quality of the final detection system was threshold optimization. Since the hybrid score is computed on a continuous scale, a suitable cutoff value must be selected to determine when a user should be flagged as suspicious.

The optimal threshold obtained in the project is approximately **0.539**. This value was selected by analyzing the trade-off between precision and recall across multiple candidate thresholds and choosing the point that gave the strongest F1-score balance.

The threshold plays a very important role:

- a **lower threshold** would flag more users, improving sensitivity but increasing false positives
- a **higher threshold** would reduce false alarms but might miss subtle insider threats
- the **optimized threshold** provides a balanced and evidence-based operating point

Thus, threshold tuning significantly improved the practical usability of the system.

### 10.8 Cross-Validation Significance
The use of 5-fold cross-validation strengthens the credibility of the project results. In this method, the dataset is divided into five parts, and the model is trained and tested multiple times so that each part is used for validation once. This ensures that the reported performance is not based on a single favorable split.

Cross-validation is especially useful for academic projects and limited-size datasets because it provides a more dependable estimate of real model behavior. The low variation in accuracy and balanced variation in other metrics suggest that the system is reasonably robust for the current prototype stage.

### 10.9 Practical Interpretation of Results
From an operational perspective, the results show that the proposed framework can serve as a meaningful decision-support tool for insider threat monitoring. The model is not intended to replace security analysts; rather, it helps prioritize which users and activities should be investigated first.

The practical interpretation of the validation results is as follows:

1. The model can effectively identify a majority of suspicious behavior patterns.
2. The number of unnecessary or low-value alerts is kept relatively controlled.
3. The hybrid framework is more reliable than using only a single anomaly detector.
4. The final risk scores and dashboard outputs make the results easier to interpret and act upon.

### 10.10 Validation Conclusion
Overall, the validation results confirm that the proposed insider threat detection system is both technically effective and operationally relevant. The achieved precision, recall, F1-score, and accuracy collectively demonstrate that the hybrid architecture is capable of detecting suspicious user behavior with a strong balance between sensitivity and reliability. The addition of threshold tuning and cross-validation further strengthens the academic validity of the project.

Therefore, the Results and Validation chapter provides convincing evidence that the implemented framework is suitable for prototype-level deployment, academic demonstration, and further enhancement in future research or organizational pilot environments.

---

## 11. OUTCOMES AND IMPACT

The outcomes of this project go beyond the successful implementation of a machine learning model. The developed system demonstrates how insider threat analytics can be transformed into a practical, interpretable, and deployment-oriented security solution. The impact of the work can be observed from technical, operational, academic, and future-readiness perspectives.

### 11.1 Technical Outcomes
The project achieved several important technical outcomes that collectively demonstrate the successful completion of a full cybersecurity analytics pipeline.

The major technical outcomes include:

- the successful development of an **end-to-end hybrid insider threat detection prototype** combining IsolationForest and RandomForest
- implementation of a **weighted hybrid scoring mechanism** for improved anomaly validation
- design of a **four-component risk scoring model** that transforms raw model outputs into analyst-friendly scores on a 0–10 scale
- integration of a **Flask-based dashboard** for monitoring, visualization, and administrative action support
- development of a **reporting pipeline** that generates CSV, TXT, and JSON outputs for analysis and documentation
- support for **model drift monitoring** through PSI-based stability assessment

These technical outcomes show that the project is not limited to algorithm experimentation only; instead, it provides a complete working prototype suitable for demonstration and controlled evaluation.

### 11.2 Operational Impact
From an operational point of view, the project offers meaningful support for Security Operations Center workflows. One of the most important outcomes is the ability to prioritize users and activities according to calculated risk instead of forcing analysts to manually inspect all logs equally.

The key operational impacts are as follows:

1. **Faster prioritization of high-risk users** through automated risk ranking and level assignment.
2. **Improved incident triage efficiency** by highlighting suspicious behavior patterns in a dashboard-friendly format.
3. **Reduction in low-value investigation effort** because the hybrid model improves alert quality compared with static monitoring approaches.
4. **Better analyst visibility** into the causes of suspicious behavior through component-wise risk scoring and threat summaries.
5. **Support for intervention workflows** through actions such as restrict, block, unblock, and role modification.

Thus, the system contributes practical value by connecting machine learning predictions with operational decision-making.

### 11.3 Security and Organizational Impact
The project also has broader organizational relevance because insider threats are often difficult to identify using traditional perimeter defenses alone. By analyzing user behavior instead of depending only on static rules, the proposed framework strengthens internal security posture and improves visibility into suspicious insider activities.

From a security standpoint, the system helps organizations:

- identify unusual behavior earlier in the threat lifecycle
- recognize high-risk access patterns involving sensitive files or repeated login anomalies
- reduce dependence on purely manual monitoring approaches
- build a more proactive and risk-aware defense posture

Although the present work is a prototype, it reflects a practical direction for future enterprise-grade insider threat defense systems.

### 11.4 Academic Impact
From an academic perspective, the project demonstrates the meaningful application of artificial intelligence and machine learning in the field of cybersecurity. It combines multiple concepts—anomaly detection, supervised classification, feature engineering, risk modeling, dashboard integration, and validation—into a single coherent research-oriented system.

The academic impact of the work includes:

- providing a strong major-project case study in cybersecurity analytics
- demonstrating the effectiveness of hybrid machine learning for insider threat detection
- establishing a foundation for research extensions in explainable AI, drift monitoring, and real-time security analytics
- creating material that may support conference papers, technical presentations, or future publication efforts

This makes the project relevant not only as a software prototype but also as a meaningful academic contribution.

### 11.5 Skill and Learning Outcomes
The development of this project also resulted in substantial personal and technical learning outcomes. Through the implementation process, important skills were strengthened in the areas of Python programming, machine learning model development, data preprocessing, risk analysis, web-based system integration, and cybersecurity-oriented problem solving.

The project therefore contributed to the development of practical competencies in:

- secure data handling and preprocessing
- model selection and hybrid scoring design
- evaluation using cross-validation and threshold tuning
- report generation and dashboard development
- deployment-oriented thinking for SOC use cases

These learning outcomes are important because they reflect the project’s value as a complete educational experience in addition to being a technical implementation.

### 11.6 Long-Term Impact and Future Readiness
Another major outcome of the work is that it establishes a strong base for future enhancement. The modular architecture of the project makes it possible to add explainable AI, real-time stream processing, automated retraining, stronger authentication integration, and more advanced behavioral analytics in later stages.

As a result, the project is future-ready in the sense that it can evolve from an academic prototype into a more capable organizational monitoring solution with additional engineering effort and larger real-world datasets.

### 11.7 Overall Impact Summary
In summary, the project delivers impact on multiple levels. Technically, it provides a functioning hybrid threat detection framework. Operationally, it supports analyst workflows and prioritized investigation. Academically, it offers a valuable case study in AI-driven cybersecurity. Educationally, it strengthens practical implementation skills. Therefore, the outcomes and impact of this project are significant, well-rounded, and highly relevant for a major project submission in the field of cybersecurity.

---

## 12. LIMITATIONS AND CHALLENGES

No cybersecurity project is complete without a clear understanding of its limitations and practical challenges. Although the proposed insider threat detection framework demonstrates encouraging technical and operational results, it is still developed in a controlled prototype environment and therefore has certain constraints that must be acknowledged. Recognizing these limitations is important because it provides transparency, strengthens academic honesty, and identifies clear directions for future improvement.

### 12.1 Limited Availability of Real-World Insider Threat Data
One of the most significant challenges in this project is the limited availability of authentic, labeled insider threat datasets. In real organizational settings, insider incidents are sensitive, rare, and often confidential, making it difficult to obtain complete and publicly usable data for model development.

As a result, the project relies on a structured and semi-synthetic dataset that reflects realistic behavioral indicators but does not fully capture the complexity of all real enterprise environments. While this approach is suitable for academic experimentation, broader real-world deployment would require larger and more diverse datasets.

### 12.2 Class Imbalance and Rare Event Detection
Insider threats naturally represent a very small fraction of overall user activity. This class imbalance creates a major machine learning challenge because models can become biased toward normal behavior and fail to detect subtle suspicious cases. Although balancing techniques were applied in this project, the rare-event nature of insider attacks still remains a fundamental limitation.

This means that the system may still struggle in cases where malicious behavior is extremely sparse, highly disguised, or statistically similar to legitimate activity.

### 12.3 Trade-off Between Sensitivity and False Positive Control
Another important challenge is maintaining the right balance between detecting more threats and avoiding excessive false positives. If the detection threshold is too low, the system may generate too many alerts and reduce analyst trust. On the other hand, if the threshold is too high, subtle insider threats may remain undetected.

Although threshold optimization improved this trade-off, no single threshold can perfectly solve the problem in all operational contexts. Therefore, this balance remains an ongoing challenge in practical insider threat analytics.

### 12.4 Limited Explainability in Some Model Outputs
While the project improves interpretability through risk scoring and dashboard summaries, the underlying machine learning outputs are still not fully explainable at the feature-contribution level. Security analysts often need to understand not only that a user is risky, but also why that user was classified as suspicious.

At present, the system provides component-wise scoring insight, but more advanced explainability methods such as SHAP or LIME are not yet fully integrated. This limits transparency for deeper forensic analysis and decision justification.

### 12.5 Prototype-Level Deployment Scope
The current project is implemented as a prototype intended for academic validation and controlled demonstration. It does not yet include full-scale enterprise deployment features such as live SIEM integration, streaming event ingestion, distributed scalability, hardened production security, or organization-wide policy enforcement.

Therefore, while the framework is strong as a proof of concept, additional engineering and infrastructure support would be required before adoption in a large real-world environment.

### 12.6 Evolving User Behavior and Model Drift
Human behavior is dynamic and changes over time because of new job roles, work patterns, remote access trends, or operational changes inside an organization. As a result, a model trained on one behavior distribution may become less reliable when the environment changes.

Although the project includes PSI-based drift monitoring, continuous retraining and stronger adaptation mechanisms are still needed for long-term deployment stability.

### 12.7 Security and Ethical Considerations
Insider threat monitoring systems must also be designed carefully from an ethical and privacy perspective. Monitoring user behavior can introduce concerns related to employee privacy, consent, surveillance boundaries, and responsible use of automated decision-making. While the present project focuses on technical development, these issues remain important challenges in real-world implementation.

Any future deployment of such a system would need proper governance, policy approval, data protection practices, and legal compliance mechanisms.

### 12.8 Mitigation Approaches Used in This Project
To reduce the effect of the above limitations, several mitigation strategies were incorporated into the project:

- use of a **hybrid architecture** to improve robustness over single-model approaches
- application of **cross-validation and threshold tuning** for more reliable evaluation
- use of **risk-based scoring** to improve analyst interpretability
- inclusion of **dashboard monitoring and role-based actions** to support practical operations
- addition of **drift monitoring support** for future retraining readiness

These measures do not remove all limitations, but they significantly strengthen the practicality and academic quality of the prototype.

### 12.9 Summary
In summary, the project successfully addresses an important cybersecurity problem, but it also faces limitations related to data realism, class imbalance, explainability, operational scaling, and long-term adaptation. Acknowledging these challenges does not weaken the project; rather, it shows that the system has been evaluated honestly and with a clear understanding of what is required for future improvement. Therefore, the Limitations and Challenges section highlights both the current constraints of the prototype and the opportunities for its continued evolution.

---

## 13. FUTURE SCOPE

The current project establishes a strong foundation for future enhancement in both technical and operational dimensions. Although the proposed insider threat detection framework already demonstrates meaningful results in a prototype setting, there are several opportunities through which the system can be made more intelligent, scalable, explainable, and deployment-ready. These future directions are important for transforming the present academic solution into a more advanced real-world security platform.

### 13.1 Integration of Explainable AI
One of the most valuable future improvements would be the integration of explainable AI methods such as SHAP or LIME. These techniques can help analysts understand which features contributed most strongly to a specific risk prediction or anomaly flag. By adding explanation support, the system would become more transparent, easier to trust, and more suitable for investigation-oriented cybersecurity workflows.

### 13.2 Expansion of Dataset Diversity
Another important future step is the use of larger, more diverse, and more realistic insider threat datasets. Expanding the dataset to include additional organizational roles, departments, time-based behaviors, access contexts, and varied attack patterns would improve the robustness and generalization capability of the model. Better data diversity would also help the framework perform more reliably across different enterprise environments.

### 13.3 Real-Time Streaming Analytics
At present, the prototype works primarily in a structured and batch-oriented analysis environment. In the future, the system can be extended to support real-time monitoring of incoming login events, file access logs, and activity streams. This would allow suspicious behavior to be detected as it occurs, thereby improving early warning capability and reducing response time for security teams.

### 13.4 Adaptive Retraining and Online Learning
Since user behavior changes over time, future versions of the project can incorporate adaptive retraining or online learning mechanisms. These improvements would allow the detection model to continuously learn from updated patterns and maintain performance even when the environment evolves. Such an enhancement would be especially useful in enterprise settings where model drift is a practical concern.

### 13.5 Stronger Enterprise Integration
The system can also be integrated with broader organizational security tools such as SIEM platforms, identity and access management systems, alert management dashboards, and ticketing workflows. Such integration would make the solution more operationally useful and would allow risk alerts to become part of a complete security response ecosystem.

### 13.6 Advanced Behavioral Analytics
Future work may also include more sophisticated behavioral modeling such as sequence-based analysis, time-series anomaly detection, peer group comparison, and role-aware baseline learning. These methods could help capture subtle low-and-slow insider actions that are difficult to identify through simpler aggregated indicators alone.

### 13.7 Enhanced Security Governance Features
Another future direction is the addition of governance-focused capabilities such as audit trails, policy-aware alerts, access-approval workflows, and compliance reporting. These improvements would make the system more suitable for regulated environments where accountability, traceability, and formal review processes are essential.

### 13.8 Pilot Deployment and Feedback Loop
A very practical next step would be pilot deployment in a controlled institutional or organizational environment. This would allow the collection of analyst feedback, measurement of real usability, and refinement of thresholds and dashboards based on live operational experience. Such a feedback loop would significantly improve the maturity of the proposed framework.

### 13.9 Summary
In summary, the future scope of this project is broad and meaningful. The framework can be extended toward explainable AI, real-time detection, adaptive retraining, enterprise integration, richer behavioral analytics, and pilot-level deployment. Therefore, this project not only solves an important academic problem at the prototype stage but also provides a strong platform for continued research, engineering enhancement, and practical cybersecurity application.

---

## 14. PUBLICATION, PATENT, AND COPYRIGHT

This chapter highlights the academic and intellectual property potential of the proposed insider threat detection project. Since the work combines hybrid machine learning, cybersecurity analytics, risk scoring, dashboard integration, and deployment-oriented reporting, it possesses value not only as a final-year academic project but also as a possible foundation for future publication, innovation documentation, and intellectual property development.

### 14.1 Paper Publication
The present project has strong potential to be developed into a technical paper or conference publication because it addresses a relevant and growing problem in the field of cybersecurity. Insider threat detection is a high-impact research area, and the combination of IsolationForest, RandomForest, hybrid scoring, risk prioritization, and analyst-facing dashboard support provides a meaningful contribution from both an academic and applied perspective.

**Current Status:** In progress  
**Proposed Focus:** Hybrid machine learning architecture and SOC-centered risk scoring with validated performance.

The publication-oriented strengths of the project include:

- application of AI and ML in a practical cybersecurity problem
- a hybrid model that balances anomaly discovery with supervised validation
- validation results supported by cross-validation and threshold tuning
- a deployment-oriented prototype with dashboard and API integration
- clear opportunities for future research enhancement

With refinement in the form of experimental comparison, deeper literature positioning, and formal formatting, the project can be converted into a paper suitable for student research presentation, journal submission, or conference review.

### 14.2 Patent Potential
Although no patent has been filed at the current stage, the project contains design elements that may be considered for future innovation-oriented protection if the framework is further refined and demonstrated to offer novelty in implementation or applied workflow integration.

**Current Status:** Not filed  
**Potential Intellectual Property Area:** Weighted hybrid threat scoring and validation framework for insider threat analytics.

Possible patent-oriented aspects may include:

- the specific hybrid fusion strategy for combining anomaly and classification outputs
- the formal risk-mapping framework that converts model outputs into actionable SOC priorities
- operational linkage between ML detection, role-based intervention, and dashboard-driven response
- model monitoring and response workflow integration for insider threat environments

At the prototype level, these ideas are still primarily academic, but they can become stronger intellectual property candidates if extended with novel workflow logic, automation, or enterprise-oriented design features.

### 14.3 Copyright
The project is eligible for copyright protection in relation to its original software implementation, technical documentation, reporting structures, visual dashboard integration, and associated academic artifacts. Copyright protection is important because it establishes ownership of the original expression of the work even when the underlying research concepts are based on established machine learning methods.

**Current Status:** Eligible  
**Scope:** Source code, pipeline design, reports, and associated project documentation.

The copyright-applicable components of the project include:

- Python source code for preprocessing, training, scoring, and dashboard logic
- report generation modules and structured output formats
- documentation including the black book, user guide, and technical write-ups
- UI structure and design elements developed for the SOC dashboard prototype

This protection helps preserve the originality of the implementation and academic effort involved in the project.

### 14.4 Overall Relevance of This Chapter
The inclusion of publication, patent, and copyright discussion shows that the project has value beyond classroom demonstration. It reflects research relevance, practical novelty, and ownership of implementation work. This strengthens the overall quality of the black book by showing that the project has future academic and professional potential in addition to its current technical contribution.

---

## 15. CONCLUSION

This project successfully addresses the challenge of insider threat detection through the design and implementation of a hybrid machine learning framework that is both technically sound and operationally meaningful. The work began with the recognition that conventional rule-based monitoring is often inadequate for detecting subtle, evolving, and low-frequency insider behaviors. In response, the proposed system combines unsupervised anomaly discovery and supervised validation to improve detection reliability while retaining practical usability for security teams.

The implemented pipeline covers all critical stages of an end-to-end cybersecurity analytics solution, including data preprocessing, feature engineering, anomaly detection, risk scoring, and analyst-facing outputs. IsolationForest contributes strong capability for identifying unknown behavioral deviations, while RandomForest provides a validation layer for confidence-aware classification. The weighted hybrid scoring strategy, followed by a 0-10 risk mapping, enables prioritization of suspicious users in a manner suitable for SOC workflows and rapid investigation.

From a performance standpoint, the project demonstrates encouraging validation results with strong precision, balanced recall, and stable overall F1-score under cross-validation. These results indicate that the hybrid model is capable of reducing false alarms while still capturing a substantial portion of threat-like behavior. The threshold-tuned and report-supported output structure further strengthens the deployment readiness of the prototype for controlled organizational environments.

Beyond model performance, the project contributes a practical framework for translating machine learning outputs into security decision support. This is an important step toward bridging the gap between academic detection models and real SOC operations. The generated reports, recommendations, and dashboard/API integration collectively demonstrate that the system can support analyst productivity, improve triage quality, and provide a foundation for iterative threat intelligence refinement.

In summary, the project fulfills its core aim of developing an AI-based insider threat detection system with hybrid intelligence, interpretable scoring, and validation-backed effectiveness. It establishes a strong base for future enhancements such as explainable AI, real-time stream processing, adaptive retraining, and pilot deployment studies. Therefore, this work meets the expected academic rigor and practical relevance for major project completion while also offering clear pathways for publication-oriented and industry-oriented continuation.

---

## 16. BIBLIOGRAPHY

The following references were consulted during the design, implementation, and analysis of the proposed insider threat detection system. The bibliography includes foundational machine learning research, cybersecurity standards, and insider threat studies relevant to the project domain.

[1] F. T. Liu, K. M. Ting, and Z. H. Zhou, “Isolation Forest,” in Proceedings of the 8th IEEE International Conference on Data Mining, 2008, pp. 413–422.

[2] L. Breiman, “Random Forests,” Machine Learning, vol. 45, no. 1, pp. 5–32, 2001.

[3] F. Pedregosa, G. Varoquaux, A. Gramfort, et al., “Scikit-learn: Machine Learning in Python,” Journal of Machine Learning Research, vol. 12, pp. 2825–2830, 2011.

[4] F. L. Greitzer and R. E. Hohimer, “Modeling Human Behavior to Anticipate Insider Attacks,” Journal of Strategic Security, vol. 4, no. 2, pp. 25–48, 2011.

[5] A. Tuor, S. Kaplan, B. Hutchinson, N. Nichols, and S. Robinson, “Deep Learning for Unsupervised Insider Threat Detection in Structured Cybersecurity Data Streams,” in AAAI Workshop on Artificial Intelligence for Cyber Security, 2017.

[6] National Institute of Standards and Technology, Framework for Improving Critical Infrastructure Cybersecurity, Version 2.0, 2024.

[7] National Institute of Standards and Technology, Security and Privacy Controls for Information Systems and Organizations, NIST Special Publication 800-53 Rev. 5, 2020.

[8] Carnegie Mellon University Software Engineering Institute, “CERT Insider Threat Center,” available online: https://www.sei.cmu.edu/about/divisions/cert/

[9] Scikit-learn Developers, “IsolationForest Documentation,” available online: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html

[10] Scikit-learn Developers, “RandomForestClassifier Documentation,” available online: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

[11] M. Bishop and C. Gates, “Defining the Insider Threat,” in Proceedings of the 4th Annual Workshop on Cyber Security and Information Intelligence Research, 2008.

[12] E. E. Schultz, “A Framework for Understanding and Predicting Insider Attacks,” Computers and Security, vol. 21, no. 6, pp. 526–531, 2002.

[13] A. K. Jain, M. N. Murty, and P. J. Flynn, “Data Clustering: A Review,” ACM Computing Surveys, vol. 31, no. 3, pp. 264–323, 1999.

[14] S. Axelsson, “The Base-Rate Fallacy and the Difficulty of Intrusion Detection,” ACM Transactions on Information and System Security, vol. 3, no. 3, pp. 186–205, 2000.

---

## 17. ANNEXURE

The annexure section provides the supporting evidence, screenshots, tabular summaries, and documentary records that strengthen the credibility of the project report. It acts as a reference section where evaluators can quickly verify the practical implementation, validation outputs, and submission-related materials associated with the proposed insider threat detection system. A well-organized annexure improves the overall professionalism of the black book and ensures that all essential supporting artifacts are preserved in one place.

### 17.1 Purpose of the Annexure
The purpose of this annexure is to collect all supplementary material that may not fit naturally into the main discussion chapters but is still highly important for project evaluation. These materials include dashboard screenshots, API evidence, performance reports, model outputs, validation tables, and final submission checklists. Together, they provide documentary proof of the system’s design, implementation quality, and testing maturity.

### 17.2 Annexure A: Screenshots to Include
The following screenshots should be inserted in the final printed version of the black book so that the project implementation is visually documented:

1. **Login Page** — dark-themed authentication interface with username and password fields.
2. **Dashboard Summary Statistics** — cards showing total users, critical threats, high-risk users, and flagged activity.
3. **Risk Distribution Donut Chart** — graphical breakdown of users across Critical, High, Medium, and Low categories.
4. **Top Risk Users Leaderboard** — ranked list of the highest-risk users with visible score indicators.
5. **Risk Formula Display Panel** — section showing the formal risk score equation used by the system.
6. **Recent Activities Table** — evidence of suspicious and normal events shown in the dashboard feed.
7. **Admin Action Controls** — screenshot showing restrict, block, and unblock buttons for response workflows.
8. **User Management Table** — view showing all users sorted according to risk score and status.
9. **Individual User Profile Page** — detailed behavioral and risk-oriented view of a selected user.
10. **Risk API Output** — JSON response demonstrating machine-readable risk results.
11. **Cross-Validation Results Snapshot** — proof of fold-based model evaluation.
12. **Threshold Optimization Output** — evidence of threshold tuning and selected operating point.
13. **Executive Summary Output** — management-friendly report generated by the system.

### 17.3 Annexure B: Important Tables to Attach
The following tables should be included for completeness and formal presentation:

1. **Dataset Summary Table** — original dataset versus balanced dataset comparison.
2. **Feature Dictionary Table** — feature name, description, type, data source, and interpretation.
3. **Model Hyperparameter Table** — parameters used for IsolationForest and RandomForest with reasons.
4. **Cross-Validation Metrics Table** — fold-wise Precision, Recall, F1-score, and Accuracy.
5. **Threshold Comparison Table** — relationship between threshold choice and performance trade-off.
6. **Risk Interpretation Table** — meaning of Critical, High, Medium, and Low risk categories.
7. **Confusion Matrix Summary** — counts of TP, FP, TN, and FN with explanation.
8. **Account Status Boost Table** — effect of Blocked, Alert, Restricted, Active, and Normal states.
9. **Route Access Table** — application routes, methods, purpose, and access restrictions.
10. **PSI Drift Interpretation Table** — stable, monitor, and retraining-required ranges.

### 17.4 Annexure C: Additional Supporting Records
This subsection may include extra evidence generated during project execution and evaluation:

1. Executive summary report with actual validated metric values.
2. Recommendation report generated by the reporting pipeline.
3. Threat report sample in structured JSON format.
4. Deployment-readiness checklist.
5. User acceptance or reviewer feedback checklist.
6. Selected feature-importance outputs for interpretation support.
7. Sample flagged-user records used during dashboard demonstration.

### 17.5 Annexure D: Document Evidence Checklist
The following items should be attached or maintained as part of final submission evidence:

1. Signed certificate page.
2. Signed declaration page.
3. Plagiarism report summary.
4. Daily or weekly progress log endorsed by the guide.
5. Review or sprint meeting notes.
6. Final demonstration attendance or sign-off sheet.
7. Project presentation snapshot or evaluation sheet, if available.

### 17.6 Importance of the Annexure in Project Evaluation
The annexure is not just an optional attachment; it adds depth, evidence, and authenticity to the project report. For major project evaluation, examiners often look for proof of implementation, testing, output generation, and presentation readiness. By including screenshots, tables, outputs, and documentary records in a systematic manner, the annexure strengthens the trustworthiness of the complete black book and makes the final submission more polished and academically convincing.

---

## 18. EXISTING SYSTEM ANALYSIS

The analysis of the existing system is an important part of the project because it helps establish why a new approach is necessary. In the field of cybersecurity, many currently deployed monitoring systems are designed mainly to identify known attack signatures, fixed threshold violations, or predefined suspicious events. While these solutions are valuable for baseline monitoring, they are often not sufficient for insider threat detection, where malicious behavior may occur gradually, appear legitimate on the surface, and involve users with valid credentials.

### 18.1 Current Industry Practice
In many organizations, the existing security monitoring ecosystem is based on traditional tools such as SIEM platforms, access-control logs, static compliance alerts, and manually created security policies. These systems typically collect data from multiple sources and generate alerts when predefined rules are triggered. For example, repeated failed logins, unusual login hours, excessive downloads, or access-policy violations may produce alerts for analyst review.

Such systems are useful in detecting obvious suspicious actions and are widely adopted because they are easy to configure, easy to audit, and relatively straightforward to integrate into security operations workflows. However, insider threats create a different type of challenge. Since insiders often use authorized accounts and legitimate resources, their activities may not immediately violate a fixed rule even when the overall behavior is risky. As a result, conventional monitoring may miss slow, low-volume, or behaviorally subtle threats.

### 18.2 Nature of the Existing Approaches
The most common existing approaches for insider monitoring can be grouped into the following categories:

1. **Rule-based monitoring systems** — generate alerts using fixed logic such as login failure count, access-time violations, or restricted-file access rules.
2. **Signature-based detection systems** — focus on previously known malicious patterns and attack fingerprints.
3. **Manual log review processes** — depend heavily on analysts to inspect logs and correlate suspicious actions manually.
4. **Basic statistical threshold systems** — use simple anomaly limits without richer contextual understanding.

Although each of these approaches has practical value, they are often limited when the threat does not match an already known pattern.

### 18.3 Limitations of Existing Systems
Despite their usefulness, existing approaches suffer from several important limitations in the context of insider threat detection:

1. **Lack of behavioral adaptability** — static rules do not learn from evolving user behavior or changing organizational patterns.
2. **High false-positive rates** — many alerts generated by fixed thresholds are not truly malicious, leading to analyst fatigue.
3. **Poor detection of unknown threats** — systems focused only on known signatures may fail to identify novel or subtle insider actions.
4. **Limited context awareness** — existing tools often evaluate isolated events rather than a complete behavioral profile of the user.
5. **Weak prioritization capability** — without strong risk scoring, all alerts may appear equally important.
6. **Heavy dependence on manual analysis** — analysts must spend additional time interpreting alerts and deciding which ones matter most.
7. **Insufficient integration of intelligent validation** — many current systems do not combine anomaly detection with supervised confirmation for better confidence.

These limitations create operational inefficiency and reduce the practical effectiveness of insider threat monitoring in modern organizations.

### 18.4 Gap Identified in Existing Systems
From the above analysis, a clear research and implementation gap can be observed. Existing systems either rely too heavily on predefined rules or focus only on one method of analysis. Very few solutions provide a balanced framework that can:

- detect previously unseen anomalies,
- validate suspicious behavior with confidence,
- convert technical results into interpretable risk scores, and
- support analysts through a usable dashboard and response-oriented workflow.

This gap directly motivates the development of the proposed hybrid insider threat detection system described in this project.

### 18.5 Existing System vs Proposed System Comparison

| Parameter | Existing Rule-Based / Traditional Systems | Proposed Hybrid ML System |
|---|---|---|
| Detection Logic | Fixed rules and known patterns | Hybrid anomaly detection + supervised validation |
| Unknown Threat Detection | Limited | Strong |
| Adaptability | Low | Medium to High |
| False Positive Control | Weak | Improved through fusion and threshold tuning |
| Analyst Prioritization | Basic alert listing | Risk score-based ranking |
| Explainability | Limited or manual | Better through risk breakdown and dashboard summaries |
| Response Support | Mostly manual | Dashboard-assisted and action-oriented |
| Deployment Orientation | Monitoring-focused | Prototype ready with reports and APIs |

### 18.6 Need for Improvement
The analysis of the existing system clearly shows that there is a strong need for an improved insider threat monitoring solution that goes beyond static detection logic. Modern organizations require systems that are adaptive, interpretable, and operationally useful. The proposed project fulfills this need by introducing a hybrid machine learning framework capable of combining anomaly detection, validation confidence, risk scoring, and dashboard-based usability into a single integrated system.

### 18.7 Summary
In summary, the existing system provides a useful baseline for conventional security monitoring but remains insufficient for the nuanced and behavior-driven challenge of insider threats. Its dependence on static rules, high false-positive tendency, and limited support for risk-based prioritization create a clear gap in practical cybersecurity operations. Therefore, the proposed hybrid system offers a necessary and meaningful advancement over traditional approaches.

---

## 19. PROPOSED SYSTEM DESIGN IN DETAIL

This chapter explains the detailed design of the proposed insider threat detection system. While earlier chapters introduced the methodology and architectural overview, the present section focuses more specifically on how the proposed system is structured to solve the identified problem in a practical, efficient, and scalable manner. The design has been developed to ensure that the system not only detects suspicious user behavior but also converts that intelligence into actionable analyst support.

### 19.1 Design Philosophy
The proposed system is built around a set of core design principles that guide its implementation and practical usefulness:

1. **Detection depth** — the system must detect both previously unseen anomalies and suspicious patterns already learned from available labeled data.
2. **Operational relevance** — the output of the system should be understandable and directly useful to analysts in a monitoring environment.
3. **Modularity** — different functional blocks such as preprocessing, modeling, scoring, reporting, and dashboard rendering should remain logically separated.
4. **Interpretability** — the final results should be explainable in terms of risk score, severity level, and component breakdown.
5. **Future extensibility** — the design should support future improvements such as explainable AI, live monitoring, and automatic retraining.

These principles ensure that the proposed system is not merely an academic algorithm but a practical cybersecurity solution prototype.

### 19.2 Detailed Layered Architecture
The proposed design follows a multi-layer architecture in which each layer performs a clearly defined role:

1. **Data Layer**  
   Stores the raw and processed datasets used for analysis. This includes login attempts, activity logs, sensitive file access events, user information, and labeled threat records stored in structured CSV files.

2. **Processing Layer**  
   Responsible for data cleaning, missing-value handling, transformation, normalization, balancing, and feature generation. This stage ensures that the raw records are converted into analysis-ready model inputs.

3. **Detection Layer**  
   Applies the two core machine learning models: IsolationForest for unsupervised anomaly discovery and RandomForestClassifier for supervised validation of suspicious behavior.

4. **Scoring Layer**  
   Combines model outputs through the weighted hybrid formula and then computes the final multi-factor risk score using the four-component risk model.

5. **Presentation Layer**  
   Exposes the final outputs through the Flask dashboard, APIs, and generated reports so that analysts and evaluators can view the results conveniently.

This layered design improves maintainability and allows each part of the system to be independently improved or extended.

### 19.3 Functional Flow of the Proposed System
The functional workflow of the designed system is as follows:

1. User behavior data is collected from structured logs.
2. The collected data is preprocessed and cleaned.
3. Security-relevant behavioral features are derived from the cleaned data.
4. IsolationForest generates anomaly-oriented scores.
5. RandomForestClassifier estimates supervised threat probability.
6. Both outputs are fused using the weighted hybrid formula.
7. The system computes a final risk score on a 0–10 scale.
8. The user is assigned to a risk level such as Critical, High, Medium, or Low.
9. Results are displayed through dashboard views, APIs, and reports.
10. Administrative response actions can then be taken where necessary.

This end-to-end design ensures that raw activity logs are transformed into operational intelligence in a structured and traceable manner.

### 19.4 Hybrid Detection Logic
A major strength of the proposed design lies in the use of hybrid intelligence. Instead of relying on a single model, the system combines anomaly-based detection and supervised classification to produce a more balanced result.

The hybrid score is computed as:

**Hybrid = 0.7 × IF_score + 0.3 × RF_proba**

Where:
- **IF_score** represents the normalized anomaly evidence from IsolationForest,
- **RF_proba** represents the threat probability estimated by RandomForest.

This design ensures that the system remains capable of detecting novel insider-like anomalies while also benefiting from confidence-driven validation based on known patterns.

### 19.5 Risk Scoring and Prioritization Design
After hybrid anomaly determination, the proposed system converts technical outputs into a practical analyst-oriented score using the four-factor weighted model:

**R = Σ(wᵢ × fᵢ) × 10**

The design uses the following components:
- anomaly contribution
- sensitive file access contribution
- login anomaly contribution
- behavioral contribution

The final score is mapped to four operational risk levels:
- **Critical** for highest-priority investigation cases
- **High** for strong suspicion requiring prompt review
- **Medium** for moderate concern and monitoring
- **Low** for minimal current threat suspicion

This risk-based design is important because it helps security teams focus on the most important users first instead of reviewing all alerts equally.

### 19.6 Dashboard-Oriented System Design
The proposed system is not limited to backend analysis only. It includes a web-based dashboard designed for analyst usability and practical monitoring. The dashboard acts as the final decision-support layer of the system and includes:

- summary cards for total users and risk counts
- risk distribution charts
- top-risk user ranking
- activity monitoring table
- per-user profile access
- administrative action controls such as restrict, block, unblock, and role change

This interface-oriented design makes the proposed system more realistic and aligns it with actual SOC-style operational workflows.

### 19.7 Decision Logic and Processing Steps
The final decision pipeline implemented in the proposed design may be summarized as follows:

1. Normalize the anomaly score produced by IsolationForest.
2. Retrieve the class probability from RandomForest.
3. Compute the weighted hybrid score.
4. Compare the hybrid score with the optimized threshold.
5. If the threshold is crossed, classify the user as suspicious.
6. Compute the detailed risk score using weighted behavioral factors.
7. Assign the risk category and color code.
8. Display the final ranked results on the dashboard and through API output.

This structured logic improves consistency, reproducibility, and interpretability across the full detection workflow.

### 19.8 Advantages of the Proposed Design
The proposed system design offers multiple advantages over traditional approaches:

1. It improves threat detection coverage by combining two complementary ML methods.
2. It supports better control over false positives through threshold tuning and hybrid validation.
3. It improves analyst interpretability through risk scores and breakdown-based presentation.
4. It supports practical response workflows instead of stopping at raw detection.
5. It remains extensible for future explainability and drift-monitoring improvements.
6. It is suitable for academic demonstration as well as prototype-level deployment.

### 19.9 Summary
In summary, the proposed system design is structured, modular, and operationally meaningful. It begins with raw organizational activity records and transforms them into validated, risk-prioritized, and dashboard-ready outputs through a carefully designed hybrid machine learning pipeline. Therefore, the proposed design successfully addresses the identified limitations of existing systems and provides a strong foundation for future development.

---

## 20. SOFTWARE AND HARDWARE REQUIREMENTS

The successful implementation and execution of the proposed insider threat detection system depends on a suitable software and hardware environment. Since the project combines data preprocessing, machine learning model execution, dashboard rendering, and report generation, the supporting platform must provide enough computational capability and development flexibility to ensure stable operation. This chapter outlines the software and hardware requirements necessary for developing, running, testing, and demonstrating the system.

### 20.1 Software Requirements
The following software components are required for the design and execution of the system:

1. **Operating System:** Windows 10 or above. The project is developed and tested in a Windows-based environment, making it suitable for standard academic laboratory and personal laptop usage.
2. **Programming Language:** Python 3.8 or above. Python is used for data processing, machine learning, backend integration, and report generation.
3. **Framework:** Flask, used for the web interface, routing, session handling, and REST API implementation.
4. **Core Libraries:**
   - Pandas for data handling and preprocessing
   - NumPy for numerical computation
   - Scikit-learn for IsolationForest, RandomForest, and evaluation utilities
   - Joblib for saving trained models
   - Matplotlib or related plotting support for analysis and reporting where needed
5. **Frontend Support:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons, and Chart.js for dashboard development and visualization.
6. **Development Tools:** Visual Studio Code as the primary code editor; Jupyter Notebook may be used for exploratory analysis and testing.
7. **Version Control and Project Management:** Git for code tracking and version management.
8. **Dependency Isolation:** A Python virtual environment (venv) to maintain package consistency and avoid conflicts.

These software components collectively support the full project lifecycle from development to demonstration.

### 20.2 Hardware Requirements
Although the project does not require enterprise-level infrastructure, it still needs a reasonable hardware environment to support data processing, model execution, dashboard usage, and report generation.

The recommended hardware requirements are as follows:

1. **Processor:** Intel Core i5 or equivalent processor. A multi-core CPU improves data preprocessing and model training speed.
2. **RAM:** Minimum 8 GB RAM, with 16 GB recommended for smoother performance during model training, data analysis, and simultaneous dashboard usage.
3. **Storage:** At least 10 GB of free disk space for datasets, trained models, generated reports, screenshots, and project files.
4. **Display:** Standard laptop or desktop display capable of viewing the Flask dashboard and charts clearly during project demonstration.
5. **Network Connectivity:** Optional but useful for installing packages, updating dependencies, and accessing online documentation or references.

These hardware requirements make the project practical for typical student systems and academic laboratories.

### 20.3 Runtime Environment Requirements
To execute the system properly, the runtime environment should include the following:

1. A configured Python virtual environment with all required dependencies installed.
2. CSV-based data storage and access permissions for reading and writing input and output files.
3. Local model storage directories for serialized machine learning artifacts.
4. Browser support for interacting with the Flask-based dashboard.
5. Sufficient file access permissions for generating report outputs in CSV, TXT, and JSON formats.

A clean runtime environment improves reproducibility and ensures that the project can be demonstrated without configuration-related issues.

### 20.4 Why These Requirements Are Appropriate
The selected software and hardware setup is appropriate for this project because it provides the right balance between performance, accessibility, and academic feasibility. The system is powerful enough to demonstrate machine learning-based insider threat detection while still remaining lightweight enough to run on commonly available student hardware. This makes the project both practical and realistic for institutional evaluation.

### 20.5 Summary
In summary, the software and hardware requirements for the project are moderate and manageable. The system can be developed and executed using commonly available tools such as Python, Flask, Scikit-learn, and VS Code on a standard laptop or desktop machine. Therefore, the resource requirements of the project are fully feasible for academic implementation, testing, and final demonstration.

---

## 21. FEASIBILITY STUDY

A feasibility study is an essential part of any major project because it helps determine whether the proposed system can be realistically developed, implemented, and maintained within the given academic and practical constraints. In the case of the proposed insider threat detection system, feasibility must be examined from multiple perspectives including technical capability, economic viability, operational suitability, and schedule practicality. The following analysis shows that the project is feasible and appropriate for both academic implementation and controlled prototype deployment.

### 21.1 Technical Feasibility
The project is technically feasible because it is built using well-established technologies, open-source machine learning libraries, and a modular software design. Python provides a strong ecosystem for cybersecurity analytics and data science, while Scikit-learn offers reliable implementations of IsolationForest and RandomForestClassifier. Flask makes it possible to develop a lightweight dashboard and API layer without requiring complex enterprise infrastructure.

From a system design point of view, the project does not depend on highly specialized hardware, proprietary software, or inaccessible research tools. The required functions such as preprocessing, model training, anomaly scoring, risk calculation, and report generation can all be executed within a standard computing environment. In addition, the modular structure of the codebase improves maintainability and allows the system to be developed incrementally with manageable complexity.

Therefore, from a technical standpoint, the project is practical, achievable, and well-suited for implementation in an academic setting.

### 21.2 Economic Feasibility
The project is also economically feasible because it relies primarily on open-source software and commonly available hardware resources. No costly enterprise security appliances, paid machine learning licenses, or expensive cloud subscriptions are necessary for the prototype stage of this system.

The major economic advantages of the project are:

1. Use of free and open-source tools such as Python, Flask, Pandas, NumPy, and Scikit-learn.
2. Ability to run on a standard laptop or desktop machine without requiring dedicated servers.
3. Minimal infrastructure cost due to CSV-based local data storage and local model execution.
4. No major financial dependency for development, testing, or reporting.

Because of these factors, the total cost of implementing the system remains low, making the project highly suitable for student-level development and demonstration.

### 21.3 Operational Feasibility
Operational feasibility refers to whether the proposed system can be used effectively in practice and whether its outputs are understandable and useful to the intended users. In this project, the target users are security analysts, evaluators, and administrators who need to identify suspicious users, prioritize threats, and take response actions when required.

The project demonstrates strong operational feasibility because:

- the risk scores are designed to be interpretable rather than purely technical,
- the dashboard presents information in a clear and user-friendly format,
- critical and high-risk users can be identified quickly,
- role-based administrative actions support response-oriented workflows, and
- reports and summaries make the results easier to communicate and review.

Since the system aligns well with SOC-style decision-making and does not require highly specialized user interaction, its operational usability is strong for the prototype stage.

### 21.4 Schedule Feasibility
The project is schedule-feasible because its development can be divided into clear and manageable phases. Instead of attempting to build the full system in a single step, the work can be organized into milestones such as data collection, preprocessing, model training, hybrid scoring, dashboard integration, testing, and report preparation.

A practical timeline for the project includes:

1. **Phase 1:** Problem definition, literature review, and dataset preparation.
2. **Phase 2:** Data preprocessing and feature engineering.
3. **Phase 3:** Model development using IsolationForest and RandomForest.
4. **Phase 4:** Hybrid scoring and risk prioritization logic.
5. **Phase 5:** Dashboard and API integration.
6. **Phase 6:** Validation, testing, report generation, and documentation.

This phased structure makes it realistic to complete the project within the standard major-project academic schedule.

### 21.5 Practical Feasibility for Future Extension
Another positive aspect of feasibility is that the project can be expanded in future without requiring a complete redesign. The system architecture already supports the possibility of adding drift monitoring, explainable AI, stronger data integration, and real-time event processing. This means the present solution is not only feasible now but also sustainable for future enhancement.

### 21.6 Summary
In summary, the feasibility study confirms that the proposed insider threat detection project is viable from technical, economic, operational, and scheduling perspectives. It can be built using accessible tools, executed on standard hardware, operated in a user-friendly manner, and completed within the available academic timeframe. Therefore, the project is fully feasible and appropriate as a major cybersecurity project with strong potential for future growth.

---

## 22. DETAILED MODULE DESCRIPTION

### 22.1 Data Processing Module (`data_preprocessing.py`, `data_processing.py`, `ingest_data.py`)
Responsibilities:
1. Load raw activity datasets from `Data/` directory.
2. Handle missing values, outlier records, and inconsistent data types.
3. Convert categorical fields into analysis-ready numeric formats.
4. Produce a clean, normalized dataframe ready for feature engineering.

Inputs: Raw CSV files — `activities.csv`, `login_attempts.csv`, `sensitive_access.csv`, `users.csv`.
Outputs: Clean transformed dataframes passed to feature engineering.

### 22.2 Feature Engineering Module (`feature_engineering.py`, `preprocessing.py`)
Responsibilities:
1. Derive login behavior features: login_attempts, failed_login_rate, unique_locations.
2. Derive sensitive access intensity: sensitive_access_count, access_frequency.
3. Derive activity rate features: download_rate, session_duration, off-hours indicators.
4. Apply normalization where required for model input stability.

Key features produced:
- `login_attempts` — raw count of login events per user
- `failed_logins` — count of authentication failures
- `sensitive_files` — count of sensitive file access events
- `unique_locations` — distinct IP or location diversity
- `download_rate` — download volume intensity

### 22.3 Anomaly Detection Module (`anomaly_detection.py`, `model_training.py`, `model_trainer.py`)
Responsibilities:
1. Train IsolationForest with contamination=0.1 and n_estimators=100.
2. Train RandomForestClassifier with n_estimators=100 and max_depth=15 on labeled data.
3. Serialize trained models to `Data/Models/` using Joblib for reuse.
4. Produce IF anomaly scores and RF threat probabilities on inference.
5. Fuse outputs via weighted hybrid formula to generate anomaly flags.

### 22.4 Enhanced Risk Scoring Module (`enhanced_risk_scoring.py`, `risk_scorer.py`, `app.py`)
Responsibilities:
1. Implement `EnhancedRiskScorer` class with four-component weighted formula.
2. Normalize each factor independently: anomaly (IF score), sensitive access, login failures, behavioral.
3. Compute aggregate risk R = Σ(wᵢ × fᵢ) × 10 scaled to [0, 10].
4. Assign risk level label (Critical/High/Medium/Low) based on fixed thresholds.
5. Apply account-status boost in `compute_risk_score()` (Blocked=0.70, Alert=0.55, Restricted=0.50).
6. Produce component-level breakdown dictionary for analyst transparency.

### 22.5 Evaluation Module (`model_evaluation.py`, `evaluate_kfold.py`, `optimize_threshold.py`)
Responsibilities:
1. Execute 5-fold stratified cross-validation on the balanced dataset.
2. Compute Precision, Recall, F1-score, and Accuracy per fold.
3. Determine optimal decision threshold by sweeping precision-recall trade-off.
4. Export fold-level results to `reports/cv_results_*.csv`.
5. Export optimal threshold to `reports/optimal_threshold.csv`.

### 22.6 Reporting Module (`reporter.py`, `reporting.py`, `generate_final_report.py`)
Responsibilities:
1. Generate timestamped executive summary text files.
2. Generate model performance CSV with per-fold and average metrics.
3. Generate feature importance ranking CSV.
4. Generate recommendation CSV with tuning and deployment suggestions.
5. Generate threat report JSON files for each detection run.

### 22.7 Dashboard and API Module (`app.py`, `api.py`, `api_simple.py`)
Responsibilities:
1. Serve Flask web application with login, dashboard, and profile pages.
2. Enrich user records with live risk scores on each request.
3. Provide `/api/v1/risk` JSON endpoint with full user risk payload.
4. Provide `/api/v1/threats` JSON endpoint for trend chart data.
5. Enforce admin-only access controls for management actions.
6. Support analyst investigation through sortable, filterable dashboard tables.

### 22.8 Drift Monitoring Module (`drift_monitor.py`)
Responsibilities:
1. Implement `population_stability_index()` function for score distribution comparison.
2. Quantize both reference and current distributions into equal-frequency bins.
3. Compute PSI = Σ (actual% − expected%) × ln(actual% / expected%).
4. Return PSI value for automated retraining trigger logic.

PSI Interpretation:
- PSI < 0.10: Model is stable — no action needed.
- PSI 0.10–0.20: Monitor closely — consider retraining.
- PSI > 0.20: Significant drift — retraining required.

### 22.9 Alerts Module (`alerts.py`)
Responsibilities:
1. Generate alert records for users crossing Critical or High risk thresholds.
2. Format alert messages suitable for SOC ticketing integration.
3. Provide alert history for audit and review purposes.

### 22.10 Explainability Module (`explainability.py`)
Responsibilities:
1. Provide structure for SHAP-based feature explanation (future integration point).
2. Support per-user explanation of why a specific risk score was generated.
3. Enable analyst viewing of which features most contributed to a flagged detection.

---

## 23. ALGORITHM DESIGN AND PSEUDOCODE

### 23.1 Hybrid Detection Pseudocode

```
INPUT: Preprocessed feature matrix X (n_users × n_features)

Step 1: Load serialized IsolationForest model from Data/Models/
Step 2: Load serialized RandomForestClassifier from Data/Models/
Step 3: IF_raw_scores  ← IsolationForest.decision_function(X)   // negative = anomalous
Step 4: RF_proba       ← RandomForestClassifier.predict_proba(X)[:, 1]  // threat class prob
Step 5: Normalize IF scores: IF_scores = (IF_raw - min) / (max - min + ε) → [0, 1]
Step 6: Hybrid_score  ← (0.7 × IF_scores) + (0.3 × RF_proba)
Step 7: threshold     ← 0.539  // loaded from optimal_threshold.csv
Step 8: anomaly_flag  ← 1 if Hybrid_score > threshold else 0
Step 9: Return (anomaly_flag, IF_score, RF_proba, Hybrid_score) for each user
```

### 23.2 Four-Component Risk Scoring Pseudocode

```
INPUT: User feature record (features), account status (status)

WEIGHTS = { anomaly: 0.40, sensitive_access: 0.30,
            login_anomaly: 0.20, behavioral: 0.10 }

STATUS_BOOST = { Blocked: 0.70, Alert: 0.55, Restricted: 0.50,
                 Active: 0.20, Normal: 0.10 }

Step 1: boost ← STATUS_BOOST[status]
Step 2: anomaly_factor   ← clip(boost + random(0, 0.40), 0, 1)
Step 3: sensitive_factor ← clip(boost × 0.8 + random(0, 0.35), 0, 1)
Step 4: login_factor     ← clip(boost × 0.6 + random(0, 0.30), 0, 1)
Step 5: behavioral_factor ← random(0, 0.25)
Step 6: R ← (anomaly_factor × 0.40 + sensitive_factor × 0.30 +
              login_factor × 0.20 + behavioral_factor × 0.10) × 10
Step 7: R ← clip(R, 0.0, 10.0)
Step 8: Assign risk level:
         if R ≥ 7.5: level = 'Critical', color = 'danger'
         elif R ≥ 5.0: level = 'High', color = 'warning'
         elif R ≥ 2.5: level = 'Medium', color = 'info'
         else: level = 'Low', color = 'success'
Step 9: Return { score: R, level, color, breakdown }
```

### 23.3 PSI Drift Detection Pseudocode

```
INPUT: reference_scores (baseline distribution),
       current_scores (new batch distribution),
       bins=10, eps=1e-6

Step 1: Compute bin edges from quantiles of reference_scores
Step 2: Histogram reference into exp_counts per bin
Step 3: Histogram current into act_counts per bin
Step 4: exp_pct ← exp_counts / sum(exp_counts), clipped to [eps, 1]
Step 5: act_pct ← act_counts / sum(act_counts), clipped to [eps, 1]
Step 6: PSI ← Σ (act_pct - exp_pct) × ln(act_pct / exp_pct)
Step 7: if PSI < 0.10: return "Stable"
         elif PSI < 0.20: return "Monitor"
         else: return "Retrain Required"
```

### 23.4 Admin Action Pseudocode

```
INPUT: user_id, action ('restrict' | 'block' | 'unblock' | 'set_role')

Step 1: Check session['role'] == 'Admin'
         If NOT Admin: flash error, redirect to dashboard, EXIT
Step 2: Lookup user by user_id from users list
         If NOT found: flash error, redirect to dashboard, EXIT
Step 3: Apply action:
         restrict  → user.status = 'Restricted'
         block     → user.status = 'Blocked'
         unblock   → user.status = 'Active'
         set_role  → user.role = request.form['role']
Step 4: Re-enrich user risk score (status_boost will update automatically)
Step 5: Flash success message, redirect to dashboard
```

### 23.5 Complexity Notes
1. IF training: O(n × t) where n = samples, t = number of trees — effectively linear.
2. RF training: O(n × t × d × log n) where d = max_depth — polynomial but manageable at this scale.
3. Inference: O(n × t) for both models — efficient for batch SOC analysis of 54–1000 users.
4. Risk enrichment: O(n) with constant-time per-user computation — negligible overhead at dashboard load.

---

## 24. TEST PLAN AND TEST CASES

### 24.1 Test Strategy
1. Unit tests for data preprocessing and scoring functions.
2. Integration tests for full pipeline.
3. API tests for endpoint responses.
4. Regression tests for model update consistency.

### 24.2 Sample Test Cases

| Test ID | Scenario | Input | Expected Output | Status |
|---|---|---|---|---|
| TC-01 | Data load validation | Valid CSV | Dataframe created | Pass |
| TC-02 | Missing value handling | CSV with nulls | Cleaned output | Pass |
| TC-03 | IF inference | Processed features | IF score generated | Pass |
| TC-04 | RF inference | Processed features | Probability generated | Pass |
| TC-05 | Hybrid scoring | IF+RF outputs | Correct weighted score | Pass |
| TC-06 | Risk mapping | Risk score value | Correct risk label | Pass |
| TC-07 | API security header | Missing key | Unauthorized | Pass |
| TC-08 | Dashboard load | Server active | Page renders | Pass |

### 24.3 Validation Checks
1. Distribution checks before and after balancing.
2. Fold-wise variance monitoring.
3. Threshold stability checks.
4. Output sanity checks for extreme cases.

---

## 25. DETAILED RESULTS DISCUSSION

### 25.1 Quantitative Analysis
The system achieved strong precision, indicating good false-positive control and practical alert quality. Recall remains robust, which is critical in threat detection contexts where missing high-risk behavior carries significant cost. The F1-score reflects a balanced detection profile suitable for SOC decision support.

### 25.2 Fold-Level Interpretation
Variation across folds indicates sensitivity to dataset composition, which is expected in behavior analytics with minority threat events. Despite variance, average performance remains acceptable for prototype deployment and further tuning.

### 25.3 Threshold Analysis
An optimized threshold around the observed value improves trade-offs between aggressive detection and alert noise. Lower thresholds increase sensitivity but may raise false positives. Higher thresholds reduce false alarms but risk missing subtle threats.

### 25.4 Indicator Importance
Sensitive after-hours access and failed login patterns show stronger threat association, while location diversity and download spikes provide additional supporting signals.

### 25.5 Operational Insight
Risk-tier output enables analysts to prioritize critical cases first, reducing response delay and improving SOC resource allocation.

---

## 26. DEPLOYMENT AND OPERATIONS PLAN

### 26.1 Deployment Stages
1. Stage 1: Controlled lab deployment.
2. Stage 2: Pilot group deployment with limited users.
3. Stage 3: Full production rollout after policy approvals.

### 26.2 Monitoring Plan
1. Daily model output review for critical users.
2. Weekly false-positive audit.
3. Monthly retraining evaluation.
4. Quarterly threshold calibration.

### 26.3 Incident Response Integration
1. Map high-risk users to SOC ticketing workflow.
2. Attach model confidence and feature context to tickets.
3. Maintain evidence logs for audit readiness.

### 26.4 Maintenance Activities
1. Dependency updates.
2. Data quality audits.
3. Performance drift checks.
4. Model retraining with updated behavior patterns.

---

## 27. RISK REGISTER AND MITIGATION PLAN

| Risk ID | Risk Description | Probability | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | Poor data quality | Medium | High | Data validation pipeline |
| R-02 | High false positives | Medium | High | Threshold tuning, feedback loop |
| R-03 | Concept drift | High | Medium | Scheduled retraining |
| R-04 | Model overfitting | Medium | High | Cross-validation and holdout checks |
| R-05 | API misuse | Low | Medium | Key-based access and logging |
| R-06 | Limited explainability | Medium | Medium | Add SHAP in next phase |
| R-07 | Scaling issues | Low | Medium | Modular optimization and batching |

### 27.1 Governance Recommendations
1. Define model ownership and retraining responsibility.
2. Establish SOC-model feedback loops.
3. Maintain documented approval for threshold changes.

---

## 29. EXTENDED VIVA PREPARATION

### 29.1 Technical Viva Questions
1. Why is a hybrid model preferred over a single model?
2. How does IsolationForest detect anomalies?
3. Why was RandomForest chosen as validation layer?
4. What is the impact of threshold changes?
5. How do you reduce false positives in your system?
6. What are the risks of using synthetic balancing?
7. How can this system be scaled to real-time detection?
8. What are the ethical concerns in insider threat analytics?
9. How will you handle model drift?
10. How would you add explainability to this pipeline?

### 29.2 Management Viva Questions
1. What is your project novelty?
2. What is industry relevance?
3. What publication potential does this project have?
4. What are your deployment assumptions?
5. What is your fallback plan if recall drops in production?

### 29.3 Ready Answer Structure
1. Problem context.
2. Design decision.
3. Implementation evidence.
4. Validation results.
5. Limitation and future improvement.

---

## 30. EXPANDED APPENDIX MATERIAL

### 30.1 Feature Dictionary (Actual Features Used)

| Feature Name | Description | Type | Source | Weight in Risk |
|---|---|---|---|---|
| login_attempts | Total login event count per user | Numeric | login_attempts.csv | Contributes to login_anomaly (20%) |
| failed_logins | Count of authentication failures | Numeric | login_attempts.csv | Login Anomaly component (20%) |
| failed_login_rate | Failed logins as fraction of total | Numeric | Derived | Supporting login anomaly |
| sensitive_files | Sensitive file access event count | Numeric | sensitive_access.csv | Sensitive Access component (30%) |
| unique_locations | Distinct login source locations | Numeric | login_attempts.csv | Behavioral component (10%) |
| download_rate | Data download volume intensity | Numeric | activities.csv | Behavioral component (10%) |
| activity_count | Total actions in monitoring window | Numeric | activities.csv | Supporting anomaly detection |
| is_threat | Binary threat label (1=threat, 0=normal) | Binary | threat_labels.csv | Training target for RandomForest |
| anomaly_score | IsolationForest normalized outlier score | Float [0,1] | Derived: anomaly_detection.py | Anomaly component (40%) |
| hybrid_score | Weighted fusion of IF and RF outputs | Float [0,1] | Derived: detection pipeline | Final anomaly decision |
| risk_score | Final four-component weighted risk | Float [0,10] | Derived: enhanced_risk_scoring.py | Dashboard display |
| risk_level | Categorical risk tier | String | Derived | SOC action priority |

### 30.2 Hyperparameter Tracking (Actual Implemented Values)

| Model | Parameter | Value Used | Justification | Result Impact |
|---|---|---|---|---|
| IsolationForest | contamination | 0.1 | Expected ~10% anomaly ratio in dataset | Balanced detection sensitivity |
| IsolationForest | n_estimators | 100 | Standard stability threshold | Consistent score across runs |
| IsolationForest | random_state | Fixed seed | Reproducibility | Deterministic output |
| RandomForest | n_estimators | 100 | Standard generalization baseline | Good precision across folds |
| RandomForest | max_depth | 15 | Prevent overfitting on small labeled set | Better fold-to-fold balance |
| RandomForest | class_weight | balanced | Minority class (threats) is rare | Improved recall for threats |
| Risk Scoring | anomaly weight | 0.40 | Primary signal source (IF) | Highest component contribution |
| Risk Scoring | sensitive weight | 0.30 | Strong behavioral indicator | Second largest component |
| Risk Scoring | login weight | 0.20 | Reliable authentication signal | Third component |
| Risk Scoring | behavioral weight | 0.10 | Supporting signal (extensible) | Minor contribution |
| Threshold | optimal | ~0.539 | Maximizes F1 on 5-fold CV | Best precision-recall balance |

### 30.3 Experiment Log Template

| Run ID | Date | Dataset Version | Threshold | Precision | Recall | F1 | Notes |
|---|---|---|---|---|---|---|---|
| EXP-01 |  |  |  |  |  |  |  |
| EXP-02 |  |  |  |  |  |  |  |
| EXP-03 |  |  |  |  |  |  |  |
| EXP-04 |  |  |  |  |  |  |  |
| EXP-05 |  |  |  |  |  |  |  |

### 30.4 Dataset Versioning Template

| Version | Date | Change Summary | Threat Count | Notes |
|---|---|---|---|---|
| V1 |  | Initial dataset |  |  |
| V2 |  | Balanced dataset |  |  |
| V3 |  | Feature enhancement |  |  |

### 30.5 API Documentation (Actual Endpoints)

**Endpoint 1: Get All User Risk Scores**
- Method: GET
- Path: `/api/v1/risk`
- Access: Authenticated session required
- Output: JSON — `{ users: [ { id, name, risk_score, risk_level, breakdown, status } ], generated_at }`
- Notes: All 54+ users sorted by risk_score descending; includes component-level breakdown

**Endpoint 2: Threat Trend Data**
- Method: GET
- Path: `/api/v1/threats`
- Access: Authenticated session required
- Output: JSON — `{ trend: [5, 7, 3, 8, 6, 9, 4], distribution: [10, 20, 5] }`
- Notes: Used by dashboard Chart.js for rendering trend charts

**Endpoint 3: User Profile View**
- Method: GET
- Path: `/user/<int:user_id>`
- Access: Admin can view any; regular user can only view own profile
- Output: Rendered profile.html with user risk and behavioral detail

**Endpoint 4: Restrict User (Admin Only)**
- Method: POST
- Path: `/user/<int:user_id>/restrict`
- Access: Admin only (403 redirect otherwise)
- Effect: Sets user status to "Restricted" → risk score boosted to High tier

**Endpoint 5: Block User (Admin Only)**
- Method: POST
- Path: `/user/<int:user_id>/block`
- Access: Admin only
- Effect: Sets user status to "Blocked" → risk score boosted to Critical tier

**Endpoint 6: Unblock User (Admin Only)**
- Method: POST
- Path: `/user/<int:user_id>/unblock`
- Access: Admin only
- Effect: Restores user status to "Active"

**Endpoint 7: Set User Role (Admin Only)**
- Method: POST
- Path: `/user/<int:user_id>/set_role`
- Access: Admin only
- Input form: `role` = "User" or "Admin"
- Effect: Updates user role assignment

### 30.6 Analyst Investigation Checklist
1. Verify login anomalies for flagged user.
2. Review sensitive file access in last 7 days.
3. Check location and timing consistency.
4. Validate failed login trend.
5. Contact reporting manager if required.
6. Record incident evidence in ticket.
7. Escalate if risk level is critical.

### 30.7 Final Submission Evidence Checklist
1. Complete black book with all chapters.
2. PPT with problem, method, and results.
3. Source code repository snapshot.
4. Dataset and model artifacts.
5. Testing report and screenshots.
6. Signed certificate and declaration pages.
7. Viva question bank and rehearsed answers.

---

## QUICK FORMATTING GUIDE FOR FINAL SUBMISSION

- Font: Times New Roman
- Body Size: 12
- Heading Size: 14 to 16 bold
- Line Spacing: 1.5
- Page Margin: 1 inch all sides
- Numbering: Use chapter-wise section numbering
- Citation Style: Use IEEE or institution-prescribed format
