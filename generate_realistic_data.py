import pandas as pd
import random

num_users = 1000
output_path = (
    r"D:\Major Project\Insider Threat Detection\reports"
    r"\detailed_results_20260217_122948.csv"
)

risk_levels = ["Low", "Medium", "High", "Critical"]

rows = []
for i in range(1, num_users + 1):
    user_id = f"USER_{i:04d}"
    risk_score = round(random.uniform(1, 10), 2)
    # Assign risk_level based on risk_score
    if risk_score >= 8:
        risk_level = "Critical"
    elif risk_score >= 6:
        risk_level = "High"
    elif risk_score >= 4:
        risk_level = "Medium"
    else:
        risk_level = "Low"
    confidence = round(random.uniform(40, 100), 2)
    anomaly_score = round(random.uniform(0, 1), 3)
    total_activities = random.randint(50, 500)
    failed_activities = random.randint(0, 20)
    downloads_count = random.randint(0, 50)
    sensitive_files_accessed = random.randint(0, 10)
    after_hours_access = random.randint(0, 15)
    unique_locations = random.randint(1, 5)
    # Add a timestamp for timeline chart (optional)
    base_date = pd.Timestamp('2026-02-18')
    days_offset = pd.to_timedelta(random.randint(0, 30), unit='D')
    timestamp = base_date + days_offset
    rows.append({
        "user_id": user_id,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "confidence": confidence,
        "anomaly_score": anomaly_score,
        "total_activities": total_activities,
        "failed_activities": failed_activities,
        "downloads_count": downloads_count,
        "sensitive_files_accessed": sensitive_files_accessed,
        "after_hours_access": after_hours_access,
        "unique_locations": unique_locations,
        "timestamp": timestamp
    })

df = pd.DataFrame(rows)
df.to_csv(output_path, index=False)
print(f"Generated {num_users} users in {output_path}")
