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

Developers get affordable, private inference via API. Providers earn by running models on their mobiles—and keep 85%. The network grows with every device that joins.

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
| **No model training** | Your prompts are never used to train AI models |
| **OpenAI-compatible** | Swap your base URL in minutes |

### Quick Start

```bash
curl -X POST https://api.nataris.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.2-1b-instruct-q4_k_m",
    "messages": [{"role": "user", "content": "Explain quantum computing in one paragraph."}]
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
| **Joining bonus** | Earn a bonus after completing your first job (subject to eligibility criteria) |
| **Earn from idle compute** | Your phone works while you don't |
| **No expertise needed** | Just install and go online |
| **Device protection** | Thermal and battery safeguards |
| **Keep 85%** | Fair revenue share |

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
| **Text Generation** | Qwen 2.5 0.5B, Llama 3.2 1B, Phi-3 Mini 3.8B | Chat, code, summarization |
| **Text Generation (coming soon)** | Mistral 7B, Llama 2 7B | Advanced tasks, broad knowledge |

> **Audio (STT, TTS, Voice Agent):** Built but temporarily disabled while we scale the text inference network. Will be re-enabled once provider capacity grows.

## Advanced Features

| Feature | Description |
|---------|-------------|
| **Multi-Step Workflows** | Orchestrate research, code gen, agent, and map-reduce pipelines via a single API call |
| **RAG (Document Q&A)** | Upload documents, get answers grounded in your content *(coming soon)* |
| **Conversation Memory** | Server-side message persistence with auto-summarization |
| **Cost Controls** | Budget caps per workflow, cost estimation endpoint |

### Orchestration Example

```python
response = client.chat.completions.create(
    model="llama-3.2-1b-instruct-q4_k_m",
    messages=[{"role": "user", "content": "Research renewable energy trends"}],
    extra_body={
        "orchestration": {
            "enabled": True,
            "workflow": "research",
            "max_cost_usd": 1.0
        }
    }
)
```

---

## What You Can Build

- **Creative freedom** — Open-weight models, no content filtering, your rules
- **Privacy-first apps** — Your prompts are not used to train models or fed into corporate AI pipelines
- **Bots & automation** — High volume without strict rate limits
- **Prototyping** — Test ideas without big upfront spend
- **Research pipelines** — Multi-step analysis orchestrated automatically
- **Document Q&A** — RAG-powered answers from your own documents *(coming soon)*

---

## Why Nataris?

| | Nataris | Traditional APIs |
|---|---------|------------------|
| **Data use** | Prompts never used for model training | Often used to improve models |
| **Models** | Open-weight, unfiltered | Vendor-controlled |
| **Pricing** | Pay-per-use, no minimums | Subscriptions, limits |
| **Economics** | 85% to providers | Value to corporations |
| **Filtering** | No content filtering | Vendor-controlled output |

---

## Open Source

Built on amazing open-source projects:

| Project | Purpose |
|---------|---------|
| [RunAnywhere](https://github.com/AugustDev/runanywhere) | Cross-platform AI inference |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | Efficient LLM inference |
| [ONNX Runtime](https://github.com/microsoft/onnxruntime) | Cross-platform ML |
| [Ollama](https://github.com/ollama/ollama) | Cloud backstop inference |

---

## Documentation

- [API Reference](./docs/api-reference.md) — Complete endpoint docs (orchestration, conversations)
- [Integration Guide](./docs/integration-guide.md) — Step-by-step tutorial with advanced features
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
| **Q2 2026** | iOS app, 7B models, RAG |
| **Q3 2026** | Enterprise tier, SLAs |
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
