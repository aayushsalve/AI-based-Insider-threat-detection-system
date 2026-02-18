import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(42)
data = {
    'login_attempts': np.random.randint(1, 50, 100),
    'files_accessed': np.random.randint(0, 200, 100),
    'data_uploaded': np.random.randint(0, 500, 100),
    'failed_logins': np.random.randint(0, 10, 100),
    'after_hours_activity': np.random.randint(0, 1, 100),
}

df = pd.DataFrame(data)
df.to_csv('data/sample.csv', index=False)
print("Sample data created: data/sample.csv")
