# Nataris API Examples

Sample code for integrating with the Nataris API — including chat completions, orchestration workflows, RAG, and conversation memory.

## Prerequisites

1. Sign up at [nataris.ai](https://nataris.ai)
2. Get your API key from the [dashboard](https://nataris.ai/dashboard)

## Examples

### cURL

Command-line examples covering inference, chat, orchestration, and RAG.

```bash
cd curl
chmod +x *.sh

# Basic inference + chat + orchestration + RAG
./basic-inference.sh

# Transcribe audio
./transcribe-audio.sh recording.wav
```

### Node.js

```bash
cd nodejs
npm install
NATARIS_API_KEY=your_key npm start
```

Demonstrates: text inference, chat completions, and orchestrated research workflow.

### Python

```bash
cd python
pip install -r requirements.txt
NATARIS_API_KEY=your_key python example.py
```

Demonstrates: text inference, chat completions, and orchestrated research workflow.

## What's Covered

| Feature | cURL | Node.js | Python |
|---------|------|---------|--------|
| Text inference | Yes | Yes | Yes |
| Chat completions | Yes | Yes | Yes |
| Orchestration workflows | Yes | Yes | Yes |
| RAG (document upload) | Yes | — | — |
| Audio transcription | Yes | — | Yes |

## Need Help?

- [API Reference](../docs/api-reference.md)
- [Integration Guide](../docs/integration-guide.md)
- [FAQ](https://nataris.ai/faq)
- [Support](mailto:support@nataris.ai)
