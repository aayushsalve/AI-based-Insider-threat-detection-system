import requests
import json

BASE_URL = "http://localhost:5001"
HEADERS = {"X-API-Key": "insider-threat-api-2026"}

print("Testing Insider Threat Detection API\n")

# Test 1: Health Check
try:
    response = requests.get(f"{BASE_URL}/api/v1/health", headers=HEADERS)
    print(f"✅ Health: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"❌ Health failed: {str(e)}")

print("\n" + "="*60 + "\n")

# Test 2: Stats
try:
    response = requests.get(f"{BASE_URL}/api/v1/stats", headers=HEADERS)
    print(f"✅ Stats: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"❌ Stats failed: {str(e)}")

print("\n" + "="*60 + "\n")

# Test 3: Critical Threats
try:
    response = requests.get(
        f"{BASE_URL}/api/v1/critical-threats", headers=HEADERS
    )
    print(f"✅ Critical Threats: {response.status_code}")
    data = response.json()
    print(f"Total threats: {data['count']}")
    print("First 3:")
    for threat in data['threats'][:3]:
        print(f"  - {threat['user_id']}: {threat['risk_score']:.1f}")
except Exception as e:
    print(f"❌ Critical threats failed: {str(e)}")
