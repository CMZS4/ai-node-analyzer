# AI Node Analyzer

AI-powered blockchain node log analyzer that detects sync failures, peer connectivity issues, and infrastructure bottlenecks.

---

## Features

- Detects peer connection failures
- Identifies blockchain sync stalls
- Flags disk space warnings
- Provides technical remediation suggestions
- Returns structured JSON output with severity levels

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

### Windows Quick Start

Tested on Windows with Git and Python installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/CMZS4/ai-node-analyzer.git
   cd ai-node-analyzer
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

5. Run:
   ```bash
   python app.py
   ```

---

## Usage

Place your node log file as:

```txt
node_log.txt
```

Run the analyzer:

```bash
python app.py
```

Results are saved to:

```txt
analysis_result.json
```

---

## Tech Stack

- Python
- OpenAI API
- python-dotenv

---

## Roadmap

- CLI arguments (`--input`, `--output`)
- Improved error handling
- Web dashboard (Streamlit)
- Docker support

---

Built for blockchain node operators and DevOps engineers.