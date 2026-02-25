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
node_log.txt (or use the sample in examples/node_log.sample.txt)
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
## Example Files

Sample files are included in the `examples/` directory:

- `examples/node_log.sample.txt`
- `examples/analysis_result.sample.json`
---

## CLI Usage Examples

Run with default paths:

```bash
python app.py

Run with a custom input file: 
python app.py --input examples/node_log.sample.txt

Run with a custom output file:

python app.py --input examples/node_log.sample.txt --output examples/custom_result.json

Troubleshooting
OPENAI_API_KEY is missing

Create a .env file in the project root and add:

OPENAI_API_KEY=your_api_key_here

Log file not found

Make sure the input path exists, or use:

python app.py --input path/to/your/node_log.txt

JSON parsing failed

Sometimes model output may not be valid JSON. In that case, the raw response is saved to:

raw_model_output.txt

You can inspect it and retry with a shorter or cleaner log input.




