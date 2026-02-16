import pandas as pd
import random
from datetime import datetime, timedelta


def generate_user_data(num_users, num_records_per_user):
    # Simulating different users
    user_ids = [f'U{i+1}' for i in range(num_users)]

    # Simulate random logins and file access data
    data = []

    for user in user_ids:
        for _ in range(num_records_per_user):
            # Random timestamp between now and 30 days ago
            timestamp = datetime.now() - timedelta(
                days=random.randint(0, 30), hours=random.randint(0, 24))

            # Simulate login hour (0 to 23 hours)
            login_hour = random.randint(0, 23)

            # Simulate file access count (0 to 20 files accessed per session)
            file_access_count = random.randint(0, 20)

            # Simulate sensitive file access (1 or 0)
            sensitive_file_access = random.randint(0, 1)

            # Create a record for this user
            record = [user, timestamp, login_hour, file_access_count,
                      sensitive_file_access]
            data.append(record)

    # Convert to DataFrame
    columns = ["user_id", "timestamp", "login_hour",
               "file_access_count", "sensitive_file_access"]
    df = pd.DataFrame(data, columns=columns)

    return df


def save_data_to_csv(df, filename="simulated_activity.csv"):
    # Save DataFrame to a CSV file
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


# Generate data for 10 users, each with 100 records
data = generate_user_data(num_users=10, num_records_per_user=100)

# Save the generated data to a CSV file
save_data_to_csv(data)
