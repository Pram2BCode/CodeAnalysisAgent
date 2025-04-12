import os
import json
import requests
from dotenv import load_dotenv

# Explicitly load the .env file from the config directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../config/.env'))

# Initialize Gemini API key and URL
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL")
if not GEMINI_API_KEY or not GEMINI_API_URL:
    raise ValueError("Gemini API key or URL is not set in the environment variables.")

# Rule-based analysis agents
class NamingConventionAgent:
    def analyze(self, file_content):
        violations = []
        lines = file_content.splitlines()
        for i, line in enumerate(lines, start=1):
            if "class " in line and not line.split()[1][0].isupper():
                violations.append({
                    "line": i,
                    "issue": "Class name not in PascalCase",
                    "suggestion": "Rename to PascalCase."
                })
        return {"rule_id": "CR001", "violations": violations}

class SecretHandlingAgent:
    def analyze(self, file_content):
        violations = []
        lines = file_content.splitlines()
        for i, line in enumerate(lines, start=1):
            if "API_KEY" in line and "os.getenv" not in line:
                violations.append({
                    "line": i,
                    "issue": "Hardcoded API key",
                    "suggestion": "Use os.getenv('API_KEY') instead."
                })
        return {"rule_id": "CR002", "violations": violations}

class GeminiAnalysisAgent:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def analyze(self, file_content):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {"code": file_content}

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            analysis = response.json()
            return {
                "rule_id": "AI001",
                "violations": analysis.get("violations", [])
            }
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Gemini API: {e}")
            return {"rule_id": "AI001", "violations": []}

# Main analysis function
def analyze_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return

    with open(file_path, "r") as file:
        file_content = file.read()

    agents = [
        NamingConventionAgent(),
        SecretHandlingAgent(),
        GeminiAnalysisAgent(GEMINI_API_KEY, GEMINI_API_URL)
    ]
    analysis_summary = []

    for agent in agents:
        analysis_summary.append(agent.analyze(file_content))

    # Ensure the reports directory exists
    os.makedirs("reports", exist_ok=True)

    # Generate JSON report
    report = {
        "file_name": os.path.basename(file_path),
        "analysis_summary": analysis_summary
    }

    output_path = os.path.join("reports", "analysis_report.json")
    with open(output_path, "w") as report_file:
        json.dump(report, report_file, indent=4)

    print(f"Analysis complete. Report saved to {output_path}.")

# Entry point
def main():
    file_path = input("Enter the path to the Python file to analyze: ").strip()
    analyze_file(file_path)

if __name__ == "__main__":
    main()