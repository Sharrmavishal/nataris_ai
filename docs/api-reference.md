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
    "model": "qwen2.5-0.5b",
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
  "model": "qwen2.5-0.5b",
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

### POST /transcribe

Convert audio to text using Whisper.

**Request Body (multipart/form-data):**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `file` | file | Yes | Audio file (WAV, MP3, FLAC, M4A) |
| `model` | string | No | Whisper model (default: whisper-small) |
| `language` | string | No | ISO language code (auto-detect if omitted) |

**Example Request:**

```bash
curl -X POST https://api.nataris.ai/v1/transcribe \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@recording.wav" \
  -F "model=whisper-small"
```

**Example Response:**

```json
{
  "id": "trans_9876543210",
  "object": "transcription",
  "text": "Hello, this is a test recording.",
  "language": "en",
  "duration": 3.2,
  "segments": [
    {
      "start": 0.0,
      "end": 3.2,
      "text": "Hello, this is a test recording."
    }
  ]
}
```

---

### POST /synthesize

Convert text to speech using Piper.

**Request Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `text` | string | Yes | Text to synthesize |
| `model` | string | No | TTS model (default: piper-en-us) |
| `voice` | string | No | Voice variant |
| `speed` | float | No | Speed multiplier 0.5-2.0 (default: 1.0) |

**Example Request:**

```bash
curl -X POST https://api.nataris.ai/v1/synthesize \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Welcome to Nataris.",
    "model": "piper-en-us",
    "speed": 1.0
  }' \
  --output speech.wav
```

**Response:**

Returns audio file in WAV format (16-bit, 22050 Hz).

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
      "id": "qwen2.5-0.5b",
      "object": "model",
      "type": "llm",
      "description": "Qwen 2.5 0.5B - Fast, efficient language model",
      "available": true
    },
    {
      "id": "whisper-small",
      "object": "model",
      "type": "stt",
      "description": "Whisper Small - Multilingual speech recognition",
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
    "qwen2.5-0.5b": {
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
| 503 | `PROVIDER_UNAVAILABLE` | No providers available |

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

## Webhooks (Coming Soon)

Configure webhooks to receive notifications for:
- Job completion
- Low balance alerts
- Usage thresholds

---

## Support

- **Email:** support@nataris.ai
- **Docs:** https://nataris.ai/docs
