#!/usr/bin/env python3
import requests
import json

api_key = "app-8VotUbgbHWgwj4Jj8XdPIL1o"
url = "https://api.dify.ai/v1/chat-messages"

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

payload = {
    "inputs": {},
    "query": "What is AI?",
    "response_mode": "streaming",
    "user": "test"
}

print("Testing new Chat App...")
print(f"App ID: {api_key}\n")

response = requests.post(url, headers=headers, json=payload, stream=True, timeout=10)
print(f"Status: {response.status_code}")

if response.status_code == 200:
    print("✅ SUCCESS! Streaming response:\n")
    full_answer = ""
    for line in response.iter_lines():
        if line:
            line_text = line.decode('utf-8')
            if line_text.startswith('data: '):
                try:
                    data = json.loads(line_text[6:])
                    event = data.get('event')
                    if event == 'message':
                        full_answer = data.get('answer', '')
                    elif event == 'agent_message':
                        full_answer += data.get('answer', '')
                except:
                    pass
    print(f"Answer: {full_answer[:200]}...")
else:
    print(f"❌ Error: {response.text}")
    try:
        error_data = response.json()
        print(f"\nDetails: {json.dumps(error_data, indent=2)}")
    except:
        pass
