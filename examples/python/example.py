#!/usr/bin/env python3
"""
Nataris API - Python Example

Install dependencies:
    pip install requests

Run:
    NATARIS_API_KEY=your_key python example.py
"""

import os
import requests

API_KEY = os.environ.get('NATARIS_API_KEY')
API_URL = 'https://api.nataris.ai/v1'

if not API_KEY:
    print('Error: NATARIS_API_KEY environment variable is required')
    print('Usage: NATARIS_API_KEY=your_key python example.py')
    exit(1)

HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}


def inference(prompt: str, model: str = 'qwen2.5-0.5b-instruct-q6_k', max_tokens: int = 100) -> dict:
    """Make an inference request."""
    response = requests.post(
        f'{API_URL}/inference',
        headers=HEADERS,
        json={
            'model': model,
            'prompt': prompt,
            'max_tokens': max_tokens,
        }
    )
    response.raise_for_status()
    return response.json()


def list_models() -> dict:
    """List available models."""
    response = requests.get(f'{API_URL}/models', headers=HEADERS)
    response.raise_for_status()
    return response.json()


def get_usage() -> dict:
    """Get usage and balance."""
    response = requests.get(f'{API_URL}/usage', headers=HEADERS)
    response.raise_for_status()
    return response.json()


def main():
    print('=== Nataris API - Python Example ===\n')

    # 1. Check balance
    print('1. Checking balance...')
    usage = get_usage()
    print(f'   Balance: ${usage["balance_usd"]}')
    print(f'   Requests this period: {usage["total_requests"]}\n')

    # 2. List models
    print('2. Available models:')
    models = list_models()
    for m in models['data']:
        print(f'   - {m["id"]} ({m["type"]})')
    print()

    # 3. Make inference
    print('3. Making inference request...')
    result = inference('Explain machine learning in one sentence.')
    print(f'   Model: {result["model"]}')
    print(f'   Response: {result["output"]}')
    print(f'   Tokens used: {result["usage"]["total_tokens"]}\n')

    # 4. Chat Completions (OpenAI-compatible)
    print('4. Chat completion...')
    chat_response = requests.post(
        f'{API_URL}/chat/completions',
        headers=HEADERS,
        json={
            'model': 'llama-3.2-1b-instruct-q4_k_m',
            'messages': [{'role': 'user', 'content': 'What is quantum computing?'}],
            'max_tokens': 100,
        }
    )
    chat = chat_response.json()
    content = chat.get('choices', [{}])[0].get('message', {}).get('content', '')
    print(f'   Response: {content[:80]}...\n')

    # 5. Orchestration — multi-step research workflow
    print('5. Orchestrated research workflow...')
    orch_response = requests.post(
        f'{API_URL}/chat/completions',
        headers=HEADERS,
        json={
            'model': 'llama-3.2-1b-instruct-q4_k_m',
            'messages': [{'role': 'user', 'content': 'Research the impact of AI on healthcare'}],
            'orchestration': {
                'enabled': True,
                'workflow': 'research',
                'max_cost_usd': 1.0,
            },
        }
    )
    orch = orch_response.json()
    nataris = orch.get('nataris', {})
    print(f'   Workflow: {nataris.get("workflow_id", "N/A")}')
    print(f'   Steps: {nataris.get("steps_executed", "N/A")}')
    print(f'   Cost: ${nataris.get("total_cost_usd", "N/A")}\n')

    print('=== Done ===')


if __name__ == '__main__':
    main()
