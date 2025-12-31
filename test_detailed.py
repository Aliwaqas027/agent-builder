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

print("Detailed streaming test...\n")

response = requests.post(url, headers=headers, json=payload, stream=True, timeout=10)
print(f"Status: {response.status_code}\n")

if response.status_code == 200:
    print("Raw streaming events:")
    print("-" * 70)
    
    for line in response.iter_lines():
        if line:
            line_text = line.decode('utf-8')
            print(line_text)
            
            if line_text.startswith('data: '):
                try:
                    data = json.loads(line_text[6:])
                    event = data.get('event')
                    
                    if event in ['message', 'agent_message', 'message_end']:
                        print(f"  → Event: {event}")
                        if 'answer' in data:
                            print(f"  → Answer: {data['answer'][:100]}")
                except Exception as e:
                    print(f"  → Parse error: {e}")
    
    print("-" * 70)
else:
    print(f"Error: {response.text}")
