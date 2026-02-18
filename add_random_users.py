import pandas as pd
import random

# Path to your CSV file (edit if needed)
csv_path = r"reports\detailed_results_20260217_122948.csv"

# Load existing data to get columns
df = pd.read_csv(csv_path)

# How many new users to add
num_new = 1000

# Find the highest existing user number to avoid duplicates
existing_ids = set(df['user_id'].astype(str))
max_num = 0
for uid in existing_ids:
    if uid.startswith("USER_"):
        try:
            num = int(uid.split("_")[1])
            if num > max_num:
                max_num = num
        except ValueError:
            continue

# Generate new rows
new_rows = []
for i in range(1, num_new + 1):
    user_id = f"USER_{max_num + i:04d}"
    risk_score = round(random.uniform(1, 10), 2)
    risk_level = random.choices(
        ["Low", "Medium", "High", "Critical"],
        weights=[0.4, 0.3, 0.2, 0.1]
    )[0]
    confidence = round(random.uniform(10, 100), 2)
    anomaly_score = round(random.uniform(0, 1), 3)
    # Adjust this list to match your CSV columns!
    row = {
        "user_id": user_id,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "confidence": confidence,
        "anomaly_score": anomaly_score
    }
    # Fill in any other columns with 0 or default values
    for col in df.columns:
        if col not in row:
            row[col] = 0
    new_rows.append(row)

# Append to DataFrame and save
df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
df.to_csv(csv_path, index=False)

print(f"Added {num_new} new users to {csv_path}")

# Example: Get the top 10 users with the highest risk scores
limit = 10
top = df.sort_values('risk_score', ascending=False).head(limit)
print(top)
