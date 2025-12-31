#!/usr/bin/env python3
"""
Check what type of Dify app we're dealing with
"""
import requests
import json

api_key = "app-zEpyX9lzyWkM7aX1vTym2snU"
base_url = "https://api.dify.ai/v1"

print("\n" + "="*70)
print("  Checking Dify App Configuration")
print("="*70 + "\n")

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Check parameters endpoint
print("1. Checking app parameters...")
try:
    response = requests.get(f"{base_url}/parameters", headers=headers, timeout=10)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nApp Configuration:")
        print(json.dumps(data, indent=2)[:1000])
    else:
        print(f"Error: {response.text}")
except Exception as e:
    print(f"Exception: {e}")

# Check info endpoint
print("\n2. Checking app info...")
try:
    response = requests.get(f"{base_url}/info", headers=headers, timeout=10)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nApp Info:")
        print(json.dumps(data, indent=2))
    else:
        print(f"Error: {response.text}")
except Exception as e:
    print(f"Exception: {e}")

# Check meta endpoint
print("\n3. Checking app meta...")
try:
    response = requests.get(f"{base_url}/meta", headers=headers, timeout=10)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nApp Meta:")
        print(json.dumps(data, indent=2))
    else:
        print(f"Error: {response.text}")
except Exception as e:
    print(f"Exception: {e}")

print("\n" + "="*70)
print("\nDiagnosis:")
print("-" * 70)
print("""
The app might be:
1. An Agent app (requires workflow configuration)
2. A Chat app (requires model configuration)
3. Not properly published
4. Missing model configuration in the orchestrate section

Next steps:
- Check if this is an "Agent" type app
- Agent apps need workflow nodes configured
- Each node needs a model selected
- Regular Chat apps need model in settings
""")
print("="*70 + "\n")
