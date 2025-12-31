#!/usr/bin/env python3
import requests
import json

api_key = "app-zEpyX9lzyWkM7aX1vTym2snU"
url = "https://api.dify.ai/v1/chat-messages"

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

payload = {
    "inputs": {},
    "query": "Hello",
    "response_mode": "streaming",
    "user": "test"
}

print("Testing Dify API...")
print(f"Payload: {json.dumps(payload, indent=2)}\n")

response = requests.post(url, headers=headers, json=payload, stream=True)
print(f"Status: {response.status_code}")

if response.status_code != 200:
    print(f"Error: {response.text}")
else:
    print("Success! Streaming response:")
    for line in response.iter_lines():
        if line:
            print(line.decode('utf-8'))
