# IRIS – Drafting & Composition Agent

**Mission**: Generate structured outlines and high-quality drafts in the author's authentic tone.

## Core Capabilities

- Transform Aletheia briefs into structured outlines (Define → Contrast → Synthesize → Project)
- Apply VoicePrint parameters to preserve cadence, rhythm, and diction
- Generate drafts with voice and stylistic metrics
- Output in markdown or plain text for Notion synchronization

## API Endpoints

- `POST /v1/outlines` - Generate structured outlines from idea briefs
- `POST /v1/drafts` - Generate full drafts with voice parameters
- `GET /v1/drafts/{id}` - Retrieve specific draft details
- `GET /healthz` - Health check endpoint

## Key Deliverables

- `voiceprint.json` - Voice parameters for authentic tone preservation
- Prompt templates for outline and draft generation
- FastAPI endpoints for outline and draft creation

## Dependencies

- Python 3.11+
- FastAPI, uvicorn
- Anthropic SDK (for draft generation)
- Optional OpenAI cross-checking
- Shared SDK for schemas and logging

## Development

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the service
uvicorn main:app --reload --port 8002

# Install additional dependencies
pip install <package>
pip freeze > requirements.txt
```

## Data Flow

IRIS receives ideas from Aletheia and sends drafts to Erebus:

```
Aletheia → IRIS → Erebus
            ↑
        Mnemosyne (voice consistency)
```

## VoicePrint System

IRIS maintains authentic voice through:
- Cadence and rhythm patterns
- Diction preferences and vocabulary
- Sentence structure templates
- Stylistic markers

## Related Repositories

- [agent-aletheia](https://github.com/stephenpeters/agent-aletheia) - Provides content ideas
- [agent-erebus](https://github.com/stephenpeters/agent-erebus) - Refines drafts for authenticity
- [agent-mnemosyne](https://github.com/stephenpeters/agent-mnemosyne) - Provides voice baseline
- [agent-sdk](https://github.com/stephenpeters/agent-sdk) - Shared schemas and utilities
