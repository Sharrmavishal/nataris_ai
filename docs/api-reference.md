# Nataris API Reference

Complete reference for the Nataris REST API.

## Overview

- **Base URL:** `https://api.nataris.ai/v1`
- **Authentication:** Bearer token (API key)
- **Content-Type:** `application/json` (unless otherwise noted)

## Authentication

Include your API key in the `Authorization` header:

```
Authorization: Bearer nat_live_xxxxxxxxxxxxxxxxxxxxxxxx
```

API keys are prefixed with:
- `nat_live_` - Production keys
- `nat_test_` - Test/sandbox keys

## Endpoints

---

### POST /chat/completions

**OpenAI-compatible** endpoint for conversational AI. Recommended for multi-turn conversations.

> **Important:** Nataris is stateless. Each request may hit a different provider device. You must send the full conversation history (messages array) with each request.

**Request Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `model` | string | Yes | Model identifier (e.g., "llama-3.2-1b-instruct-q4_k_m") |
| `messages` | array | Yes | Conversation history (see below) |
| `max_tokens` | integer | No | Maximum tokens to generate (default: 256) |
| `temperature` | float | No | Randomness 0-2 (default: 0.7) |
| `top_p` | float | No | Nucleus sampling 0-1 (default: 0.9) |
| `stream` | boolean | No | Enable SSE streaming (default: false) |
| `conversation_id` | string | No | Optional ID for your analytics |

**Message Format:**

```json
{
  "role": "system" | "user" | "assistant",
  "content": "Message text"
}
```

**Example Request:**

```bash
curl -X POST https://api.nataris.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.2-1b-instruct-q4_k_m",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is Python?"},
      {"role": "assistant", "content": "Python is a programming language..."},
      {"role": "user", "content": "Show me an example"}
    ],
    "max_tokens": 256
  }'
```

**Example Response:**

```json
{
  "id": "chatcmpl-abc123xyz",
  "object": "chat.completion",
  "created": 1706000000,
  "model": "llama-3.2-1b-instruct-q4_k_m",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Here's a simple Python example:\n\n```python\nprint('Hello, World!')\n```"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 45,
    "completion_tokens": 20,
    "total_tokens": 65
  }
}
```

**Streaming Response (SSE):**

When `stream: true`, returns Server-Sent Events:

```
data: {"id":"chatcmpl-abc123","choices":[{"delta":{"role":"assistant"}}]}
data: {"id":"chatcmpl-abc123","choices":[{"delta":{"content":"Here's"}}]}
data: {"id":"chatcmpl-abc123","choices":[{"delta":{"content":" a"}}]}
data: {"id":"chatcmpl-abc123","choices":[{"finish_reason":"stop"}]}
data: [DONE]
```

---

### POST /inference

Generate text using a language model.

**Request Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `model` | string | Yes | Model identifier |
| `prompt` | string | Yes | Input text prompt |
| `max_tokens` | integer | No | Maximum tokens to generate (default: 100) |
| `temperature` | float | No | Randomness 0-2 (default: 0.7) |
| `stream` | boolean | No | Enable streaming (default: false) |

**Example Request:**

```bash
curl -X POST https://api.nataris.ai/v1/inference \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-0.5b-instruct-q6_k",
    "prompt": "Write a haiku about AI",
    "max_tokens": 50,
    "temperature": 0.8
  }'
```

**Example Response:**

```json
{
  "id": "inf_1234567890",
  "object": "inference",
  "created": 1706000000,
  "model": "qwen2.5-0.5b-instruct-q6_k",
  "output": "Silicon minds wake\nLearning from humanity\nFuture uncertain",
  "usage": {
    "prompt_tokens": 6,
    "completion_tokens": 12,
    "total_tokens": 18
  },
  "provider": {
    "region": "IN",
    "latency_ms": 245
  }
}
```

---

### GET /models

List available models.

**Example Request:**

```bash
curl https://api.nataris.ai/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Example Response:**

```json
{
  "object": "list",
  "data": [
    {
      "id": "qwen2.5-0.5b-instruct-q6_k",
      "object": "model",
      "type": "llm",
      "description": "Qwen 2.5 0.5B - Fast, efficient language model",
      "available": true
    },
    {
      "id": "llama-3.2-1b-instruct-q4_k_m",
      "object": "model",
      "type": "llm",
      "description": "Llama 3.2 1B - General purpose language model",
      "available": true
    }
  ]
}
```

---

### GET /usage

Get current billing period usage.

**Example Request:**

```bash
curl https://api.nataris.ai/v1/usage \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Example Response:**

```json
{
  "object": "usage",
  "period_start": "2026-01-01T00:00:00Z",
  "period_end": "2026-01-31T23:59:59Z",
  "balance_usd": 4.75,
  "total_requests": 1250,
  "total_tokens": 125000,
  "by_model": {
    "qwen2.5-0.5b-instruct-q6_k": {
      "requests": 1000,
      "tokens": 100000
    },
    "whisper-small": {
      "requests": 250,
      "seconds": 3600
    }
  }
}
```

---

## Error Codes

| HTTP Code | Error Code | Description |
|-----------|------------|-------------|
| 400 | `INVALID_REQUEST` | Malformed request body |
| 401 | `INVALID_API_KEY` | Missing or invalid API key |
| 402 | `INSUFFICIENT_CREDITS` | Account balance depleted |
| 404 | `MODEL_NOT_FOUND` | Model doesn't exist |
| 429 | `RATE_LIMIT_EXCEEDED` | Too many requests |
| 202 | `MODEL_PROVISIONING` | Model is being provisioned (request queued) |

**Error Response Format:**

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Retry after 60 seconds.",
    "type": "rate_limit_error",
    "retry_after": 60
  }
}
```

---

---

### POST /chat/completions (with Orchestration)

Run multi-step AI workflows through a single API call.

**Additional Fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `orchestration.enabled` | boolean | No | Enable multi-step workflow |
| `orchestration.workflow` | string | No | `research`, `code`, `agent`, `map_reduce`, `auto` |
| `orchestration.max_steps` | integer | No | Maximum inference steps (default: 10) |
| `orchestration.max_cost_usd` | number | No | Budget cap in USD |

**Example Request:**

```bash
curl -X POST https://api.nataris.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
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
  }'
```

**Workflow Types:**

| Type | Steps | Use Case |
|------|-------|----------|
| `research` | research → analyze → write | Deep research synthesis |
| `code` | plan → implement → review | Code generation with review |
| `agent` | think → act (loop) | ReAct reasoning agent |
| `map_reduce` | chunk → map → reduce | Large document analysis |
| `auto` | Auto-selected | Based on input |

**Pricing:** Orchestrated steps are billed at the same base model rate (no surcharge). Use `POST /v1/workflows/estimate` to preview costs.

---

### POST /documents

Upload a document for RAG (Retrieval-Augmented Generation).

**Request Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `content` | string | Yes | Full document text |
| `document_name` | string | No | Filename for reference |
| `chunk_size` | integer | No | Characters per chunk (default: 1000) |
| `chunk_overlap` | integer | No | Overlap between chunks (default: 200) |

**Example Request:**

```bash
curl -X POST https://api.nataris.ai/v1/documents \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Your full document text here...",
    "document_name": "research-paper.txt"
  }'
```

**Example Response:**

```json
{
  "document_id": "doc_abc123",
  "chunks_created": 12,
  "document_name": "research-paper.txt"
}
```

---

### POST /chat/completions (with RAG)

Ask questions grounded in your uploaded documents.

**Additional Fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `rag.enabled` | boolean | No | Enable RAG context injection |
| `rag.document_id` | string | No | Limit to specific document |
| `rag.max_chunks` | integer | No | Max context chunks (default: 3) |

**Example:**

```bash
curl -X POST https://api.nataris.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.2-1b-instruct-q4_k_m",
    "messages": [{"role": "user", "content": "Summarize the key findings"}],
    "rag": {"enabled": true, "document_id": "doc_abc123", "max_chunks": 5}
  }'
```

---

### POST /conversations

Create a conversation for server-side message persistence.

**Example Response:**

```json
{
  "id": "conv_xyz789",
  "title": null,
  "message_count": 0,
  "created_at": "2026-01-25T10:00:00Z"
}
```

Then pass `conversation_id` in chat completions:

```json
{
  "model": "llama-3.2-1b-instruct-q4_k_m",
  "messages": [{"role": "user", "content": "Hello!"}],
  "conversation_id": "conv_xyz789"
}
```

Messages are automatically persisted. Titles are auto-generated. Older messages are summarized to maintain context efficiently.

**Other conversation endpoints:**
- `GET /conversations` — List conversations
- `GET /conversations/:id` — Get context (messages + summary)
- `DELETE /conversations/:id` — Delete conversation

---

### GET /workflows

List your orchestration workflows.

**Example Response:**

```json
{
  "workflows": [
    {
      "id": "wf_123",
      "type": "RESEARCH",
      "status": "COMPLETED",
      "task": "Research renewable energy",
      "total_cost_usd": 0.042,
      "steps_executed": 3,
      "created_at": "2026-01-25T10:00:00Z"
    }
  ],
  "total": 1
}
```

---

### POST /workflows/estimate

Preview cost before running a workflow.

```bash
curl -X POST https://api.nataris.ai/v1/workflows/estimate \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "llama-3.2-1b-instruct-q4_k_m", "workflow": "research"}'
```

---

## Webhooks (Coming Soon)

Configure webhooks to receive notifications for:
- Job completion
- Low balance alerts
- Usage thresholds

---

## Support

- **Email:** support@nataris.ai
- **Docs:** https://nataris.ai/docs
