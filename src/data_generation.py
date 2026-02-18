import pandas as pd
from datetime import datetime, timedelta
import random


def generate_user_data(num_users=100):
    """Generate synthetic user profiles"""
    departments = ["IT", "Finance", "HR", "Legal", "Operations", "Sales"]
    roles = ["Analyst", "Manager", "Director", "Engineer", "Specialist"]

    users = []
    for i in range(num_users):
        users.append({
            "user_id": f"USER_{i+1:04d}",
            "department": random.choice(departments),
            "role": random.choice(roles),
            "tenure_months": random.randint(1, 120)
        })
    return pd.DataFrame(users)


def generate_activity_data(num_users=100, num_records=5000):
    """Generate synthetic user activity logs"""
    activities = []
    start_date = datetime.now() - timedelta(days=90)

    for _ in range(num_records):
        user_id = f"USER_{random.randint(1, num_users):04d}"
        activity_date = start_date + timedelta(days=random.randint(0, 90))

        activities.append({
            "user_id": user_id,
            "timestamp": activity_date,
            "activity_type": random.choice(
                ["login", "file_access", "email_send", "data_download"]
            ),
            "resource": f"resource_{random.randint(1, 50)}",
            "status": random.choice(["success", "failed", "blocked"]),
            "data_volume_mb": round(random.uniform(0.1, 1000), 2)
        })
    return pd.DataFrame(activities)


def generate_sensitive_file_access(num_users=100, num_records=2000):
    """Generate sensitive file access patterns"""
    sensitive_files = [
        "payroll_data.xlsx",
        "employee_records.db",
        "financial_reports.pdf",
        "strategic_plans.docx",
        "customer_database.sql"
    ]

    access_logs = []
    start_date = datetime.now() - timedelta(days=90)

    for _ in range(num_records):
        user_id = f"USER_{random.randint(1, num_users):04d}"
        timestamp = start_date + timedelta(days=random.randint(0, 90))

        access_logs.append({
            "user_id": user_id,
            "timestamp": timestamp,
            "file_name": random.choice(sensitive_files),
            "action": random.choice(["read", "download", "copy", "email"]),
            "is_after_hours": random.choice([True, False]),
            "is_anomalous": random.choice([True, False])
        })
    return pd.DataFrame(access_logs)


def generate_login_attempts(num_users=100, num_records=1500):
    """Generate login attempt data"""
    login_data = []
    start_date = datetime.now() - timedelta(days=90)

    for _ in range(num_records):
        user_id = f"USER_{random.randint(1, num_users):04d}"
        timestamp = start_date + timedelta(days=random.randint(0, 90))

        source_ip = (
            f"{random.randint(1, 255)}.{random.randint(0, 255)}."
            f"{random.randint(0, 255)}.{random.randint(0, 255)}"
        )
        login_data.append({
            "user_id": user_id,
            "timestamp": timestamp,
            "source_ip": source_ip,
            "login_status": random.choice(["success", "failed"]),
            "failed_attempts": random.randint(0, 5),
            "location": random.choice(["Office", "Remote", "VPN"])
        })
    return pd.DataFrame(login_data)


def generate_insider_threat_labels(num_users=100, threat_percentage=0.10):
    """Generate labels indicating insider threat users"""
    threat_count = int(num_users * threat_percentage)
    threat_users = [
        f"USER_{random.randint(1, num_users):04d}"
        for _ in range(threat_count)
    ]
    threat_users = list(set(threat_users))

    labels = []
    for i in range(1, num_users + 1):
        user_id = f"USER_{i:04d}"
        labels.append({
            "user_id": user_id,
            "is_threat": 1 if user_id in threat_users else 0
        })
    return pd.DataFrame(labels)


def save_synthetic_data(output_dir="data"):
    """Generate and save all synthetic data"""
    import os
    os.makedirs(output_dir, exist_ok=True)

    print("Generating synthetic data...")
    users_df = generate_user_data(num_users=100)
    activities_df = generate_activity_data(
        num_users=100, num_records=5000
    )
    sensitive_df = generate_sensitive_file_access(
        num_users=100, num_records=2000
    )
    login_df = generate_login_attempts(
        num_users=100, num_records=1500
    )
    labels_df = generate_insider_threat_labels(
        num_users=100, threat_percentage=0.10
    )

    # Save to CSV
    users_df.to_csv(f"{output_dir}/users.csv", index=False)
    activities_df.to_csv(f"{output_dir}/activities.csv", index=False)
    sensitive_df.to_csv(f"{output_dir}/sensitive_access.csv", index=False)
    login_df.to_csv(f"{output_dir}/login_attempts.csv", index=False)
    labels_df.to_csv(f"{output_dir}/threat_labels.csv", index=False)

    print(f"✓ Data saved to {output_dir}/")
    print(f"  - users.csv: {len(users_df)} records")
    print(f"  - activities.csv: {len(activities_df)} records")
    print(f"  - sensitive_access.csv: {len(sensitive_df)} records")
    print(f"  - login_attempts.csv: {len(login_df)} records")
    print(f"  - threat_labels.csv: {len(labels_df)} records")


if __name__ == "__main__":
    save_synthetic_data()
