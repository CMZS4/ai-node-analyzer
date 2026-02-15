import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("node_log.txt", "r") as file:
    log_data = file.read()

system_prompt = """
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
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": log_data}
    ],
    temperature=0
)

analysis_text = response.choices[0].message.content

print("\nRaw AI Output:\n")
print(analysis_text)

try:
    parsed = json.loads(analysis_text)
    issues = parsed.get("issues", [])

    print("\nStructured Issues:\n")

    for issue in issues:
        print(f"Title: {issue['title']}")
        print(f"Severity: {issue['severity']}")
        print(f"Explanation: {issue['technical_explanation']}")
        print(f"Fix: {issue['recommended_fix']}")
        print("-" * 50)

    # ✅ JSON FILE EXPORT
    with open("analysis_result.json", "w") as outfile:
        json.dump(parsed, outfile, indent=4)

    print("\n✅ Results saved to analysis_result.json")

except Exception as e:
    print("\n⚠ JSON parsing failed.")
    print("Error:", e)
