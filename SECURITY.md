# Security Policy

## Reporting a Vulnerability

We take security seriously at Nataris. If you discover a security vulnerability, please report it responsibly.

### How to Report

**Email:** security@nataris.ai

Please include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested fixes (optional)

### What to Expect

1. **Acknowledgment:** We'll acknowledge your report within 48 hours
2. **Assessment:** We'll investigate and assess the severity within 7 days
3. **Resolution:** We'll work on a fix and keep you updated on progress
4. **Disclosure:** Once fixed, we'll coordinate disclosure with you

### Scope

This policy applies to:
- Nataris API (api.nataris.ai)
- Nataris Developer Portal (nataris.ai)
- Nataris Provider App (Android)
- This repository and related code

### Out of Scope

- Social engineering attacks
- Denial of service attacks
- Issues in third-party dependencies (report these to the maintainers)
- Issues that require physical access to a user's device

## Security Practices

### API Security
- All API traffic is encrypted via TLS 1.3
- API keys are hashed and never stored in plaintext
- Rate limiting protects against abuse
- Request validation using strict schemas

### Provider Network
- WebSocket connections secured with WSS
- Provider identity verified via device attestation
- Job assignments validated server-side
- No direct peer-to-peer connections

### Data Handling
- Inference data processed locally on provider devices
- Minimal data retention on platform servers
- No training on user data
- GDPR-compliant data practices

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| < 1.0   | :x:                |

## Contact

- **Security issues:** security@nataris.ai
- **General support:** support@nataris.ai
- **Privacy concerns:** privacy@nataris.ai
