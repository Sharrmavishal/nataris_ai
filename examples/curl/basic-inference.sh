#!/bin/bash
# Nataris API - Basic Inference Example
# Replace YOUR_API_KEY with your actual API key

API_KEY="YOUR_API_KEY"
API_URL="https://api.nataris.ai/v1"

echo "=== Nataris API Examples ==="
echo ""

# 1. Text Generation
echo "1. Text Generation (LLM)"
echo "-------------------------"
curl -s -X POST "${API_URL}/inference" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-0.5b",
    "prompt": "What is the capital of France? Answer in one sentence.",
    "max_tokens": 50
  }' | jq .

echo ""

# 2. List Available Models
echo "2. List Available Models"
echo "------------------------"
curl -s "${API_URL}/models" \
  -H "Authorization: Bearer ${API_KEY}" | jq .

echo ""

# 3. Check Usage/Balance
echo "3. Check Usage & Balance"
echo "------------------------"
curl -s "${API_URL}/usage" \
  -H "Authorization: Bearer ${API_KEY}" | jq .

echo ""
echo "=== Done ==="
