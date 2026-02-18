import urllib.request
import json

url = "http://localhost:5001/api/v1/health"
headers = {"X-API-Key": "insider-threat-api-2026"}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())
        print("✅ API Response:")
        print(json.dumps(data, indent=2))
except Exception as e:
    print(f"❌ Error: {str(e)}")
