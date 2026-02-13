#!/bin/bash
# Nataris API - Audio Transcription Example
#
# NOTE: Audio endpoints (STT, TTS, Voice Agent) are temporarily disabled
# while we scale the text inference network. They will be re-enabled soon.
#
# Replace YOUR_API_KEY with your actual API key

API_KEY="YOUR_API_KEY"
API_URL="https://api.nataris.ai/v1"

echo "⚠️  Audio endpoints are temporarily disabled."
echo "They will be re-enabled once text inference capacity grows."
echo ""
echo "In the meantime, try text inference:"
echo "  ./basic-inference.sh"
