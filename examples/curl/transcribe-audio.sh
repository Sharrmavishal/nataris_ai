#!/bin/bash
# Nataris API - Audio Transcription Example
# Replace YOUR_API_KEY with your actual API key

API_KEY="YOUR_API_KEY"
API_URL="https://api.nataris.ai/v1"

# Check if audio file is provided
if [ -z "$1" ]; then
  echo "Usage: ./transcribe-audio.sh <audio-file>"
  echo "Example: ./transcribe-audio.sh recording.wav"
  exit 1
fi

AUDIO_FILE="$1"

# Check if file exists
if [ ! -f "$AUDIO_FILE" ]; then
  echo "Error: File not found: $AUDIO_FILE"
  exit 1
fi

echo "Transcribing: $AUDIO_FILE"
echo "Using model: whisper-small"
echo ""

curl -X POST "${API_URL}/transcribe" \
  -H "Authorization: Bearer ${API_KEY}" \
  -F "file=@${AUDIO_FILE}" \
  -F "model=whisper-small" | jq .
