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


def inference(prompt: str, model: str = 'qwen2.5-0.5b', max_tokens: int = 100) -> dict:
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


def transcribe(audio_path: str, model: str = 'whisper-small') -> dict:
    """Transcribe an audio file."""
    with open(audio_path, 'rb') as f:
        response = requests.post(
            f'{API_URL}/transcribe',
            headers={'Authorization': f'Bearer {API_KEY}'},
            files={'file': f},
            data={'model': model}
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

    print('=== Done ===')


if __name__ == '__main__':
    main()
