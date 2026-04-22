# Insider Threat Detection System - SOC User Guide

This guide describes how to operate the current dashboard and demo workflow in this repository.

## Scope

The current system is a project prototype with:

- a Flask-based dashboard
- local demo authentication
- synthetic or demo-oriented activity generation
- 0-10 risk scoring
- admin actions for response simulation

It is not currently integrated with enterprise SSO, live SIEM ingestion, or an externally secured API gateway.

## Accessing The Dashboard

Start the app from the project root:

```powershell
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Demo Accounts

The primary demo accounts currently defined in the app are:

- Admin: `aayush` / `aayushadminpass`
- User: `amit` / `adminpass`
- User: `priya` / `analystpass`

Additional demo users are generated at runtime to populate the dashboard.

## Current Risk Model

The current dashboard computes risk from four weighted factors:

- Anomaly: 40%
- Sensitive access: 30%
- Login anomaly: 20%
- Behavioral signal: 10%

Risk is shown on a 0-10 scale.

## Risk Levels

The thresholds implemented in the Flask app are:

| Level | Score Range | Suggested Response |
|---|---|---|
| Critical | 7.5 to 10.0 | Immediate review and escalation |
| High | 5.0 to 7.4 | Prompt review |
| Medium | 2.5 to 4.9 | Monitor and trend |
| Low | 0.0 to 2.4 | Routine observation |

## Dashboard Sections

### Summary Cards

The top metrics provide:

- total users
- critical threats
- high-risk counts
- flagged activity counts

### Risk Distribution

The donut chart summarizes the user population by risk level.

### Top Risk Users

The leaderboard surfaces the users with the highest scores for quick triage.

### Recent User Activities

This section lists recent flagged and normal actions, ordered by risk score.

### User Management

When logged in as admin, you can:

- restrict a user
- block a user
- unblock a user
- change a user role

These controls are designed for demo and presentation workflows.

## Active API Endpoints

The current demo API surface is:

### Risk Data

```text
GET /api/v1/risk
```

Returns user risk score data, level, breakdown, and status.

### Threat Summary

```text
GET /api/v1/threats
```

Returns simplified trend and distribution data used by the demo.

There is no API-key enforcement in the current Flask implementation for these routes.

## Suggested Analyst Workflow

1. Log in to the dashboard.
2. Review Critical and High users first.
3. Inspect the recent activity table for the highest scoring entries.
4. If using the admin account, simulate containment with Restrict or Block.
5. Open the user profile page for a narrower per-user review.
6. Use generated files in the `reports` directory when you need supporting evidence for the presentation or written report.

## Important Limitations

- The dashboard uses demo users and generated activity, not live enterprise telemetry.
- Some scripts in the repository are experimental or legacy and should not all be treated as the main execution path.
- The web dashboard is currently the primary operator-facing surface for the repository.

## Troubleshooting

### Dashboard does not load

- confirm the application started successfully
- confirm port `5000` is available
- verify Flask is installed in the active environment

### Login fails

- confirm the username and password match one of the demo accounts above
- check for accidental whitespace

### Risk values change after user actions

- this is expected when a user status changes to values such as `Restricted` or `Blocked`
- the current app recalculates risk from user ID and status

## Support

Project contact:

- Aayush Salve
- Email: `aayushsalve15@gmail.com`
- Repository: https://github.com/aayushsalve/AI-based-Insider-threat-detection-system
