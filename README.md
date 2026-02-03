# Nataris — The People's AI Network

<p align="center">
  <strong>AI infrastructure owned by those who power it.</strong>
</p>

<p align="center">
  <a href="https://nataris.ai">Website</a> •
  <a href="https://nataris.ai/docs">API Docs</a> •
  <a href="https://nataris.ai/pricing">Pricing</a> •
  <a href="https://nataris.ai/faq">FAQ</a>
</p>

---

## What is Nataris?

Developers get affordable, private inference via API. Providers earn by running models on their mobiles—and keep 80%. The network grows with every device that joins.

**Powered by people, not datacenters.**

---

## How It Works

```
Developer App  →  Nataris API  →  Provider Network  →  AI Response
                      ↓
              Smart Routing
         (model, latency, availability)
                      ↓
            On-Device Inference
```

1. **Developers** send API requests to Nataris
2. **Smart routing** finds the best available device
3. **Providers** run inference locally on their phones
4. **Results** are returned via secure connections

---

## For Developers

| Benefit | Details |
|---------|---------|
| **$5 free credits** | No credit card required |
| **Pay for what you use** | No vendor lock-in, no minimums |
| **Open-weight models** | You choose how you use them |
| **No central logging** | Data not pooled in one cloud |
| **OpenAI-compatible** | Swap your base URL in minutes |

### Quick Start

```bash
curl -X POST https://api.nataris.ai/v1/jobs \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "modelId": "llama-3.2-1b-instruct-q4_k_m",
    "prompt": "Explain quantum computing in one paragraph."
  }'
```

### OpenAI SDK Compatible

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_NATARIS_KEY",
    base_url="https://api.nataris.ai/v1"
)

response = client.chat.completions.create(
    model="llama-3.2-1b-instruct-q4_k_m",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

---

## For Providers

| Benefit | Details |
|---------|---------|
| **₹200 (~$2.50) joining bonus** | After your first successful job |
| **Earn from idle compute** | Your phone works while you don't |
| **No expertise needed** | Just install and go online |
| **Device protection** | Thermal and battery safeguards |
| **Keep 80%** | Fair revenue share |

### Get Started

1. **Download** the Nataris app
2. **Select** models to host
3. **Go online** when you want to earn
4. **Get paid** per inference

**Requirements:** Android 8.0+, 4GB+ RAM

---

## Inference Capabilities

| Category | Models | Use Cases |
|----------|--------|-----------|
| **Text Generation** | Llama 3.2, Qwen 2.5, Phi-3, Mistral | Chat, code, summarization |
| **Speech-to-Text** | Whisper (3 sizes) | Transcription, voice commands |
| **Text-to-Speech** | Piper VITS | Voice synthesis, accessibility |
| **Voice Detection** | Silero VAD | Speech activity detection |
| **Voice Agent** | STT → LLM → TTS | Conversational AI pipeline |

---

## What You Can Build

- **Privacy-first apps** — Sensitive data stays on devices, not central logs
- **Multi-language support** — 100+ languages via Whisper
- **Creative freedom** — Open-weight models, your rules
- **Bots & automation** — High volume without strict rate limits
- **Prototyping** — Test ideas without big upfront spend

---

## Why Nataris?

| | Nataris | Traditional APIs |
|---|---------|------------------|
| **Logging** | No central prompt logging | Prompts stored on servers |
| **Models** | Open-weight, unfiltered | Vendor-controlled |
| **Pricing** | Pay-per-use, no minimums | Subscriptions, limits |
| **Economics** | 80% to providers | Value to corporations |

---

## Open Source

Built on amazing open-source projects:

| Project | Purpose |
|---------|---------|
| [RunAnywhere](https://github.com/AugustDev/runanywhere) | Cross-platform AI inference |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | Efficient LLM inference |
| [ONNX Runtime](https://github.com/microsoft/onnxruntime) | Cross-platform ML |
| [Whisper](https://github.com/openai/whisper) | Speech recognition |
| [Piper](https://github.com/rhasspy/piper) | Text-to-speech |

---

## Documentation

- [API Reference](https://nataris.ai/docs) — Complete endpoint docs
- [Integration Guide](./docs/integration-guide.md) — Step-by-step tutorial
- [Security](https://nataris.ai/security) — Our security model
- [FAQ](https://nataris.ai/faq) — Common questions

---

## Code Examples

Check out the [examples](./examples) folder:

- [Node.js](./examples/nodejs) — Express.js integration
- [Python](./examples/python) — FastAPI integration
- [cURL](./examples/curl) — Command-line examples

---

## Roadmap

| Quarter | Milestone |
|---------|-----------|
| **Q1 2026** | Beta launch — Android app, core models ← We are here |
| **Q2 2026** | Token launch — Provider rewards, staking |
| **Q3 2026** | iOS app — Enterprise tier, SLAs |
| **Q4 2026** | Ecosystem — Connectors, governance |

---

## Contact

- **Website:** [nataris.ai](https://nataris.ai)
- **Support:** support@nataris.ai
- **Security:** security@nataris.ai

---

## License

This repository (documentation and examples) is licensed under the MIT License. See [LICENSE](./LICENSE).

---

<p align="center">
  <em>"AI infrastructure, owned by everyone."</em>
</p>

<p align="center">
  <strong>Powered by people, not datacenters.</strong>
</p>
