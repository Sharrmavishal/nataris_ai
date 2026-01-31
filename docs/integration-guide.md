# Nataris Integration Guide

This guide walks you through integrating Nataris AI APIs into your application.

## Prerequisites

- Nataris account ([sign up here](https://nataris.ai/register))
- API key (available in your [dashboard](https://nataris.ai/dashboard))

## Authentication

All API requests require authentication via Bearer token:

```bash
Authorization: Bearer YOUR_API_KEY
```

## Base URL

```
https://api.nataris.ai/v1
```

## Available Endpoints

### Text Generation (LLM)

Generate text using language models.

```bash
POST /v1/inference
```

**Request:**
```json
{
  "model": "qwen2.5-0.5b",
  "prompt": "Explain quantum computing in simple terms",
  "max_tokens": 200,
  "temperature": 0.7
}
```

**Response:**
```json
{
  "id": "inf_abc123",
  "model": "qwen2.5-0.5b",
  "output": "Quantum computing uses quantum mechanics...",
  "usage": {
    "prompt_tokens": 8,
    "completion_tokens": 145,
    "total_tokens": 153
  }
}
```

### Speech-to-Text (Whisper)

Transcribe audio to text.

```bash
POST /v1/transcribe
```

**Request (multipart/form-data):**
```bash
curl -X POST https://api.nataris.ai/v1/transcribe \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "file=@audio.wav" \
  -F "model=whisper-small"
```

**Response:**
```json
{
  "id": "trans_xyz789",
  "text": "Hello, how can I help you today?",
  "language": "en",
  "duration": 2.5
}
```

### Text-to-Speech (Piper)

Convert text to natural speech.

```bash
POST /v1/synthesize
```

**Request:**
```json
{
  "model": "piper-en-us",
  "text": "Welcome to Nataris, the people's AI network.",
  "voice": "default"
}
```

**Response:**
Returns audio file (WAV format).

## Supported Models

### Language Models

| Model | Parameters | Best For |
|-------|------------|----------|
| `qwen2.5-0.5b` | 0.5B | Fast responses, simple tasks |
| `qwen2.5-1.5b` | 1.5B | Balanced performance |
| `llama-3.2-1b` | 1B | General purpose |
| `phi-3-mini` | 3.8B | Complex reasoning |

### Speech Models

| Model | Size | Languages |
|-------|------|-----------|
| `whisper-tiny` | 39MB | Multilingual |
| `whisper-small` | 244MB | Multilingual |
| `piper-en-us` | 20MB | English |

## Error Handling

### Error Response Format

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests. Please retry after 60 seconds.",
    "retry_after": 60
  }
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `INVALID_API_KEY` | 401 | API key is invalid or missing |
| `INSUFFICIENT_CREDITS` | 402 | Account balance too low |
| `RATE_LIMIT_EXCEEDED` | 429 | Too many requests |
| `MODEL_NOT_FOUND` | 404 | Requested model unavailable |
| `PROVIDER_UNAVAILABLE` | 503 | No providers available |

## Best Practices

### 1. Handle Errors Gracefully

```javascript
try {
  const response = await fetch('https://api.nataris.ai/v1/inference', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ model: 'qwen2.5-0.5b', prompt: 'Hello' })
  });
  
  if (!response.ok) {
    const error = await response.json();
    if (error.error.code === 'RATE_LIMIT_EXCEEDED') {
      // Wait and retry
      await sleep(error.error.retry_after * 1000);
      // Retry request...
    }
  }
} catch (error) {
  console.error('Network error:', error);
}
```

### 2. Use Appropriate Models

Choose the smallest model that meets your needs:
- Simple Q&A → `qwen2.5-0.5b`
- Complex reasoning → `phi-3-mini`
- Quick transcription → `whisper-tiny`

### 3. Monitor Usage

Check your usage in the [billing dashboard](https://nataris.ai/billing) to:
- Track credit consumption
- Set up usage alerts
- Review request history

## Rate Limits

| Tier | Requests/min | Concurrent |
|------|--------------|------------|
| Free | 10 | 2 |
| Starter | 60 | 5 |
| Pro | 300 | 20 |

## SDKs (Coming Soon)

We're working on official SDKs for:
- Node.js / TypeScript
- Python
- Go

In the meantime, use the REST API directly or check our [examples](../examples/).

## Support

- **Documentation:** [nataris.ai/docs](https://nataris.ai/docs)
- **FAQ:** [nataris.ai/faq](https://nataris.ai/faq)
- **Support:** support@nataris.ai
