# Nataris - The People's AI Network

<p align="center">
  <strong>Decentralized AI inference powered by everyday devices</strong>
</p>

<p align="center">
  <a href="https://nataris.ai">Website</a> •
  <a href="https://nataris.ai/docs">Documentation</a> •
  <a href="https://nataris.ai/faq">FAQ</a> •
  <a href="https://nataris.ai/roadmap">Roadmap</a>
</p>

---

## What is Nataris?

Nataris is a decentralized AI infrastructure platform that connects developers who need affordable AI capabilities with device owners who want to earn by sharing their idle compute power.

**For Developers:**
- Access AI models (LLMs, Speech-to-Text, Text-to-Speech) via simple REST APIs
- Pay only for what you use - no minimums, no subscriptions
- No vendor lock-in, no rate limits

**For Providers:**
- Earn passive income by sharing your device's idle compute
- All processing happens locally on your device
- You control when and how your device participates

## How It Works

```
Developer App  →  Nataris API  →  Provider Network  →  AI Response
     ↑                                                      ↓
     └──────────────────────────────────────────────────────┘
```

1. **Developers** send API requests to Nataris
2. **Smart routing** matches requests to optimal providers based on model, latency, and availability
3. **Providers** run inference locally using on-device AI models
4. **Results** are returned to developers via secure WebSocket connections

## Supported Models

| Category | Models | Use Cases |
|----------|--------|-----------|
| **LLM** | Qwen 2.5, Llama 3.2, Phi-3 | Chat, summarization, code generation |
| **Speech-to-Text** | Whisper (multiple sizes) | Transcription, voice commands |
| **Text-to-Speech** | Piper | Voice synthesis, accessibility |

## Quick Start

### For Developers

1. **Sign up** at [nataris.ai](https://nataris.ai) and get your API key
2. **Make your first request:**

```bash
curl -X POST https://api.nataris.ai/v1/inference \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-0.5b",
    "prompt": "What is the capital of France?",
    "max_tokens": 100
  }'
```

3. **Explore the docs** for advanced features like streaming, voice agents, and batch processing

### For Providers

1. **Download** the Nataris Provider App from [Google Play](https://play.google.com/store/apps/details?id=ai.nataris.provider)
2. **Register** and set up your device
3. **Start earning** when developers use your compute

## Documentation

- [API Reference](https://nataris.ai/docs) - Complete API documentation
- [Integration Guide](./docs/integration-guide.md) - Step-by-step integration tutorial
- [FAQ](https://nataris.ai/faq) - Frequently asked questions
- [Security](https://nataris.ai/security) - Our security practices

## Open Source

Nataris is built on top of amazing open-source projects:

- [RunAnywhere](https://github.com/AugustDev/runanywhere) - Cross-platform AI inference
- [llama.cpp](https://github.com/ggerganov/llama.cpp) - Efficient LLM inference
- [ONNX Runtime](https://github.com/microsoft/onnxruntime) - Cross-platform ML inference
- [Whisper](https://github.com/openai/whisper) - Speech recognition
- [Piper](https://github.com/rhasspy/piper) - Text-to-speech

## Examples

Check out the [examples](./examples) folder for sample integrations:

- [Node.js](./examples/nodejs) - Express.js integration
- [Python](./examples/python) - FastAPI integration
- [cURL](./examples/curl) - Command-line examples

## Community

- **Website:** [nataris.ai](https://nataris.ai)
- **Support:** support@nataris.ai
- **Security:** security@nataris.ai

## License

This repository is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

---

<p align="center">
  <strong>Built for developers, powered by the community</strong>
</p>
