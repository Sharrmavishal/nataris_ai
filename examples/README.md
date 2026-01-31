# Nataris API Examples

Sample code for integrating with the Nataris API.

## Prerequisites

1. Sign up at [nataris.ai](https://nataris.ai)
2. Get your API key from the [dashboard](https://nataris.ai/dashboard)

## Examples

### cURL

Simple command-line examples.

```bash
cd curl
chmod +x *.sh

# Basic inference
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

### Python

```bash
cd python
pip install -r requirements.txt
NATARIS_API_KEY=your_key python example.py
```

## Need Help?

- [API Documentation](https://nataris.ai/docs)
- [FAQ](https://nataris.ai/faq)
- [Support](mailto:support@nataris.ai)
