import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


INPUT_LOG_FILE = Path("node_log.txt")
OUTPUT_JSON_FILE = Path("analysis_result.json")
MODEL_NAME = "gpt-4o-mini"


def build_system_prompt() -> str:
    return """
You are a senior blockchain infrastructure engineer.

Analyze the provided node log and return a structured JSON response in this exact format:
{
  "issues": [
    {
      "title": "",
      "severity": "Critical | Warning | Info",
      "technical_explanation": "",
      "recommended_fix": ""
    }
  ]
}

Return ONLY valid JSON.
""".strip()


def load_log_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Log file not found: {path}")

    content = path.read_text(encoding="utf-8").strip()

    if not content:
        raise ValueError("Log file is empty.")

    return content


def analyze_log(client: OpenAI, log_data: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": build_system_prompt()},
            {"role": "user", "content": log_data},
        ],
        temperature=0,
    )
    return response.choices[0].message.content or ""


def print_issues(parsed: dict) -> None:
    issues = parsed.get("issues", [])

    print("\nStructured Issues:\n")

    if not issues:
        print("No issues found in parsed output.")
        return

    for issue in issues:
        print(f"Title: {issue.get('title', 'N/A')}")
        print(f"Severity: {issue.get('severity', 'N/A')}")
        print(f"Explanation: {issue.get('technical_explanation', 'N/A')}")
        print(f"Fix: {issue.get('recommended_fix', 'N/A')}")
        print("-" * 50)


def save_results(parsed: dict, output_path: Path) -> None:
    output_path.write_text(json.dumps(parsed, indent=4), encoding="utf-8")
    print(f"\n✅ Results saved to {output_path}")


def main() -> int:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY is missing. Add it to your .env file.")
        return 1

    try:
        log_data = load_log_file(INPUT_LOG_FILE)
    except FileNotFoundError as e:
        print(f"❌ {e}")
        return 1
    except ValueError as e:
        print(f"⚠ {e}")
        return 1

    client = OpenAI(api_key=api_key)

    try:
        analysis_text = analyze_log(client, log_data)
    except Exception as e:
        print("❌ OpenAI request failed.")
        print("Error:", e)
        return 1

    print("\nRaw AI Output:\n")
    print(analysis_text)

    try:
        parsed = json.loads(analysis_text)
    except json.JSONDecodeError as e:
        print("\n⚠ JSON parsing failed.")
        print("Error:", e)

        Path("raw_model_output.txt").write_text(analysis_text, encoding="utf-8")
        print("📝 Raw output saved to raw_model_output.txt")
        return 1

    print_issues(parsed)
    save_results(parsed, OUTPUT_JSON_FILE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())