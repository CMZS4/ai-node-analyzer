# AI Node Analyzer

AI-powered blockchain node log analyzer that detects sync failures, peer connectivity issues, and infrastructure bottlenecks.

---

## Features

- Detects peer connection failures
- Identifies blockchain sync stalls
- Flags disk space warnings
- Provides technical remediation suggestions

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Usage

Place your node log file as:

```
node_log.txt
```

Run the analyzer:

```bash
python app.py
```

---

## Tech Stack

- Python
- OpenAI API
- python-dotenv

---

## Roadmap

- Severity scoring
- JSON export
- Web dashboard (Streamlit)
- Docker support

---

Built for blockchain node operators and DevOps engineers.
