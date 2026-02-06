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

### Chat Completions (Recommended)

OpenAI-compatible endpoint for conversational AI. **This is the recommended approach for multi-turn conversations.**

```bash
POST /v1/chat/completions
```

**Request:**
```json
{
  "model": "llama-3.2-1b",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language..."},
    {"role": "user", "content": "Show me an example"}
  ],
  "max_tokens": 256
}
```

**Response:**
```json
{
  "id": "chatcmpl-abc123",
  "model": "llama-3.2-1b",
  "choices": [{
    "message": {
      "role": "assistant",
      "content": "Here's a simple Python example:\n\n```python\nprint('Hello!')\n```"
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 45,
    "completion_tokens": 20,
    "total_tokens": 65
  }
}
```

### Text Generation (Single Prompt)

For single-turn text generation without conversation history.

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
| `MODEL_PROVISIONING` | 202 | Model is being provisioned (request queued) |

## Multi-Step Workflows (Orchestration)

For complex tasks, Nataris can chain multiple inference steps automatically. Add the `orchestration` field to your chat completion request:

```json
{
  "model": "llama-3.2-1b",
  "messages": [{"role": "user", "content": "Research the benefits of solar energy"}],
  "orchestration": {
    "enabled": true,
    "workflow": "research",
    "max_steps": 10,
    "max_cost_usd": 1.0
  }
}
```

**Workflow types:** `research` (research → analyze → write), `code` (plan → implement → review), `agent` (ReAct think/act loop), `map_reduce` (parallel document processing), `auto` (auto-detected).

Orchestrated steps are billed at 1.5x base rate. Use `POST /v1/workflows/estimate` to preview costs before running.

## Document-Grounded Responses (RAG)

Upload documents and use them as context for chat responses:

```bash
# 1. Upload a document
curl -X POST https://api.nataris.ai/v1/documents \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"content": "Your document text...", "document_name": "paper.txt"}'

# 2. Ask questions with document context
curl -X POST https://api.nataris.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.2-1b",
    "messages": [{"role": "user", "content": "Summarize the key findings"}],
    "rag": {"enabled": true, "document_id": "DOC_ID", "max_chunks": 5}
  }'
```

Document storage and semantic search are included at no extra cost.

## Conversation Memory

Nataris supports **server-side conversation memory** — no need to send full chat history every time.

```bash
# 1. Create a conversation
curl -X POST https://api.nataris.ai/v1/conversations \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model_id": "llama-3.2-1b"}'
# Returns: {"id": "conv_xyz789", ...}

# 2. Chat with conversation_id — messages auto-persist
curl -X POST https://api.nataris.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.2-1b",
    "messages": [{"role": "user", "content": "Hello!"}],
    "conversation_id": "conv_xyz789"
  }'

# Subsequent messages have full context automatically
curl -X POST https://api.nataris.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.2-1b",
    "messages": [{"role": "user", "content": "Tell me more about that"}],
    "conversation_id": "conv_xyz789"
  }'
```

The API auto-generates titles, creates rolling summaries of older messages, and manages context windows.

## Context Management

Nataris is a P2P network where each request may be processed by a different provider device. You have two options:

### Option A: Server-Side Memory (Recommended)
Use `conversation_id` as shown above — the API handles everything.

### Option B: Client-Side History
> **Send the full conversation history with each request.**

### Why This Matters

```
❌ Wrong approach:
   Request 1: "What is Python?"  → Device A → "Python is a language..."
   Request 2: "Show me an example" → Device B → "Example of what?" (no context!)

✅ Correct approach:
   Request 2 includes full history:
   [
     {"role": "user", "content": "What is Python?"},
     {"role": "assistant", "content": "Python is a language..."},
     {"role": "user", "content": "Show me an example"}
   ]
   → Device B has full context and responds correctly!
```

### Best Practice: Use the SDK

Our TypeScript SDK includes a `Conversation` class that handles this automatically:

```typescript
import { NatarisClient, Conversation } from '@nataris/sdk';

const nataris = new NatarisClient({ apiKey: 'YOUR_KEY' });
const conversation = new Conversation(nataris, { model: 'llama-3.2-1b' });

// SDK automatically accumulates and sends full history
await conversation.send('What is Python?');
await conversation.send('Show me an example'); // Context included automatically!
```

### Manual Context Management

If using the API directly, maintain message history in your application:

```javascript
// Maintain conversation state
const messages = [];

async function chat(userMessage) {
  messages.push({ role: 'user', content: userMessage });
  
  const response = await fetch('https://api.nataris.ai/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_KEY',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: 'llama-3.2-1b',
      messages: messages  // Send full history
    })
  });
  
  const data = await response.json();
  const assistantMessage = data.choices[0].message;
  
  messages.push(assistantMessage);  // Add to history
  return assistantMessage.content;
}

// Usage
await chat('What is Python?');
await chat('Show me an example');  // Works! Full context is sent
```

### Conversation ID

Pass `conversation_id` to enable server-side memory, or use it for your own analytics:

```json
{
  "model": "llama-3.2-1b",
  "messages": [...],
  "conversation_id": "conv_xyz789"
}
```

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

## SDKs

### TypeScript / Node.js (Available Now)

```bash
npm install @nataris/sdk
```

```typescript
import { NatarisClient, Conversation } from '@nataris/sdk';

// Initialize
const nataris = new NatarisClient({ apiKey: 'YOUR_KEY' });

// Simple chat
const response = await nataris.chat({
  model: 'llama-3.2-1b',
  messages: [{ role: 'user', content: 'Hello!' }]
});

// Multi-turn conversation (auto context management)
const conversation = new Conversation(nataris, { 
  model: 'llama-3.2-1b',
  systemPrompt: 'You are a helpful assistant.'
});
await conversation.send('What is Python?');
await conversation.send('Show me an example');  // Has context!

// Streaming
for await (const chunk of nataris.chatStream({
  model: 'llama-3.2-1b',
  messages: [{ role: 'user', content: 'Tell me a story' }]
})) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? '');
}
```

### Python / Go (Coming Soon)

We're working on additional SDKs. Check our [examples](../examples/) for raw API usage.

## Support

- **Documentation:** [nataris.ai/docs](https://nataris.ai/docs)
- **FAQ:** [nataris.ai/faq](https://nataris.ai/faq)
- **Support:** support@nataris.ai
