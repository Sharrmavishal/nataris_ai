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
    "model": "qwen2.5-0.5b-instruct-q6_k",
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

# 4. Chat Completions (OpenAI-compatible)
echo "4. Chat Completions"
echo "--------------------"
curl -s -X POST "${API_URL}/chat/completions" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.2-1b-instruct-q4_k_m",
    "messages": [{"role": "user", "content": "What is quantum computing?"}],
    "max_tokens": 100
  }' | jq .

echo ""

# 5. Orchestrated Research Workflow
echo "5. Orchestrated Research Workflow"
echo "----------------------------------"
curl -s -X POST "${API_URL}/chat/completions" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.2-1b-instruct-q4_k_m",
    "messages": [{"role": "user", "content": "Research renewable energy trends"}],
    "orchestration": {
      "enabled": true,
      "workflow": "research",
      "max_steps": 10,
      "max_cost_usd": 1.0
    }
  }' | jq .

echo ""

# 6. RAG — Upload document and query
echo "6. RAG: Upload Document"
echo "------------------------"
curl -s -X POST "${API_URL}/documents" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Renewable energy is growing rapidly. Solar power capacity doubled in 2025. Wind energy now provides 10% of global electricity.",
    "document_name": "energy-report.txt"
  }' | jq .

echo ""
echo "=== Done ==="
