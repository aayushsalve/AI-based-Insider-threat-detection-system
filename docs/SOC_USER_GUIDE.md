# 🛡️ Insider Threat Detection System - SOC User Guide

## Overview
The Insider Threat Detection System (ITDS) is a real-time monitoring solution that identifies potential insider threats using machine learning and behavioral analysis.

**System Status:** ✅ Production Ready
**Model Accuracy:** 82% F1-Score | 88% Precision | 78% Recall

---

## Getting Started

### 1. Accessing the Dashboard
- **URL:** http://localhost:5000
- **Credentials:** Use your organization SSO
- **Availability:** 24/7

### 2. Dashboard Overview

#### Key Metrics
- **Critical Threats:** Users with risk score > 8.0
- **High Risk:** Users with risk score 6.0-8.0
- **Detection Rate:** % of users flagged as suspicious
- **Avg Risk Score:** System-wide average threat level

---

## Understanding Risk Levels

| Level | Score | Action Required |
|-------|-------|------------------|
| **CRITICAL** | 8.0-10.0 | Immediate investigation & escalation |
| **HIGH** | 6.0-7.9 | Investigation within 2 hours |
| **MEDIUM** | 4.0-5.9 | Monitor closely, review trends |
| **LOW** | 0-3.9 | Normal activity, routine monitoring |

---

## Top Anomaly Indicators (Priority Order)

1. **Sensitive After-Hours Access** (15.6% weight)
   - File access outside business hours
   - Action: Check if legitimate or concerning pattern

2. **Failed Login Rate** (12.4% weight)
   - Multiple failed authentication attempts
   - Action: Check for brute force or account compromise

3. **Unique Locations** (9.8% weight)
   - Logins from unexpected geographic locations
   - Action: Verify VPN usage or travel

4. **Download Rate** (8.7% weight)
   - Unusual volume of file downloads
   - Action: Review downloaded files for sensitivity

5. **Activity Frequency** (7.6% weight)
   - Unusually high activity volume
   - Action: Check for data exfiltration patterns

---

## API Endpoints for Integrations

### Authentication
All API calls require header:
```
X-API-Key: insider-threat-api-2026
```

### 1. Score Single User
```
POST /api/v1/score-user
Content-Type: application/json
X-API-Key: insider-threat-api-2026

{"user_id": "USER_0065"}

Response:
{
  "user_id": "USER_0065",
  "risk_score": 8.5,
  "risk_level": "CRITICAL",
  "confidence": 94.2
}
```

### 2. Get Critical Threats
```
GET /api/v1/critical-threats
X-API-Key: insider-threat-api-2026

Response:
{
  "threats": [
    {"user_id": "USER_0065", "risk_score": 8.5, "confidence": 94.2},
    {"user_id": "USER_0037", "risk_score": 8.2, "confidence": 89.1}
  ],
  "count": 15
}
```

### 3. Get User Profile
```
GET /api/v1/user/USER_0065/profile
X-API-Key: insider-threat-api-2026

Response includes detailed behavior metrics
```

---

## Alert Types & Response Procedures

### 🚨 CRITICAL ALERT
- **Trigger:** Risk score > 8.0
- **Response:** IMMEDIATE
  1. Lock user account (if necessary)
  2. Contact manager immediately
  3. Document in incident ticket
  4. Escalate to CISO

### ⚠️ HIGH ALERT
- **Trigger:** Risk score 6.0-8.0
- **Response:** Within 2 hours
  1. Review user activity logs
  2. Check with user's manager
  3. Monitor closely for trends
  4.  Document findings

### 📊 MEDIUM ALERT
- **Trigger:** Risk score 4.0-6.0
- **Response:** Within 24 hours
  1. Review trends over past week
  2. Check for pattern changes
  3. Flag for continued monitoring

---

## Investigation Checklist

When investigating a suspicious user:

- [ ] Review all file access in past 7 days
- [ ] Check login locations (map unusual IPs)
- [ ] Audit failed login attempts
- [ ] Verify any VPN/proxy usage
- [ ] Contact user's manager for context
- [ ] Check email forwarding rules
- [ ] Review recent privilege escalations
- [ ] Check calendar for travel/leave
- [ ] Document all findings
- [ ] Send formal inquiry if needed

---

## Common Scenarios

### Scenario 1: User on Business Trip
**Indicator:** Multiple unique locations
**Action:**
- Verify travel plans in calendar
- Check VPN usage for each location
- Mark as benign if legitimate
- Continue monitoring

### Scenario 2: New Employee
**Indicator:** High activity frequency initially
**Action:**
- Check training materials/onboarding
- Verify with manager
- Set expectations for learning curve
- Review after 30-day period

### Scenario 3: Late Night Work
**Indicator:** After-hours access
**Action:**
- Verify with manager if approved
- Check if regular pattern
- Review file sensitivity
- Accept if legitimate recurring pattern

---

## Reporting & Export

### Generate Threat Report
```
Dashboard → Reports → Threat Report
Format: PDF, CSV, JSON
```

### Schedule Periodic Reports
- Daily: Critical threats only
- Weekly: All threats with trends
- Monthly: Full system analysis

---

## Troubleshooting

### Dashboard Not Loading
- [ ] Check network connectivity
- [ ] Clear browser cache
- [ ] Check API server status

### API Connection Failed
- [ ] Verify API key is correct
- [ ] Check if API server is running
- [ ] Verify firewall rules

### Missing User Data
- [ ] Verify user exists in system
- [ ] Check if user has minimum activity
- [ ] Run data refresh cycle

---

## Contact & Support

- **System Issues:** security-team@company.com
- **Escalations:** ciso@company.com
- **On-Call SOC:** +1-XXX-XXX-XXXX

---

## System Performance

**Last Updated:** 2026-02-17
**Model Accuracy:** 82% F1-Score
**Avg Detection Time:** < 5 minutes
**False Positive Rate:** 12%

---

*For more information, contact the Security Operations team.*

---

# 🛡️ Insider Threat Detection System - SOC User Guide

## Overview
The Insider Threat Detection System (ITDS) is a real-time monitoring solution that identifies potential insider threats using machine learning and behavioral analysis.

**System Status:** ✅ Production Ready
**Model Accuracy:** 82% F1-Score | 88% Precision | 78% Recall

---

## Getting Started

### 1. Accessing the Dashboard
- **URL:** http://localhost:5000
- **Credentials:** Use your organization SSO
- **Availability:** 24/7

### 2. Dashboard Overview

#### Key Metrics
- **Critical Threats:** Users with risk score > 8.0
- **High Risk:** Users with risk score 6.0-8.0
- **Detection Rate:** % of users flagged as suspicious
- **Avg Risk Score:** System-wide average threat level

---

## Understanding Risk Levels

| Level | Score | Action Required |
|-------|-------|------------------|
| **CRITICAL** | 8.0-10.0 | Immediate investigation & escalation |
| **HIGH** | 6.0-7.9 | Investigation within 2 hours |
| **MEDIUM** | 4.0-5.9 | Monitor closely, review trends |
| **LOW** | 0-3.9 | Normal activity, routine monitoring |

---

## Top Anomaly Indicators (Priority Order)

1. **Sensitive After-Hours Access** (15.6% weight)
   - File access outside business hours
   - Action: Check if legitimate or concerning pattern

2. **Failed Login Rate** (12.4% weight)
   - Multiple failed authentication attempts
   - Action: Check for brute force or account compromise

3. **Unique Locations** (9.8% weight)
   - Logins from unexpected geographic locations
   - Action: Verify VPN usage or travel

4. **Download Rate** (8.7% weight)
   - Unusual volume of file downloads
   - Action: Review downloaded files for sensitivity

5. **Activity Frequency** (7.6% weight)
   - Unusually high activity volume
   - Action: Check for data exfiltration patterns

---

## API Endpoints for Integrations

### Authentication
All API calls require header:
```
X-API-Key: insider-threat-api-2026
```

### 1. Score Single User
```
POST /api/v1/score-user
Content-Type: application/json
X-API-Key: insider-threat-api-2026

{"user_id": "USER_0065"}

Response:
{
  "user_id": "USER_0065",
  "risk_score": 8.5,
  "risk_level": "CRITICAL",
  "confidence": 94.2
}
```

### 2. Get Critical Threats
```
GET /api/v1/critical-threats
X-API-Key: insider-threat-api-2026

Response:
{
  "threats": [
    {"user_id": "USER_0065", "risk_score": 8.5, "confidence": 94.2},
    {"user_id": "USER_0037", "risk_score": 8.2, "confidence": 89.1}
  ],
  "count": 15
}
```

### 3. Get User Profile
```
GET /api/v1/user/USER_0065/profile
X-API-Key: insider-threat-api-2026

Response includes detailed behavior metrics
```

---

## Alert Types & Response Procedures

### 🚨 CRITICAL ALERT
- **Trigger:** Risk score > 8.0
- **Response:** IMMEDIATE
  1. Lock user account (if necessary)
  2. Contact manager immediately
  3. Document in incident ticket
  4. Escalate to CISO

### ⚠️ HIGH ALERT
- **Trigger:** Risk score 6.0-8.0
- **Response:** Within 2 hours
  1. Review user activity logs
  2. Check with user's manager
  3. Monitor closely for trends
  4.  Document findings

### 📊 MEDIUM ALERT
- **Trigger:** Risk score 4.0-6.0
- **Response:** Within 24 hours
  1. Review trends over past week
  2. Check for pattern changes
  3. Flag for continued monitoring

---

## Investigation Checklist

When investigating a suspicious user:

- [ ] Review all file access in past 7 days
- [ ] Check login locations (map unusual IPs)
- [ ] Audit failed login attempts
- [ ] Verify any VPN/proxy usage
- [ ] Contact user's manager for context
- [ ] Check email forwarding rules
- [ ] Review recent privilege escalations
- [ ] Check calendar for travel/leave
- [ ] Document all findings
- [ ] Send formal inquiry if needed

---

## Common Scenarios

### Scenario 1: User on Business Trip
**Indicator:** Multiple unique locations
**Action:**
- Verify travel plans in calendar
- Check VPN usage for each location
- Mark as benign if legitimate
- Continue monitoring

### Scenario 2: New Employee
**Indicator:** High activity frequency initially
**Action:**
- Check training materials/onboarding
- Verify with manager
- Set expectations for learning curve
- Review after 30-day period

### Scenario 3: Late Night Work
**Indicator:** After-hours access
**Action:**
- Verify with manager if approved
- Check if regular pattern
- Review file sensitivity
- Accept if legitimate recurring pattern

---

## Reporting & Export

### Generate Threat Report
```
Dashboard → Reports → Threat Report
Format: PDF, CSV, JSON
```

### Schedule Periodic Reports
- Daily: Critical threats only
- Weekly: All threats with trends
- Monthly: Full system analysis

---

## Troubleshooting

### Dashboard Not Loading
- [ ] Check network connectivity
- [ ] Clear browser cache
- [ ] Check API server status

### API Connection Failed
- [ ] Verify API key is correct
- [ ] Check if API server is running
- [ ] Verify firewall rules

### Missing User Data
- [ ] Verify user exists in system
- [ ] Check if user has minimum activity
- [ ] Run data refresh cycle

---

## Contact & Support

- **System Issues:** security-team@company.com
- **Escalations:** ciso@company.com
- **On-Call SOC:** +1-XXX-XXX-XXXX

---

## System Performance

**Last Updated:** 2026-02-17
**Model Accuracy:** 82% F1-Score
**Avg Detection Time:** < 5 minutes
**False Positive Rate:** 12%

---

*For more information, contact the Security Operations team.*

---

# 🛡️ Insider Threat Detection System - SOC User Guide

## Overview
The Insider Threat Detection System (ITDS) is a real-time monitoring solution that identifies potential insider threats using machine learning and behavioral analysis.

**System Status:** ✅ Production Ready
**Model Accuracy:** 82% F1-Score | 88% Precision | 78% Recall

---

## Getting Started

### 1. Accessing the Dashboard
- **URL:** http://localhost:5000
- **Credentials:** Use your organization SSO
- **Availability:** 24/7

### 2. Dashboard Overview

#### Key Metrics
- **Critical Threats:** Users with risk score > 8.0
- **High Risk:** Users with risk score 6.0-8.0
- **Detection Rate:** % of users flagged as suspicious
- **Avg Risk Score:** System-wide average threat level

---

## Understanding Risk Levels

| Level | Score | Action Required |
|-------|-------|------------------|
| **CRITICAL** | 8.0-10.0 | Immediate investigation & escalation |
| **HIGH** | 6.0-7.9 | Investigation within 2 hours |
| **MEDIUM** | 4.0-5.9 | Monitor closely, review trends |
| **LOW** | 0-3.9 | Normal activity, routine monitoring |

---

## Top Anomaly Indicators (Priority Order)

1. **Sensitive After-Hours Access** (15.6% weight)
   - File access outside business hours
   - Action: Check if legitimate or concerning pattern

2. **Failed Login Rate** (12.4% weight)
   - Multiple failed authentication attempts
   - Action: Check for brute force or account compromise

3. **Unique Locations** (9.8% weight)
   - Logins from unexpected geographic locations
   - Action: Verify VPN usage or travel

4. **Download Rate** (8.7% weight)
   - Unusual volume of file downloads
   - Action: Review downloaded files for sensitivity

5. **Activity Frequency** (7.6% weight)
   - Unusually high activity volume
   - Action: Check for data exfiltration patterns

---

## API Endpoints for Integrations

### Authentication
All API calls require header:
```
X-API-Key: insider-threat-api-2026
```

### 1. Score Single User
```
POST /api/v1/score-user
Content-Type: application/json
X-API-Key: insider-threat-api-2026

{"user_id": "USER_0065"}

Response:
{
  "user_id": "USER_0065",
  "risk_score": 8.5,
  "risk_level": "CRITICAL",
  "confidence": 94.2
}
```

### 2. Get Critical Threats
```
GET /api/v1/critical-threats
X-API-Key: insider-threat-api-2026

Response:
{
  "threats": [
    {"user_id": "USER_0065", "risk_score": 8.5, "confidence": 94.2},
    {"user_id": "USER_0037", "risk_score": 8.2, "confidence": 89.1}
  ],
  "count": 15
}
```

### 3. Get User Profile
```
GET /api/v1/user/USER_0065/profile
X-API-Key: insider-threat-api-2026

Response includes detailed behavior metrics
```

---

## Alert Types & Response Procedures

### 🚨 CRITICAL ALERT
- **Trigger:** Risk score > 8.0
- **Response:** IMMEDIATE
  1. Lock user account (if necessary)
  2. Contact manager immediately
  3. Document in incident ticket
  4. Escalate to CISO

### ⚠️ HIGH ALERT
- **Trigger:** Risk score 6.0-8.0
- **Response:** Within 2 hours
  1. Review user activity logs
  2. Check with user's manager
  3. Monitor closely for trends
  4.  Document findings

### 📊 MEDIUM ALERT
- **Trigger:** Risk score 4.0-6.0
- **Response:** Within 24 hours
  1. Review trends over past week
  2. Check for pattern changes
  3. Flag for continued monitoring

---

## Investigation Checklist

When investigating a suspicious user:

- [ ] Review all file access in past 7 days
- [ ] Check login locations (map unusual IPs)
- [ ] Audit failed login attempts
- [ ] Verify any VPN/proxy usage
- [ ] Contact user's manager for context
- [ ] Check email forwarding rules
- [ ] Review recent privilege escalations
- [ ] Check calendar for travel/leave
- [ ] Document all findings
- [ ] Send formal inquiry if needed

---

## Common Scenarios

### Scenario 1: User on Business Trip
**Indicator:** Multiple unique locations
**Action:**
- Verify travel plans in calendar
- Check VPN usage for each location
- Mark as benign if legitimate
- Continue monitoring

### Scenario 2: New Employee
**Indicator:** High activity frequency initially
**Action:**
- Check training materials/onboarding
- Verify with manager
- Set expectations for learning curve
- Review after 30-day period

### Scenario 3: Late Night Work
**Indicator:** After-hours access
**Action:**
- Verify with manager if approved
- Check if regular pattern
- Review file sensitivity
- Accept if legitimate recurring pattern

---

## Reporting & Export

### Generate Threat Report
```
Dashboard → Reports → Threat Report
Format: PDF, CSV, JSON
```

### Schedule Periodic Reports
- Daily: Critical threats only
- Weekly: All threats with trends
- Monthly: Full system analysis

---

## Troubleshooting

### Dashboard Not Loading
- [ ] Check network connectivity
- [ ] Clear browser cache
- [ ] Check API server status

### API Connection Failed
- [ ] Verify API key is correct
- [ ] Check if API server is running
- [ ] Verify firewall rules

### Missing User Data
- [ ] Verify user exists in system
- [ ] Check if user has minimum activity
- [ ] Run data refresh cycle

---

## Contact & Support

- **System Issues:** security-team@company.com
- **Escalations:** ciso@company.com
- **On-Call SOC:** +1-XXX-XXX-XXXX

---

## System Performance

**Last Updated:** 2026-02-17
**Model Accuracy:** 82% F1-Score
**Avg Detection Time:** < 5 minutes
**False Positive Rate:** 12%

---

*For more information, contact the Security Operations team.*

---

# 🛡️ Insider Threat Detection System - SOC User Guide

## Overview
The Insider Threat Detection System (ITDS) is a real-time monitoring solution that identifies potential insider threats using machine learning and behavioral analysis.

**System Status:** ✅ Production Ready
**Model Accuracy:** 82% F1-Score | 88% Precision | 78% Recall

---

## Getting Started

### 1. Accessing the Dashboard
- **URL:** http://localhost:5000
- **Credentials:** Use your organization SSO
- **Availability:** 24/7

### 2. Dashboard Overview

#### Key Metrics
- **Critical Threats:** Users with risk score > 8.0
- **High Risk:** Users with risk score 6.0-8.0
- **Detection Rate:** % of users flagged as suspicious
- **Avg Risk Score:** System-wide average threat level

---

## Understanding Risk Levels

| Level | Score | Action Required |
|-------|-------|------------------|
| **CRITICAL** | 8.0-10.0 | Immediate investigation & escalation |
| **HIGH** | 6.0-7.9 | Investigation within 2 hours |
| **MEDIUM** | 4.0-5.9 | Monitor closely, review trends |
| **LOW** | 0-3.9 | Normal activity, routine monitoring |

---

## Top Anomaly Indicators (Priority Order)

1. **Sensitive After-Hours Access** (15.6% weight)
   - File access outside business hours
   - Action: Check if legitimate or concerning pattern

2. **Failed Login Rate** (12.4% weight)
   - Multiple failed authentication attempts
   - Action: Check for brute force or account compromise

3. **Unique Locations** (9.8% weight)
   - Logins from unexpected geographic locations
   - Action: Verify VPN usage or travel

4. **Download Rate** (8.7% weight)
   - Unusual volume of file downloads
   - Action: Review downloaded files for sensitivity

5. **Activity Frequency** (7.6% weight)
   - Unusually high activity volume
   - Action: Check for data exfiltration patterns

---

## API Endpoints for Integrations

### Authentication
All API calls require header:
```
X-API-Key: insider-threat-api-2026
```

### 1. Score Single User
```
POST /api/v1/score-user
Content-Type: application/json
X-API-Key: insider-threat-api-2026

{"user_id": "USER_0065"}

Response:
{
  "user_id": "USER_0065",
  "risk_score": 8.5,
  "risk_level": "CRITICAL",
  "confidence": 94.2
}
```

### 2. Get Critical Threats
```
GET /api/v1/critical-threats
X-API-Key: insider-threat-api-2026

Response:
{
  "threats": [
    {"user_id": "USER_0065", "risk_score": 8.5, "confidence": 94.2},
    {"user_id": "USER_0037", "risk_score": 8.2, "confidence": 89.1}
  ],
  "count": 15
}
```

### 3. Get User Profile
```
GET /api/v1/user/USER_0065/profile
X-API-Key: insider-threat-api-2026

Response includes detailed behavior metrics
```

---

## Alert Types & Response Procedures

### 🚨 CRITICAL ALERT
- **Trigger:** Risk score > 8.0
- **Response:** IMMEDIATE
  1. Lock user account (if necessary)
  2. Contact manager immediately
  3. Document in incident ticket
  4. Escalate to CISO

### ⚠️ HIGH ALERT
- **Trigger:** Risk score 6.0-8.0
- **Response:** Within 2 hours
  1. Review user activity logs
  2. Check with user's manager
  3. Monitor closely for trends
  4.  Document findings

### 📊 MEDIUM ALERT
- **Trigger:** Risk score 4.0-6.0
- **Response:** Within 24 hours
  1. Review trends over past week
  2. Check for pattern changes
  3. Flag for continued monitoring

---

## Investigation Checklist

When investigating a suspicious user:

- [ ] Review all file access in past 7 days
- [ ] Check login locations (map unusual IPs)
- [ ] Audit failed login attempts
- [ ] Verify any VPN/proxy usage
- [ ] Contact user's manager for context
- [ ] Check email forwarding rules
- [ ] Review recent privilege escalations
- [ ] Check calendar for travel/leave
- [ ] Document all findings
- [ ] Send formal inquiry if needed

---

## Common Scenarios

### Scenario 1: User on Business Trip
**Indicator:** Multiple unique locations
**Action:**
- Verify travel plans in calendar
- Check VPN usage for each location
- Mark as benign if legitimate
- Continue monitoring

### Scenario 2: New Employee
**Indicator:** High activity frequency initially
**Action:**
- Check training materials/onboarding
- Verify with manager
- Set expectations for learning curve
- Review after 30-day period

### Scenario 3: Late Night Work
**Indicator:** After-hours access
**Action:**
- Verify with manager if approved
- Check if regular pattern
- Review file sensitivity
- Accept if legitimate recurring pattern

---

## Reporting & Export

### Generate Threat Report
```
Dashboard → Reports → Threat Report
Format: PDF, CSV, JSON
```

### Schedule Periodic Reports
- Daily: Critical threats only
- Weekly: All threats with trends
- Monthly: Full system analysis

---

## Troubleshooting

### Dashboard Not Loading
- [ ] Check network connectivity
- [ ] Clear browser cache
- [ ] Check API server status

### API Connection Failed
- [ ] Verify API key is correct
- [ ] Check if API server is running
- [ ] Verify firewall rules

### Missing User Data
- [ ] Verify user exists in system
- [ ] Check if user has minimum activity
- [ ] Run data refresh cycle

---

## Contact & Support

- **System Issues:** security-team@company.com
- **Escalations:** ciso@company.com
- **On-Call SOC:** +1-XXX-XXX-XXXX

---

## System Performance

**Last Updated:** 2026-02-17
**Model Accuracy:** 82% F1-Score
**Avg Detection Time:** < 5 minutes
**False Positive Rate:** 12%

---

*For more information, contact the Security Operations team.*

---

# 🛡️ Insider Threat Detection System - SOC User Guide

## Overview
The Insider Threat Detection System (ITDS) is a real-time monitoring solution that identifies potential insider threats using machine learning and behavioral analysis.

**System Status:** ✅ Production Ready
**Model Accuracy:** 82% F1-Score | 88% Precision | 78% Recall

---

## Getting Started

### 1. Accessing the Dashboard
- **URL:** http://localhost:5000
- **Credentials:** Use your organization SSO
- **Availability:** 24/7

### 2. Dashboard Overview

#### Key Metrics
- **Critical Threats:** Users with risk score > 8.0
- **High Risk:** Users with risk score 6.0-8.0
- **Detection Rate:** % of users flagged as suspicious
- **Avg Risk Score:** System-wide average threat level

---

## Understanding Risk Levels

| Level | Score | Action Required |
|-------|-------|------------------|
| **CRITICAL** | 8.0-10.0 | Immediate investigation & escalation |
| **HIGH** | 6.0-7.9 | Investigation within 2 hours |
| **MEDIUM** | 4.0-5.9 | Monitor closely, review trends |
| **LOW** | 0-3.9 | Normal activity, routine monitoring |

---

## Top Anomaly Indicators (Priority Order)

1. **Sensitive After-Hours Access** (15.6% weight)
   - File access outside business hours
   - Action: Check if legitimate or concerning pattern

2. **Failed Login Rate** (12.4% weight)
   - Multiple failed authentication attempts
   - Action: Check for brute force or account compromise

3. **Unique Locations** (9.8% weight)
   - Logins from unexpected geographic locations
   - Action: Verify VPN usage or travel

4. **Download Rate** (8.7% weight)
   - Unusual volume of file downloads
   - Action: Review downloaded files for sensitivity

5. **Activity Frequency** (7.6% weight)
   - Unusually high activity volume
   - Action: Check for data exfiltration patterns

---

## API Endpoints for Integrations

### Authentication
All API calls require header:
```
X-API-Key: insider-threat-api-2026
```

### 1. Score Single User
```
POST /api/v1/score-user
Content-Type: application/json
X-API-Key: insider-threat-api-2026

{"user_id": "USER_0065"}

Response:
{
  "user_id": "USER_0065",
  "risk_score": 8.5,
  "risk_level": "CRITICAL",
  "confidence": 94.2
}
```

### 2. Get Critical Threats
```
GET /api/v1/critical-threats
X-API-Key: insider-threat-api-2026

Response:
{
  "threats": [
    {"user_id": "USER_0065", "risk_score": 8.5, "confidence": 94.2},
    {"user_id": "USER_0037", "risk_score": 8.2, "confidence": 89.1}
  ],
  "count": 15
}
```

### 3. Get User Profile
```
GET /api/v1/user/USER_0065/profile
X-API-Key: insider-threat-api-2026

Response includes detailed behavior metrics
```

---

## Alert Types & Response Procedures

### 🚨 CRITICAL ALERT
- **Trigger:** Risk score > 8.0
- **Response:** IMMEDIATE
  1. Lock user account (if necessary)
  2. Contact manager immediately
  3. Document in incident ticket
  4. Escalate to CISO

### ⚠️ HIGH ALERT
- **Trigger:** Risk score 6.0-8.0
- **Response:** Within 2 hours
  1. Review user activity logs
  2. Check with user's manager
  3. Monitor closely for trends
  4.  Document findings

### 📊 MEDIUM ALERT
- **Trigger:** Risk score 4.0-6.0
- **Response:** Within 24 hours
  1. Review trends over past week
  2. Check for pattern changes
  3. Flag for continued monitoring

---

## Investigation Checklist

When investigating a suspicious user:

- [ ] Review all file access in past 7 days
- [ ] Check login locations (map unusual IPs)
- [ ] Audit failed login attempts
- [ ] Verify any VPN/proxy usage
- [ ] Contact user's manager for context
- [ ] Check email forwarding rules
- [ ] Review recent privilege escalations
- [ ] Check calendar for travel/leave
- [ ] Document all findings
- [ ] Send formal inquiry if needed

---

## Common Scenarios

### Scenario 1: User on Business Trip
**Indicator:** Multiple unique locations
**Action:**
- Verify travel plans in calendar
- Check VPN usage for each location
- Mark as benign if legitimate
- Continue monitoring

### Scenario 2: New Employee
**Indicator:** High activity frequency initially
**Action:**
- Check training materials/onboarding
- Verify with manager
- Set expectations for learning curve
- Review after 30-day period

### Scenario 3: Late Night Work
**Indicator:** After-hours access
**Action:**
- Verify with manager if approved
- Check if regular pattern
- Review file sensitivity
- Accept if legitimate recurring pattern

---

## Reporting & Export

### Generate Threat Report
```
Dashboard → Reports → Threat Report
Format: PDF, CSV, JSON
```

### Schedule Periodic Reports
- Daily: Critical threats only
- Weekly: All threats with trends
- Monthly: Full system analysis

---

## Troubleshooting

### Dashboard Not Loading
- [ ] Check network connectivity
- [ ] Clear browser cache
- [ ] Check API server status

### API Connection Failed
- [ ] Verify API key is correct
- [ ] Check if API server is running
- [ ] Verify firewall rules

### Missing User Data
- [ ] Verify user exists in system
- [ ] Check if user has minimum activity
- [ ] Run data refresh cycle

---

## Contact & Support

- **System Issues:** security-team@company.com
- **Escalations:** ciso@company.com
- **On-Call SOC:** +1-XXX-XXX-XXXX

---

## System Performance

**Last Updated:** 2026-02-17
**Model Accuracy:** 82% F1-Score
**Avg Detection Time:** < 5 minutes
**False Positive Rate:** 12%

---

*For more information, contact the Security Operations team.*

---

# 🛡️ Insider Threat Detection System - SOC User Guide

## Overview
The Insider Threat Detection System (ITDS) is a real-time monitoring solution that identifies potential insider threats using machine learning and behavioral analysis.

**System Status:** ✅ Production Ready
**Model Accuracy:** 82% F1-Score | 88% Precision | 78% Recall

---

## Getting Started

### 1. Accessing the Dashboard
- **URL:** http://localhost:5000
- **Credentials:** Use your organization SSO
- **Availability:** 24/7

### 2. Dashboard Overview

#### Key Metrics
- **Critical Threats:** Users with risk score > 8.0
- **High Risk:** Users with risk score 6.0-8.0
- **Detection Rate:** % of users flagged as suspicious
- **Avg Risk Score:** System-wide average threat level

---

## Understanding Risk Levels

| Level | Score | Action Required |
|-------|-------|------------------|
| **CRITICAL** | 8.0-10.0 | Immediate investigation & escalation |
| **HIGH** | 6.0-7.9 | Investigation within 2 hours |
| **MEDIUM** | 4.0-5.9 | Monitor closely, review trends |
| **LOW** | 0-3.9 | Normal activity, routine monitoring |

---

## Top Anomaly Indicators (Priority Order)

1. **Sensitive After-Hours Access** (15.6% weight)
   - File access outside business hours
   - Action: Check if legitimate or concerning pattern

2. **Failed Login Rate** (12.4% weight)
   - Multiple failed authentication attempts
   - Action: Check for brute force or account compromise

3. **Unique Locations** (9.8% weight)
   - Logins from unexpected geographic locations
   - Action: Verify VPN usage or travel

4. **Download Rate** (8.7% weight)
   - Unusual volume of file downloads
   - Action: Review downloaded files for sensitivity

5. **Activity Frequency** (7.6% weight)
   - Unusually high activity volume
   - Action: Check for data exfiltration patterns

---

## API Endpoints for Integrations

### Authentication
All API calls require header:
```
X-API-Key: insider-threat-api-2026
```

### 1. Score Single User
```
POST /api/v1/score-user
Content-Type: application/json
X-API-Key: insider-threat-api-2026

{"user_id": "USER_0065"}

Response:
{
  "user_id": "USER_0065",
  "risk_score": 8.5,
  "risk_level": "CRITICAL",
  "confidence": 94.2
}
```

### 2. Get Critical Threats
```
GET /api/v1/critical-threats
X-API-Key: insider-threat-api-2026

Response:
{
  "threats": [
    {"user_id": "USER_0065", "risk_score": 8.5, "confidence": 94.2},
    {"user_id": "USER_0037", "risk_score": 8.2, "confidence": 89.1}
  ],
  "count": 15
}
```

### 3. Get User Profile
```
GET /api/v1/user/USER_0065/profile
X-API-Key: insider-threat-api-2026

Response includes detailed behavior metrics
```

---

## Alert Types & Response Procedures

### 🚨 CRITICAL ALERT
- **Trigger:** Risk score > 8.0
- **Response:** IMMEDIATE
  1. Lock user account (if necessary)
  2. Contact manager immediately
  3. Document in incident ticket
  4. Escalate to CISO

### ⚠️ HIGH ALERT
- **Trigger:** Risk score 6.0-8.0
- **Response:** Within 2 hours
  1. Review user activity logs
  2. Check with user's manager
  3. Monitor closely for trends
  4.  Document findings

### 📊 MEDIUM ALERT
- **Trigger:** Risk score 4.0-6.0
- **Response:** Within 24 hours
  1. Review trends over past week
  2. Check for pattern changes
  3. Flag for continued monitoring

---

## Investigation Checklist

When investigating a suspicious user:

- [ ] Review all file access in past 7 days
- [ ] Check login locations (map unusual IPs)
- [ ] Audit failed login attempts
- [ ] Verify any VPN/proxy usage
- [ ] Contact user's manager for context
- [ ] Check email forwarding rules
- [ ] Review recent privilege escalations
- [ ] Check calendar for travel/leave
- [ ] Document all findings
- [ ] Send formal inquiry if needed

---

## Common Scenarios

### Scenario 1: User on Business Trip
**Indicator:** Multiple unique locations
**Action:**
- Verify travel plans in calendar
- Check VPN usage for each location
- Mark as benign if legitimate
- Continue monitoring

### Scenario 2: New Employee
**Indicator:** High activity frequency initially
**Action:**
- Check training materials/onboarding
- Verify with manager
- Set expectations for learning curve
- Review after 30-day period

### Scenario 3: Late Night Work
**Indicator:** After-hours access
**Action:**
- Verify with manager if approved
- Check if regular pattern
- Review file sensitivity
- Accept if legitimate recurring pattern

---

## Reporting & Export

### Generate Threat Report
```
Dashboard → Reports → Threat Report
Format: PDF, CSV, JSON
```

### Schedule Periodic Reports
- Daily: Critical threats only
- Weekly: All threats with trends
- Monthly: Full system analysis

---

## Troubleshooting

### Dashboard Not Loading
- [ ] Check network connectivity
- [ ] Clear browser cache
- [ ] Check API server status

### API Connection Failed
- [ ] Verify API key is correct
- [ ] Check if API server is running
- [ ] Verify firewall rules

### Missing User Data
- [ ] Verify user exists in system
- [ ] Check if user has minimum activity
- [ ] Run data refresh cycle

---

## Contact & Support

- **System Issues:** security-team@company.com
- **Escalations:** ciso@company.com
- **On-Call SOC:** +1-XXX-XXX-XXXX

---

## System Performance

**Last Updated:** 2026-02-17
**Model Accuracy:** 82% F1-Score
**Avg Detection Time:** < 5 minutes
**False Positive Rate:** 12%

---

*For more information, contact the Security Operations team.*

---

# 🛡️ Insider Threat Detection System - SOC User Guide

## Overview
The Insider Threat Detection System (ITDS) is a real-time monitoring solution that identifies potential insider threats using machine learning and behavioral analysis.

**System Status:** ✅ Production Ready
**Model Accuracy:** 82% F1-Score | 88% Precision | 78% Recall

---

## Getting Started

### 1. Accessing the Dashboard
- **URL:** http://localhost:5000
- **Credentials:** Use your organization SSO
- **Availability:** 24/7

### 2. Dashboard Overview

#### Key Metrics
- **Critical Threats:** Users with risk score > 8.0
- **High Risk:** Users with risk score 6.0-8.0
- **Detection Rate:** % of users flagged as suspicious
- **Avg Risk Score:** System-wide average threat level

---

## Understanding Risk Levels

| Level | Score | Action Required |
|-------|-------|------------------|
| **CRITICAL** | 8.0-10.0 | Immediate investigation & escalation |
| **HIGH** | 6.0-7.9 | Investigation within 2 hours |
| **MEDIUM** | 4.0-5.9 | Monitor closely, review trends |
| **LOW** | 0-3.9 | Normal activity, routine monitoring |

---

## Top Anomaly Indicators (Priority Order)

1. **Sensitive After-Hours Access** (15.6% weight)
   - File access outside business hours
   - Action: Check if legitimate or concerning pattern

2. **Failed Login Rate** (12.4% weight)
   - Multiple failed authentication attempts
   - Action: Check for brute force or account compromise

3. **Unique Locations** (9.8% weight)
   - Logins from unexpected geographic locations
   - Action: Verify VPN usage or travel

4. **Download Rate** (8.7% weight)
   - Unusual volume of file downloads
   - Action: Review downloaded files for sensitivity

5. **Activity Frequency** (7.6% weight)
   - Unusually high activity volume
   - Action: Check for data exfiltration patterns

---

## API Endpoints for Integrations

### Authentication
All API calls require header:
```
X-API-Key: insider-threat-api-2026
```

### 1. Score Single User
```
POST /api/v1/score-user
Content-Type: application/json
X-API-Key: insider-threat-api-2026

{"user_id": "USER_0065"}

Response:
{
  "user_id": "USER_0065",
  "risk_score": 8.5,
  "risk_level": "CRITICAL",
  "confidence": 94.2
}
```

### 2. Get Critical Threats
```
GET /api/v1/critical-threats
X-API-Key: insider-threat-api-2026

Response:
{
  "threats": [
    {"user_id": "USER_0065", "risk_score": 8.5, "confidence": 94.2},
    {"user_id": "USER_0037", "risk_score": 8.2, "confidence": 89.1}
  ],
  "count": 15
}
```

### 3. Get User Profile
```
GET /api/v1/user/USER_0065/profile
X-API-Key: insider-threat-api-2026

Response includes detailed behavior metrics
```

---

## Alert Types & Response Procedures

### 🚨 CRITICAL ALERT
- **Trigger:** Risk score > 8.0
- **Response:** IMMEDIATE
  1. Lock user account (if necessary)
  2. Contact manager immediately
  3. Document in incident ticket
  4. Escalate to CISO

### ⚠️ HIGH ALERT
- **Trigger:** Risk score 6.0-8.0
- **Response:** Within 2 hours
  1. Review user activity logs
  2. Check with user's manager
  3. Monitor closely for trends
  4.  Document findings

### 📊 MEDIUM ALERT
- **Trigger:** Risk score 4.0-6.0
- **Response:** Within 24 hours
  1. Review trends over past week
  2. Check for pattern changes
  3. Flag for continued monitoring

---

## Investigation Checklist

When investigating a suspicious user:

- [ ] Review all file access in past 7 days
- [ ] Check login locations (map unusual IPs)
- [ ] Audit failed login attempts
- [ ] Verify any VPN/proxy usage
- [ ] Contact user's manager for context
- [ ] Check email forwarding rules
- [ ] Review recent privilege escalations
- [ ] Check calendar for travel/leave
- [ ] Document all findings
- [ ] Send formal inquiry if needed

---

## Common Scenarios

### Scenario 1: User on Business Trip
**Indicator:** Multiple unique locations
**Action:**
- Verify travel plans in calendar
- Check VPN usage for each location
- Mark as benign if legitimate
- Continue monitoring

### Scenario 2: New Employee
**Indicator:** High activity frequency initially
**Action:**
- Check training materials/onboarding
- Verify with manager
- Set expectations for learning curve
- Review after 30-day period

### Scenario 3: Late Night Work
**Indicator:** After-hours access
**Action:**
- Verify with manager if approved
- Check if regular pattern
- Review file sensitivity
- Accept if legitimate recurring pattern

---

## Reporting & Export

### Generate Threat Report
```
Dashboard → Reports → Threat Report
Format: PDF, CSV, JSON
```

### Schedule Periodic Reports
- Daily: Critical threats only
- Weekly: All threats with trends
- Monthly: Full system analysis

---

## Troubleshooting

### Dashboard Not Loading
- [ ] Check network connectivity
- [ ] Clear browser cache
- [ ] Check API server status

### API Connection Failed
- [ ] Verify API key is correct
- [ ] Check if API server is running
- [ ] Verify firewall rules

### Missing User Data
- [ ] Verify user exists in system
- [ ] Check if user has minimum activity
- [ ] Run data refresh cycle

---

## Contact & Support

- **System Issues:** security-team@company.com
- **Escalations:** ciso@company.com
- **On-Call SOC:** +1-XXX-XXX-XXXX

---

## System Performance

**Last Updated:** 2026-02-17
**Model Accuracy:** 82% F1-Score
**Avg Detection Time:** < 5 minutes
**False Positive Rate:** 12%

---

*For more information, contact the Security Operations team.*

---

# 🛡️ Insider Threat Detection System - SOC User Guide

## Overview
The Insider Threat Detection System (ITDS) is a real-time monitoring solution that identifies potential insider threats using machine learning and behavioral analysis.

**System Status:** ✅ Production Ready
**Model Accuracy:** 82% F1-Score | 88% Precision | 78% Recall

---

## Getting Started

### 1. Accessing the Dashboard
- **URL:** http://localhost:5000
- **Credentials:** Use your organization SSO
- **Availability:** 24/7

### 2. Dashboard Overview

#### Key Metrics
- **Critical Threats:** Users with risk score > 8.0
- **High Risk:** Users with risk score 6.0-8.0
- **Detection Rate:** % of users flagged as suspicious
- **Avg Risk Score:** System-wide average threat level

---

## Understanding Risk Levels

| Level | Score | Action Required |
|-------|-------|------------------|
| **CRITICAL** | 8.0-10.0 | Immediate investigation & escalation |
| **HIGH** | 6.0-7.9 | Investigation within 2 hours |
| **MEDIUM** | 4.0-5.9 | Monitor closely, review trends |
| **LOW** | 0-3.9 | Normal activity, routine monitoring |

---

## Top Anomaly Indicators (Priority Order)

1. **Sensitive After-Hours Access** (15.6% weight)
   - File access outside business hours
   - Action: Check if legitimate or concerning pattern

2. **Failed Login Rate** (12.4% weight)
   - Multiple failed authentication attempts
   - Action: Check for brute force or account compromise

3. **Unique Locations** (9.8% weight)
   - Logins from unexpected geographic locations
   - Action: Verify VPN usage or travel

4. **Download Rate** (8.7% weight)
   - Unusual volume of file downloads
   - Action: Review downloaded files for sensitivity

5. **Activity Frequency** (7.6% weight)
   - Unusually high activity volume
   - Action: Check for data exfiltration patterns

---

## API Endpoints for Integrations

### Authentication
All API calls require header:
```
X-API-Key: insider-threat-api-2026
```

### 1. Score Single User
```
POST /api/v1/score-user
Content-Type: application/json
X-API-Key: insider-threat-api-2026

{"user_id": "USER_0065"}

Response:
{
  "user_id": "USER_0065",
  "risk_score": 8.5,
  "risk_level": "CRITICAL",
  "confidence": 94.2
}
```

### 2. Get Critical Threats
```
GET /api/v1/critical-threats
X-API-Key: insider-threat-api-2026

Response:
{
  "threats": [
    {"user_id": "USER_0065", "risk_score": 8.5, "confidence": 94.2},
    {"user_id": "USER_0037", "risk_score": 8.2, "confidence": 89.1}
  ],
  "count": 15
}
```

### 3. Get User Profile
```
GET /api/v1/user/USER_0065/profile
X-API-Key: insider-threat-api-2026

Response includes detailed behavior metrics
```

---

## Alert Types & Response Procedures

### 🚨 CRITICAL ALERT
- **Trigger:** Risk score > 8.0
- **Response:** IMMEDIATE
  1. Lock user account (if necessary)
  2. Contact manager immediately
  3. Document in incident ticket
  4. Escalate to CISO

### ⚠️ HIGH ALERT
- **Trigger:** Risk score 6.0-8.0
- **Response:** Within 2 hours
  1. Review user activity logs
  2. Check with user's manager
  3. Monitor closely for trends
  4.  Document findings

### 📊 MEDIUM ALERT
- **Trigger:** Risk score 4.0-6.0
- **Response:** Within 24 hours
  1. Review trends over past week
  2. Check for pattern changes
  3. Flag for continued monitoring

---

## Investigation Checklist

When investigating a suspicious user:

- [ ] Review all file access in past 7 days
- [ ] Check login locations (map unusual IPs)
- [ ] Audit failed login attempts
- [ ] Verify any VPN/proxy usage
- [ ] Contact user's manager for context
- [ ] Check email forwarding rules
- [ ] Review recent privilege escalations
- [ ] Check calendar for travel/leave
- [ ] Document all findings
- [ ] Send formal inquiry if needed

---

## Common Scenarios

### Scenario 1: User on Business Trip
**Indicator:** Multiple unique locations
**Action:**
- Verify travel plans in calendar
- Check VPN usage for each location
- Mark as benign if legitimate
- Continue monitoring

### Scenario 2: New Employee
**Indicator:** High activity frequency initially
**Action:**
- Check training materials/onboarding
- Verify with manager
- Set expectations for learning curve
- Review after 30-day period

### Scenario 3: Late Night Work
**Indicator:** After-hours access
**Action:**
- Verify with manager if approved
- Check if regular pattern
- Review file sensitivity
- Accept if legitimate recurring pattern

---

## Reporting & Export

### Generate Threat Report
```
Dashboard → Reports → Threat Report
Format: PDF, CSV, JSON
```

### Schedule Periodic Reports
- Daily: Critical threats only
- Weekly: All threats with trends
- Monthly: Full system analysis

---

## Troubleshooting

### Dashboard Not Loading
- [ ] Check network connectivity
- [ ] Clear browser cache
- [ ] Check API server status

### API Connection Failed
- [ ] Verify API key is correct
- [ ] Check if API server is running
- [ ] Verify firewall rules

### Missing User Data
- [ ] Verify user exists in system
- [ ] Check if user has minimum activity
- [ ] Run data refresh cycle

---

## Contact & Support

- **System Issues:** security-team@company.com
- **Escalations:** ciso@company.com
- **On-Call SOC:** +1-XXX-XXX-XXXX

---

## System Performance

**Last Updated:** 2026-02-17
**Model Accuracy:** 82% F1-Score
**Avg Detection Time:** < 5 minutes
**False Positive Rate:** 12%

---

*For more information, contact the Security Operations team.*

---

# 🛡️ Insider Threat Detection System - SOC User Guide

## Overview
The Insider Threat Detection System (ITDS) is a real-time monitoring solution that identifies potential insider threats using machine learning and behavioral analysis.

**System Status:** ✅ Production Ready
**Model Accuracy:** 82% F1-Score | 88% Precision | 78% Recall

---

## Getting Started

### 1. Accessing the Dashboard
- **URL:** http://localhost:5000
- **Credentials:** Use your organization SSO
- **Availability:** 24/7

### 2. Dashboard Overview

#### Key Metrics
- **Critical Threats:** Users with risk score > 8.0
- **High Risk:** Users with risk score 6.0-8.0
- **Detection Rate:** % of users flagged as suspicious
- **Avg Risk Score:** System-wide average threat level

---

## Understanding Risk Levels

| Level | Score | Action Required |
|-------|-------|------------------|
| **CRITICAL** | 8.0-10.0 | Immediate investigation & escalation |
| **HIGH** | 6.0-7.9 | Investigation within 2 hours |
| **MEDIUM** | 4.0-5.9 | Monitor closely, review trends |
| **LOW** | 0-3.9 | Normal activity, routine monitoring |

---

## Top Anomaly Indicators (Priority Order)

1. **Sensitive After-Hours Access** (15.6% weight)
   - File access outside business hours
   - Action: Check if legitimate or concerning pattern

2. **Failed Login Rate** (12.4% weight)
   - Multiple failed authentication attempts
   - Action: Check for brute force or account compromise

3. **Unique Locations** (9.8% weight)
   - Logins from unexpected geographic locations
   - Action: Verify VPN usage or travel

4. **Download Rate** (8.7% weight)
   - Unusual volume of file downloads
   - Action: Review downloaded files for sensitivity

5. **Activity Frequency** (7.6% weight)
   - Unusually high activity volume
   - Action: Check for data exfiltration patterns

---

## API Endpoints for Integrations

### Authentication
All API calls require header:
```
X-API-Key: insider-threat-api-2026
```

### 1. Score Single User
```
POST /api/v1/score-user
Content-Type: application/json
X-API-Key: insider-threat-api-2026

{"user_id": "USER_0065"}

Response:
{
  "user_id": "USER_0065",
  "risk_score": 8.5,
  "risk_level": "CRITICAL",
  "confidence": 94.2
}
```

### 2. Get Critical Threats
```
GET /api/v1/critical-threats
X-API-Key: insider-threat-api-2026

Response:
{
  "threats": [
    {"user_id": "USER_0065", "risk_score": 8.5, "confidence": 94.2},
    {"user_id": "USER_0037", "risk_score": 8.2, "confidence": 89.1}
  ],
  "count": 15
}
```

### 3. Get User Profile
```
GET /api/v1/user/USER_0065/profile
X-API-Key: insider-threat-api-2026

Response includes detailed behavior metrics
```

---

## Alert Types & Response Procedures

### 🚨 CRITICAL ALERT
- **Trigger:** Risk score > 8.0
- **Response:** IMMEDIATE
  1. Lock user account (if necessary)
  2. Contact manager immediately
  3. Document in incident ticket
  4. Escalate to CISO

### ⚠️ HIGH ALERT
- **Trigger:** Risk score 6.0-8.0
- **Response:** Within 2 hours
  1. Review user activity logs
  2. Check with user's manager
  3. Monitor closely for trends
  4.  Document findings

### 📊 MEDIUM ALERT
- **Trigger:** Risk score 4.0-6.0
- **Response:** Within 24 hours
  1. Review trends over past week
  2. Check for pattern changes
  3. Flag for continued monitoring

---

## Investigation Checklist

When investigating a suspicious user:

- [ ] Review all file access in past 7 days
- [ ] Check login locations (map unusual IPs)
- [ ] Audit failed login attempts
- [ ] Verify any VPN/proxy usage
- [ ] Contact user's manager for context
- [ ] Check email forwarding rules
- [ ] Review recent privilege escalations
- [ ] Check calendar for travel/leave
- [ ] Document all findings
- [ ] Send formal inquiry if needed

---

## Common Scenarios

### Scenario 1: User on Business Trip
**Indicator:** Multiple unique locations
**Action:**
- Verify travel plans in calendar
- Check VPN usage for each location
- Mark as benign if legitimate
- Continue monitoring

### Scenario 2: New Employee
**Indicator:** High activity frequency initially
**Action:**
- Check training materials/onboarding
- Verify with manager
- Set expectations for learning curve
- Review after 30-day period

### Scenario 3: Late Night Work
**Indicator:** After-hours access
**Action:**
- Verify with manager if approved
- Check if regular pattern
- Review file sensitivity
- Accept if legitimate recurring pattern

---

## Reporting & Export

### Generate Threat Report
```
Dashboard → Reports → Threat Report
Format: PDF, CSV, JSON
```

### Schedule Periodic Reports
- Daily: Critical threats only
- Weekly: All threats with trends
- Monthly: Full system analysis

---

## Troubleshooting

### Dashboard Not Loading
- [ ] Check network connectivity
- [ ] Clear browser cache
- [ ] Check API server status

### API Connection Failed
- [ ] Verify API key is correct
- [ ] Check if API server is running
- [ ] Verify firewall rules

### Missing User Data
- [ ] Verify user exists in system
- [ ] Check if user has minimum activity
- [ ] Run data refresh cycle

---

## Contact & Support

- **System Issues:** security-team@company.com
- **Escalations:** ciso@company.com
- **On-Call SOC:** +1-XXX-XXX-XXXX

---

## System Performance

**Last Updated:** 2026-02-17
**Model Accuracy:** 82% F1-Score
**Avg Detection Time:** < 5 minutes
**False Positive Rate:** 12%

---

*For more information, contact the Security Operations team.*

---

# 🛡️ Insider Threat Detection System - SOC User Guide

## Overview
The Insider Threat Detection System (ITDS) is a real-time monitoring solution that identifies potential insider threats using machine learning and behavioral analysis.

**System Status:** ✅ Production Ready
**Model Accuracy:** 82% F1-Score | 88% Precision | 78% Recall

---

## Getting Started

### 1. Accessing the Dashboard
- **URL:** http://localhost:5000
- **Credentials:** Use your organization SSO
- **Availability:** 24/7

### 2. Dashboard Overview

#### Key Metrics
- **Critical Threats:** Users with risk score > 8.0
- **High Risk:** Users with risk score 6.0-8.0
- **Detection Rate:** % of users flagged as suspicious
- **Avg Risk Score:** System-wide average threat level

---

## Understanding Risk Levels

| Level | Score | Action Required |
|-------|-------|------------------|
| **CRITICAL** | 8.0-10.0 | Immediate investigation & escalation |
| **HIGH** | 6.0-7.9 | Investigation within 2 hours |
| **MEDIUM** | 4.0-5.9 | Monitor closely, review trends |
| **LOW** | 0-3.9 | Normal activity, routine monitoring |

---

## Top Anomaly Indicators (Priority Order)

1. **Sensitive After-Hours Access** (15.6% weight)
   - File access outside business hours
   - Action: Check if legitimate or concerning pattern

2. **Failed Login Rate** (12.4% weight)
   - Multiple failed authentication attempts
   - Action: Check for brute force or account compromise

3. **Unique Locations** (9.8% weight)
   - Logins from unexpected geographic locations
   - Action: Verify VPN usage or travel

4. **Download Rate** (8.7% weight)
   - Unusual volume of file downloads
   - Action: Review downloaded files for sensitivity

5. **Activity Frequency** (7.6% weight)
   - Unusually high activity volume
   - Action: Check for data exfiltration patterns

---

## API Endpoints for Integrations

### Authentication
All API calls require header:
```
X-API-Key: insider-threat-api-2026
```

### 1. Score Single User
```
POST /api/v1/score-user
Content-Type: application/json
X-API-Key: insider-threat-api-2026

{"user_id": "USER_0065"}

Response:
{
  "user_id": "USER_0065",
  "risk_score": 8.5,
  "risk_level": "CRITICAL",
  "confidence": 94.2
}
```

### 2. Get Critical Threats
```
GET /api/v1/critical-threats
X-API-Key: insider-threat-api-2026

Response:
{
  "threats": [
    {"user_id": "USER_0065", "risk_score": 8.5, "confidence": 94.2},
    {"user_id": "USER_0037", "risk_score": 8.2, "confidence": 89.1}
  ],
  "count": 15
}
```

### 3. Get User Profile
```
GET /api/v1/user/USER_0065/profile
X-API-Key: insider-threat-api-2026

Response includes detailed behavior metrics
```

---

## Alert Types & Response Procedures

### 🚨 CRITICAL ALERT
- **Trigger:** Risk score > 8.0
- **Response:** IMMEDIATE
  1. Lock user account (if necessary)
  2. Contact manager immediately
  3. Document in incident ticket
  4. Escalate to CISO

### ⚠️ HIGH ALERT
- **Trigger:** Risk score 6.0-8.0
- **Response:** Within 2 hours
  1. Review user activity logs
  2. Check with user's manager
  3. Monitor closely for trends
  4.  Document findings

### 📊 MEDIUM ALERT
- **Trigger:** Risk score 4.0-6.0
- **Response:** Within 24 hours
  1. Review trends over past week
  2. Check for pattern changes
  3. Flag for continued monitoring

---

## Investigation Checklist

When investigating a suspicious user:

- [ ] Review all file access in past 7 days
- [ ] Check login locations (map unusual IPs)
- [ ] Audit failed login attempts
- [ ] Verify any VPN/proxy usage
- [ ] Contact user's manager for context
- [ ] Check email forwarding rules
- [ ] Review recent privilege escalations
- [ ] Check calendar for travel/leave
- [ ] Document all findings
- [ ] Send formal inquiry if needed

---

## Common Scenarios

### Scenario 1: User on Business Trip
**Indicator:** Multiple unique locations
**Action:**
- Verify travel plans in calendar
- Check VPN usage for each location
- Mark as benign if legitimate
- Continue monitoring

### Scenario 2: New Employee
**Indicator:** High activity frequency initially
**Action:**
- Check training materials/onboarding
- Verify with manager
- Set expectations for learning curve
- Review after 30-day period

### Scenario 3: Late Night Work
**Indicator:** After-hours access
**Action:**
- Verify with manager if approved
- Check if regular pattern
- Review file sensitivity
- Accept if legitimate recurring pattern

---

## Reporting & Export

### Generate Threat Report
```
Dashboard → Reports → Threat Report
Format: PDF, CSV, JSON
```

### Schedule Periodic Reports
- Daily: Critical threats only
- Weekly: All threats with trends
- Monthly: Full system analysis

---

## Troubleshooting

### Dashboard Not Loading
- [ ] Check network connectivity
- [ ] Clear browser cache
- [ ] Check API server status

### API Connection Failed
- [ ] Verify API key is correct
- [ ] Check if API server is running
- [ ] Verify firewall rules

### Missing User Data
- [ ] Verify user exists in system
- [ ] Check if user has minimum activity
- [ ] Run data refresh cycle

---

## Contact & Support

- **System Issues:** security-team@company.com
- **Escalations:** ciso@company.com
- **On-Call SOC:** +1-XXX-XXX-XXXX

---

## System Performance

**Last Updated:** 2026-02-17
**Model Accuracy:** 82% F1-Score
**Avg Detection Time:** < 5 minutes
**False Positive Rate:** 12%

---

*For more information, contact the Security Operations team.*

---

# 🛡️ Insider Threat Detection System - SOC User Guide

## Overview
The Insider Threat Detection System (ITDS) is a real-time monitoring solution that identifies potential insider threats using machine learning and behavioral analysis.

**System Status:** ✅ Production Ready
**Model Accuracy:** 82% F1-Score | 88% Precision | 78% Recall

---

## Getting Started

### 1. Accessing the Dashboard
- **URL:** http://localhost:5000
- **Credentials:** Use your organization SSO
- **Availability:** 24/7

### 2. Dashboard Overview

#### Key Metrics
- **Critical Threats:** Users with risk score > 8.0
- **High Risk:** Users with risk score 6.0-8.0
- **Detection Rate:** % of users flagged as suspicious
- **Avg Risk Score:** System-wide average threat level

---

## Understanding Risk Levels

| Level | Score | Action Required |
|-------|-------|------------------|
| **CRITICAL** | 8.0-10.0 | Immediate investigation & escalation |
| **HIGH** | 6.0-7.9 | Investigation within 2 hours |
| **MEDIUM** | 4.0-5.9 | Monitor closely, review trends |
| **LOW** | 0-3.9 | Normal activity, routine monitoring |

---

## Top Anomaly Indicators (Priority Order)

1. **Sensitive After-Hours Access** (15.6% weight)
   - File access outside business hours
   - Action: Check if legitimate or concerning pattern

2. **Failed Login Rate** (12.4% weight)
   - Multiple failed authentication attempts
   - Action: Check for brute force or account compromise

3. **Unique Locations** (9.8% weight)
   - Logins from unexpected geographic locations
   - Action: Verify VPN usage or travel

4. **Download Rate** (8.7% weight)
   - Unusual volume of file downloads
   - Action: Review downloaded files for sensitivity

5. **Activity Frequency** (7.6% weight)
   - Unusually high activity volume
   - Action: Check for data exfiltration patterns

---

## API Endpoints for Integrations

### Authentication
All API calls require header:
```
X-API-Key: insider-threat-api-2026
```

### 1. Score Single User
```
POST /api/v1/score-user
Content-Type: application/json
X-API-Key: insider-threat-api-2026

{"user_id": "USER_0065"}

Response:
{
  "user_id": "USER_0065",
  "risk_score": 8.5,
  "risk_level": "CRITICAL",
  "confidence": 94.2
}
```

### 2. Get Critical Threats
```
GET /api/v1/critical-threats
X-API-Key: insider-threat-api-2026

Response:
{
  "threats": [
    {"user_id": "USER_0065", "risk_score": 8.5, "confidence": 94.2},
    {"user_id": "USER_0037", "risk_score": 8.2, "confidence": 89.1}
  ],
  "count": 15
}
```

### 3. Get User Profile
```
GET /api/v1/user/USER_0065/profile
X-API-Key: insider-threat-api-2026

Response includes detailed behavior metrics
```

---

## Alert Types & Response Procedures

### 🚨 CRITICAL ALERT
- **Trigger:** Risk score > 8.0
- **Response:** IMMEDIATE
  1. Lock user account (if necessary)
  2. Contact manager immediately
  3. Document in incident ticket
  4. Escalate to CISO

### ⚠️ HIGH ALERT
- **Trigger:** Risk score 6.0-8.0
- **Response:** Within 2 hours
  1. Review user activity logs
  2. Check with user's manager
  3. Monitor closely for trends
  4.  Document findings

### 📊 MEDIUM ALERT
- **Trigger:** Risk score 4.0-6.0
- **Response:** Within 24 hours
  1. Review trends over past week
  2. Check for pattern changes
  3. Flag for continued monitoring

---

## Investigation Checklist

When investigating a suspicious user:

- [ ] Review all file access in past 7 days
- [ ] Check login locations (map unusual IPs)
- [ ] Audit failed login attempts
- [ ] Verify any VPN/proxy usage
- [ ] Contact user's manager for context
- [ ] Check email forwarding rules
- [ ] Review recent privilege escalations
- [ ] Check calendar for travel/leave
- [ ] Document all findings
- [ ] Send formal inquiry if needed

---

## Common Scenarios

### Scenario 1: User on Business Trip
**Indicator:** Multiple unique locations
**Action:**
- Verify travel plans in calendar
- Check VPN usage for each location
- Mark as benign if legitimate
- Continue monitoring

### Scenario 2: New Employee
**Indicator:** High activity frequency initially
**Action:**
- Check training materials/onboarding
- Verify with manager
- Set expectations for learning curve
- Review after 30-day period

### Scenario 3: Late Night Work
**Indicator:** After-hours access
**Action:**
- Verify with manager if approved
- Check if regular pattern
- Review file sensitivity
- Accept if legitimate recurring pattern

---

## Reporting & Export

### Generate Threat Report
```
Dashboard → Reports → Threat Report
Format: PDF, CSV, JSON
```

### Schedule Periodic Reports
- Daily: Critical threats only
- Weekly: All threats with trends
- Monthly: Full system analysis

---

## Troubleshooting

### Dashboard Not Loading
- [ ] Check network connectivity
- [ ] Clear browser cache
- [ ] Check API server status

### API Connection Failed
- [ ] Verify API key is correct
- [ ] Check if API server is running
- [ ] Verify firewall rules

### Missing User Data
- [ ] Verify user exists in system
- [ ] Check if user has minimum activity
- [ ] Run data refresh cycle

---

## Contact & Support

- **System Issues:** security-team@company.com
- **Escalations:** ciso@company.com
- **On-Call SOC:** +1-XXX-XXX-XXXX

---

## System Performance

**Last Updated:** 2026-02-17
**Model Accuracy:** 82% F1-Score
**Avg Detection Time:** < 5 minutes
**False Positive Rate:** 12%

---

*For more information, contact the Security Operations team.*

---

# 🛡️ Insider Threat Detection System - SOC User Guide

## Overview
The Insider Threat Detection System (ITDS) is a real-time monitoring solution that identifies potential insider threats using machine learning and behavioral analysis.

**System Status:** ✅ Production Ready
**Model Accuracy:** 82% F1-Score | 88% Precision | 78% Recall

---

## Getting Started

### 1. Accessing the Dashboard
- **URL:** http://localhost:5000
- **Credentials:** Use your organization SSO
- **Availability:** 24/7

### 2. Dashboard Overview

#### Key Metrics
- **Critical Threats:** Users with risk score > 8.0
- **High Risk:** Users with risk score 6.0-8.0
- **Detection Rate:** % of users flagged as suspicious
- **Avg Risk Score:** System-wide average threat level

---

## Understanding Risk Levels

| Level | Score | Action Required |
|-------|-------|------------------|
| **CRITICAL** | 8.0-10.0 | Immediate investigation & escalation |
| **HIGH** | 6.0-7.9 | Investigation within 2 hours |
| **MEDIUM** | 4.0-5.9 | Monitor closely, review trends |
| **LOW** | 0-3.9 | Normal activity, routine monitoring |

---

## Top Anomaly Indicators (Priority Order)

1. **Sensitive After-Hours Access** (15.6% weight)
   - File access outside business hours
   - Action: Check if legitimate or concerning pattern

2. **Failed Login Rate** (12.4% weight)
   - Multiple failed authentication attempts
   - Action: Check for brute force or account compromise

3. **Unique Locations** (9.8% weight)
   - Logins from unexpected geographic locations
   - Action: Verify VPN usage or travel

4. **Download Rate** (8.7% weight)
   - Unusual volume of file downloads
   - Action: Review downloaded files for sensitivity

5. **Activity Frequency** (7.6% weight)
   - Unusually high activity volume
   - Action: Check for data exfiltration patterns

---

## API Endpoints for Integrations

### Authentication
All API calls require header:
```
X-API-Key: insider-threat-api-2026
```

### 1. Score Single User
```
POST /api/v1/score-user
Content-Type: application/json
X-API-Key: insider-threat-api-2026

{"user_id": "USER_0065"}

Response:
{
  "user_id": "USER_0065",
  "risk_score": 8.5,
  "risk_level": "CRITICAL",
  "confidence": 94.2
}
```

### 2. Get Critical Threats
```
GET /api/v1/critical-threats
X-API-Key: insider-threat-api-2026

Response:
{
  "threats": [
    {"user_id": "USER_0065", "risk_score": 8.5, "confidence": 94.2},
    {"user_id": "USER_0037", "risk_score": 8.2, "confidence": 89.1}
  ],
  "count": 15
}
```

### 3. Get User Profile
```
GET /api/v1/user/USER_0065/profile
X-API-Key: insider-threat-api-2026

Response includes detailed behavior metrics
```

---

## Alert Types & Response Procedures

### 🚨 CRITICAL ALERT
- **Trigger:** Risk score > 8.0
- **Response:** IMMEDIATE
  1. Lock user account (if necessary)
  2. Contact manager immediately
  3. Document in incident ticket
  4. Escalate to CISO

### ⚠️ HIGH ALERT
- **Trigger:** Risk score 6.0-8.0
- **Response:** Within 2 hours
  1. Review user activity logs
  2. Check with user's manager
  3. Monitor closely for trends
  4.  Document findings

### 📊 MEDIUM ALERT
- **Trigger:** Risk score 4.0-6.0
- **Response:** Within 24 hours
  1. Review trends over past week
  2. Check for pattern changes
  3. Flag for continued monitoring

---

## Investigation Checklist

When investigating a suspicious user:

- [ ] Review all file access in past 7 days
- [ ] Check login locations (map unusual IPs)
- [ ] Audit failed login attempts
- [ ] Verify any VPN/proxy usage
- [ ] Contact user's manager for context
- [ ] Check email forwarding rules
- [ ] Review recent privilege escalations
- [ ] Check calendar for travel/leave
- [ ] Document all findings
- [ ] Send formal inquiry if needed

---

## Common Scenarios

### Scenario 1: User on Business Trip
**Indicator:** Multiple unique locations
**Action:**
- Verify travel plans in calendar
- Check VPN usage for each location
- Mark as benign if legitimate
- Continue monitoring

### Scenario 2: New Employee
**Indicator:** High activity frequency initially
**Action:**
- Check training materials/onboarding
- Verify with manager
- Set expectations for learning curve
- Review after 30-day period

### Scenario 3: Late Night Work
**Indicator:** After-hours access
**Action:**
- Verify with manager if approved
- Check if regular pattern
- Review file sensitivity
- Accept if legitimate recurring pattern

---

## Reporting & Export

### Generate Threat Report
```
Dashboard → Reports → Threat Report
Format: PDF, CSV, JSON
```

### Schedule Periodic Reports
- Daily: Critical threats only
- Weekly: All threats with trends
- Monthly: Full system analysis

---

## Troubleshooting
