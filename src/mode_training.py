from sklearn.ensemble import RandomForestClassifier
import joblib

# Assuming the data has been preprocessed and split into X_train, X_test,
# y_train, y_test

# Example: Load or create your dataset here
# Replace the following lines with your actual data loading and preprocessing
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
	data.data, data.target, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model for future use
joblib.dump(model, 'models/malicious_insider_model.pkl')
