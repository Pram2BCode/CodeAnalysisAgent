# Import necessary libraries
import json  # Library for JSON manipulation
from langchain_google_genai import ChatGoogleGenerativeAI  # LangChain integration for Google Gemini
from langchain.prompts import PromptTemplate  # LangChain class for creating prompt templates
from langchain.schema.output_parser import StrOutputParser  # LangChain parser for string output
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough  # LangChain components for running chains
from config import GOOGLE_API_KEY, RULES, GEMINI_MODEL_NAME, GEMINI_TEMPERATURE  # Import API key, rules, model name, and temperature from config.py
import os  # Library for interacting with the operating system

# Define the prompt template for analyzing a single rule
# This template instructs the AI on how to analyze the code for a specific rule
# and requests the output in a specific JSON format.
RULE_ANALYSIS_PROMPT_TEMPLATE = """
Analyze the following Python code based *only* on the rule provided.

Rule ID: {rule_id}
Rule Description: {rule_description}
Rule Details: {rule_details}

Python Code:
```python
{code}
```

Identify all lines where the rule is violated. For each violation, provide the line number, the specific issue, and a suggestion for fixing it.

If no violations are found for this rule, return an empty list.

Output ONLY a valid JSON list of violation objects, where each object has 'line', 'issue', and 'suggestion' keys. Example: [{{'line': 10, 'issue': 'Hardcoded secret', 'suggestion': 'Load from environment variable.'}}]
If no violations, output: []

JSON Violations:
"""

# Create a PromptTemplate object from the defined string template
prompt_template = PromptTemplate.from_template(RULE_ANALYSIS_PROMPT_TEMPLATE)

# Initialize the Google Generative AI model using the API key
# 'temperature=0' aims for deterministic and consistent output
llm = ChatGoogleGenerativeAI(model=GEMINI_MODEL_NAME, google_api_key=GOOGLE_API_KEY, temperature=GEMINI_TEMPERATURE)

# Define the LangChain chain for analyzing a single rule
# It sequences the prompt template, the LLM call, and an output parser
rule_chain = prompt_template | llm | StrOutputParser()

# Define individual agents for each rule using Gemini API

def agent_cr001(code_content):
    """Agent for CR001: Naming Conventions."""
    chain_input = {
        "rule_id": "CR001",
        "rule_description": "Naming Conventions",
        "rule_details": (
            "Ensure consistent, meaningful, and compliant naming practices. "
            "Classes must use PascalCase (e.g., UserManager, DataProcessor). "
            "Functions and variables must use snake_case (e.g., fetch_data, user_id). "
            "Constants must use UPPER_CASE and strictly not exceed 10 characters in length (e.g., MAX_COUNT). "
            "All names must be descriptive, unambiguous, and maintain uniformity throughout the codebase."
        ),
        "code": code_content
    }
    try:
        raw_output = rule_chain.invoke(chain_input)
        return parse_json_output(raw_output, "CR001")
    except Exception as e:
        print(f"Error invoking Gemini for CR001: {e}")
        return []

def agent_cr002(code_content):
    """Agent for CR002: Secret & Credential Handling."""
    chain_input = {
        "rule_id": "CR002",
        "rule_description": "Secret & Credential Handling",
        "rule_details": (
            "Detect any hardcoded secrets or credentials in the code, regardless of variable name. "
            "These may include API keys, access tokens, passwords, private keys, or secrets embedded in the code. "
            "Look for patterns like:\n"
            "- Strings that resemble secrets (e.g., long base64 strings, tokens, UUID-like strings) assigned to any variable.\n"
            "- Inline assignments such as `some_var = 'sk-abc123...'`, `password = '123456'`, or `token='eyJhbGciOiJIUzI1NiIs...'`\n"
            "- Usage of insecure loading like `open('secrets.txt')` or `read().decode()` without encryption.\n"
            "- Any logging or printing of potential secrets (e.g., `print(api_key)` or `logger.info('password: %s', pw)`)\n"
            "Acceptable usage includes loading secrets from environment variables, `.env` files, or secure secret managers.\n"
            "Examples of proper practices:\n"
            "- `API_KEY = os.getenv('API_KEY')`\n"
            "- Using `dotenv` or a secret manager library to fetch credentials securely.\n"
            "Flag any suspicious string literals that could contain secrets or sensitive values."
        ),
        "code": code_content
    }
    try:
        raw_output = rule_chain.invoke(chain_input)
        return parse_json_output(raw_output, "CR002")
    except Exception as e:
        print(f"Error invoking Gemini for CR002: {e}")
        return []

def agent_cr003(code_content):
    """Agent for CR003: File & Folder Naming Structure."""
    chain_input = {
        "rule_id": "CR003",
        "rule_description": "File & Folder Naming Structure",
        "rule_details": "Ensure logical, readable, and scalable structure. Files: lowercase with underscores/dashes. Logical directory grouping. Avoid nesting > 3 levels.",
        "code": code_content
    }
    try:
        raw_output = rule_chain.invoke(chain_input)
        return parse_json_output(raw_output, "CR003")
    except Exception as e:
        print(f"Error invoking Gemini for CR003: {e}")
        return []

def agent_cr004(code_content):
    """Agent for CR004: Code Formatting & Style."""
    chain_input = {
        "rule_id": "CR004",
        "rule_description": "Code Formatting & Style",
        "rule_details": "Ensure uniform code formatting. Use formatters (black/prettier), consistent indentation (Python: 4 spaces), line length 80-120 chars, no trailing spaces, proper line endings.",
        "code": code_content
    }
    try:
        raw_output = rule_chain.invoke(chain_input)
        return parse_json_output(raw_output, "CR004")
    except Exception as e:
        print(f"Error invoking Gemini for CR004: {e}")
        return []

def agent_cr005(code_content):
    """Agent for CR005: Comments & Documentation."""
    chain_input = {
        "rule_id": "CR005",
        "rule_description": "Comments & Documentation",
        "rule_details": "Ensure code is self-explanatory and documented. Function/class docstrings required. Inline comments for complex logic only. Avoid redundant comments.",
        "code": code_content
    }
    try:
        raw_output = rule_chain.invoke(chain_input)
        return parse_json_output(raw_output, "CR005")
    except Exception as e:
        print(f"Error invoking Gemini for CR005: {e}")
        return []

def agent_cr006(code_content):
    """Agent for CR006: Error Handling."""
    chain_input = {
        "rule_id": "CR006",
        "rule_description": "Error Handling",
        "rule_details": "Ensure proper error handling. Catch specific exceptions, avoid bare 'except:', log errors with context, use try/except/finally for cleanup.",
        "code": code_content
    }
    try:
        raw_output = rule_chain.invoke(chain_input)
        return parse_json_output(raw_output, "CR006")
    except Exception as e:
        print(f"Error invoking Gemini for CR006: {e}")
        return []

def agent_cr007(code_content):
    """Agent for CR007: Dependency Usage."""
    chain_input = {
        "rule_id": "CR007",
        "rule_description": "Dependency Usage",
        "rule_details": "Ensure dependencies are necessary, secure, and managed. Include manifest (requirements.txt), pin versions, remove unused dependencies.",
        "code": code_content
    }
    try:
        raw_output = rule_chain.invoke(chain_input)
        return parse_json_output(raw_output, "CR007")
    except Exception as e:
        print(f"Error invoking Gemini for CR007: {e}")
        return []

def agent_cr008(code_content):
    """Agent for CR008: Input & Data Validation."""
    chain_input = {
        "rule_id": "CR008",
        "rule_description": "Input & Data Validation",
        "rule_details": "Ensure external input is validated and sanitized. Check inputs for correctness/completeness/format, sanitize client data, use validation libraries/checks.",
        "code": code_content
    }
    try:
        raw_output = rule_chain.invoke(chain_input)
        return parse_json_output(raw_output, "CR008")
    except Exception as e:
        print(f"Error invoking Gemini for CR008: {e}")
        return []

def agent_cr009(code_content):
    """Agent for CR009: Security Practices."""
    chain_input = {
        "rule_id": "CR009",
        "rule_description": "Security Practices",
        "rule_details": "Ensure adherence to security best practices. Avoid 'eval()' on user input, use HTTPS, secure CORS/headers, don't log sensitive info.",
        "code": code_content
    }
    try:
        raw_output = rule_chain.invoke(chain_input)
        return parse_json_output(raw_output, "CR009")
    except Exception as e:
        print(f"Error invoking Gemini for CR009: {e}")
        return []

def agent_cr010(code_content):
    """Agent for CR010: Logging & Debugging Practices."""
    chain_input = {
        "rule_id": "CR010",
        "rule_description": "Logging & Debugging Practices",
        "rule_details": "Ensure efficient debugging and secure logging. Use proper logging levels, avoid 'print()' in production, don't log secrets.",
        "code": code_content
    }
    try:
        raw_output = rule_chain.invoke(chain_input)
        return parse_json_output(raw_output, "CR010")
    except Exception as e:
        print(f"Error invoking Gemini for CR010: {e}")
        return []

# Update analyze_code to include all agents
def analyze_code(code_content: str):
    """Analyzes the code content against all defined rules using individual agents."""
    analysis_results = {}
    for rule in RULES:
        rule_id = rule["id"]
        if rule_id == "CR001":
            violations = agent_cr001(code_content)
        elif rule_id == "CR002":
            violations = agent_cr002(code_content)
        elif rule_id == "CR003":
            violations = agent_cr003(code_content)
        elif rule_id == "CR004":
            violations = agent_cr004(code_content)
        elif rule_id == "CR005":
            violations = agent_cr005(code_content)
        elif rule_id == "CR006":
            violations = agent_cr006(code_content)
        elif rule_id == "CR007":
            violations = agent_cr007(code_content)
        elif rule_id == "CR008":
            violations = agent_cr008(code_content)
        elif rule_id == "CR009":
            violations = agent_cr009(code_content)
        elif rule_id == "CR010":
            violations = agent_cr010(code_content)
        else:
            violations = []  # Placeholder for other rules

        if violations:
            analysis_results[rule_id] = {
                "description": rule["description"],
                "violations": violations
            }

    return analysis_results

# Function to parse the JSON output from the AI model
# Handles potential errors during JSON parsing
def parse_json_output(output_string: str, rule_id: str):
    """Parses the JSON string output from the LLM for a rule.

    Args:
        output_string: The string output received from the LLM.
        rule_id: The ID of the rule being analyzed (for error context).

    Returns:
        A list of violation dictionaries, or an empty list if parsing fails or output is empty.
    """
    try:
        # Attempt to remove potential markdown code block fences before parsing
        cleaned_output = output_string.strip().removeprefix('```json').removesuffix('```').strip()
        # Handle empty or placeholder outputs
        if not cleaned_output or cleaned_output == '[]':
            return [] # Return empty list if no violations
        # Parse the cleaned string as JSON
        violations = json.loads(cleaned_output)
        # Basic validation: ensure it's a list
        if isinstance(violations, list):
            return violations # Return the list of violations
        else:
            # Log if the parsed JSON is not a list
            print(f"Warning: Unexpected JSON format for rule {rule_id}. Expected list, got {type(violations)}. Output: {output_string}")
            return [] # Return empty list on unexpected format
    except json.JSONDecodeError:
        # Log if JSON parsing fails
        print(f"Error: Could not decode JSON for rule {rule_id}. Raw output: {output_string}")
        return [] # Return empty list on parsing error
    except Exception as e:
        # Log any other unexpected errors during parsing
        print(f"Error parsing output for rule {rule_id}: {e}. Raw output: {output_string}")
        return [] # Return empty list on other errors

# Function to create an annotated version of the code
def annotate_code(code_content: str, analysis_results: dict):
    """Adds comments to the code indicating rule violations.

    Args:
        code_content: The original code content string.
        analysis_results: The dictionary containing analysis results from analyze_code.

    Returns:
        A string containing the original code with added violation comments.
    """
    # Split the code into lines for easier annotation
    lines = code_content.splitlines()
    # Create a dictionary to hold annotations, mapping line numbers to lists of comments
    annotations = {}

    # Iterate through each rule's results in the analysis
    for rule_id, result in analysis_results.items():
        # Iterate through each violation found for the current rule
        for violation in result.get("violations", []):
            # Get the line number (adjusting for 0-based indexing)
            line_num = violation.get("line")
            # Ensure line number is valid
            if line_num is not None and 1 <= line_num <= len(lines):
                # Adjust to 0-based index for list access
                line_idx = line_num - 1
                # Format the annotation comment
                comment = f"# REVIEW [{rule_id}]: {violation.get('issue', 'N/A')} -> SUGGESTION: {violation.get('suggestion', 'N/A')}"
                # Add the comment to the annotations dictionary for the corresponding line
                if line_idx not in annotations:
                    annotations[line_idx] = []  # Initialize list if not present
                annotations[line_idx].append(comment)  # Append the comment

    # Build the annotated code string
    annotated_lines = []
    # Iterate through the original lines with their indices
    for i, line in enumerate(lines):
        # Append the original line
        annotated_lines.append(line)
        # If there are annotations for this line index, append them
        if i in annotations:
            # Add each annotation comment on a new line, indented like the original line
            indentation = " " * (len(line) - len(line.lstrip(' ')))
            for comment in annotations[i]:
                annotated_lines.append(indentation + comment)

    # Join the lines back into a single string and return
    return "\n".join(annotated_lines)

def scan_directory_structure(base_path):
    """
    Recursively scans the directory structure and categorizes files.

    Args:
        base_path (str): The root directory to scan.

    Returns:
        dict: A dictionary mapping categories to lists of files.
    """
    structure = {
        'code_files': [],
        'config_files': [],
        'data_files': [],
        'log_files': [],
        'test_files': [],
        'other_files': []
    }

    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(('.py', '.js', '.java', '.cpp')):
                structure['code_files'].append(file_path)
            elif file.endswith(('.json', '.yaml', '.yml', '.ini', '.cfg')):
                structure['config_files'].append(file_path)
            elif file.endswith(('.csv', '.xls', '.xlsx', '.txt')):
                structure['data_files'].append(file_path)
            elif file.endswith(('.log', '.out')):
                structure['log_files'].append(file_path)
            elif 'test' in file.lower():
                structure['test_files'].append(file_path)
            else:
                structure['other_files'].append(file_path)

    return structure

def validate_best_practices(directory_structure):
    """
    Validates the directory structure against best practices.

    Args:
        directory_structure (dict): The categorized directory structure.

    Returns:
        dict: A dictionary of validation results.
    """
    validation_results = {
        'naming_conventions': [],
        'modularity': [],
        'essential_files': [],
        'redundancies': [],
        'test_placement': []
    }

    # Validate naming conventions
    for category, files in directory_structure.items():
        for file in files:
            if ' ' in file or '-' in file:
                validation_results['naming_conventions'].append(f"File '{file}' has invalid naming conventions.")

    # Validate presence of essential files
    essential_files = ['README.md', '.gitignore', 'requirements.txt']
    for essential in essential_files:
        if not any(essential in file for file in directory_structure['other_files']):
            validation_results['essential_files'].append(f"Missing essential file: {essential}")

    # Validate modularity and test placement
    for file in directory_structure['test_files']:
        if not file.startswith('tests/'):
            validation_results['test_placement'].append(f"Test file '{file}' is not in the 'tests/' directory.")

    return validation_results

def generate_improvement_suggestions(validation_results):
    """
    Generates actionable improvement suggestions based on validation results.

    Args:
        validation_results (dict): The results from best practices validation.

    Returns:
        list: A list of improvement suggestions.
    """
    suggestions = []

    for category, issues in validation_results.items():
        for issue in issues:
            if "invalid naming conventions" in issue:
                suggestions.append(f"{issue} /// Rename the file to follow snake_case or PascalCase naming conventions.")
            elif "Missing essential file" in issue:
                suggestions.append(f"{issue} /// Create the missing file and include necessary content.")
            elif "not in the 'tests/' directory" in issue:
                suggestions.append(f"{issue} /// Move the test file to a 'tests/' directory.")

    return suggestions

def write_detailed_results_to_file(results, output_file):
    """
    Writes detailed and user-friendly results to a specified text file.

    Args:
        results (dict): The results to write.
        output_file (str): The path to the output file.
    """
    with open(output_file, 'w') as f:
        f.write("Analysis Results\n")
        f.write("=" * 50 + "\n\n")

        for category, issues in results.items():
            f.write(f"Category: {category.upper()}\n")
            f.write("-" * 50 + "\n")

            if not issues:
                f.write("No issues found in this category.\n\n")
            else:
                for issue in issues:
                    f.write(f"  - {issue}\n")

            f.write("\n")

        f.write("End of Analysis\n")
        f.write("=" * 50 + "\n")

# Update the PlannerAgent to generate a detailed results file
class PlannerAgent:
    """
    The Planner Agent is responsible for breaking down tool ideas into modular tasks,
    identifying dependencies, and prioritizing tasks for development.
    """

    def __init__(self, tool_ideas):
        """
        Initialize the Planner Agent with a list of tool ideas.

        Args:
            tool_ideas (list): A list of tool ideas to be decomposed and prioritized.
        """
        self.tool_ideas = tool_ideas
        self.tasks = []

    def decompose_tools(self):
        """
        Decompose each tool idea into smaller, modular tasks.

        Returns:
            list: A list of decomposed tasks.
        """
        for tool in self.tool_ideas:
            self.tasks.append({
                "tool": tool,
                "subtasks": [
                    f"Research best practices for {tool}",
                    f"Design architecture for {tool}",
                    f"Implement core functionality for {tool}",
                    f"Write tests for {tool}",
                    f"Integrate {tool} into CLI/API",
                    f"Document usage of {tool}"
                ]
            })
        return self.tasks

    def identify_dependencies(self):
        """
        Identify dependencies between tasks.

        Returns:
            dict: A dictionary mapping tasks to their dependencies.
        """
        dependencies = {}
        for task in self.tasks:
            tool = task["tool"]
            if tool in ["Security Vulnerability Scanner", "Dependency Visualizer"]:
                dependencies[tool] = ["Code Smell Detector"]
            elif tool in ["Test Coverage Heatmap", "Style Consistency Enforcer"]:
                dependencies[tool] = ["Multi-language Linter Aggregator"]
            else:
                dependencies[tool] = []
        return dependencies

    def prioritize_tasks(self):
        """
        Prioritize tasks based on dependencies and importance.

        Returns:
            list: A prioritized list of tasks.
        """
        dependencies = self.identify_dependencies()
        prioritized = []
        while self.tasks:
            for task in self.tasks:
                tool = task["tool"]
                if all(dep in prioritized for dep in dependencies[tool]):
                    prioritized.append(tool)
                    self.tasks.remove(task)
        return prioritized

    def generate_detailed_results(self, output_file):
        """
        Generate a detailed results file with decomposed tasks, dependencies, and prioritized tasks.

        Args:
            output_file (str): The path to the output file.
        """
        decomposed_tasks = self.decompose_tools()
        dependencies = self.identify_dependencies()
        prioritized_tasks = self.prioritize_tasks()

        with open(output_file, 'w') as f:
            f.write("Detailed Tool Planning Results\n")
            f.write("=" * 50 + "\n\n")

            f.write("Decomposed Tasks:\n")
            for task in decomposed_tasks:
                f.write(f"- Tool: {task['tool']}\n")
                for subtask in task['subtasks']:
                    f.write(f"  - {subtask}\n")
                f.write("\n")

            f.write("Dependencies:\n")
            for tool, deps in dependencies.items():
                f.write(f"- {tool}: {', '.join(deps) if deps else 'None'}\n")
            f.write("\n")

            f.write("Prioritized Tasks:\n")
            for task in prioritized_tasks:
                f.write(f"- {task}\n")

            f.write("\nEnd of Detailed Results\n")

# Example usage
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Check file structure best practices")
        print("2. Check folder structure best practices and security vulnerabilities")
        print("3. Plan tool development")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            base_path = input("Enter the path to analyze: ")
            directory_structure = scan_directory_structure(base_path)
            validation_results = validate_best_practices(directory_structure)
            output_file = os.path.join(base_path, 'analysis_results.txt')
            write_detailed_results_to_file(validation_results, output_file)
            print(f"Detailed results written to {output_file}")

        elif choice == '2':
            print("Folder structure security checks are not yet implemented.")

        elif choice == '3':
            tool_ideas = [
                "Code Smell Detector",
                "Dependency Visualizer",
                "Complexity Analyzer",
                "API Contract Verifier",
                "Dead Code Finder",
                "Git History Insights",
                "License Compliance Checker",
                "Performance Bottleneck Analyzer",
                "Security Vulnerability Scanner",
                "Test Coverage Heatmap",
                "Style Consistency Enforcer",
                "TODO/Comment Tracker",
                "Refactor Suggestion Engine",
                "Build Time Analyzer",
                "Code Duplication Detector",
                "Tech Debt Dashboard",
                "Multi-language Linter Aggregator",
                "Code Comment Quality Checker",
                "Access Control Auditor",
                "Merge Conflict Risk Predictor",
                "Review Readiness Checker",
                "Annotated Architecture Map",
                "Legacy Code Detector",
                "Open Resource Tracker",
                "i18n Audit Tool"
            ]

            planner = PlannerAgent(tool_ideas)
            tasks = planner.decompose_tools()
            dependencies = planner.identify_dependencies()
            prioritized_tasks = planner.prioritize_tasks()

            print("Decomposed Tasks:", tasks)
            print("Dependencies:", dependencies)
            print("Prioritized Tasks:", prioritized_tasks)

            output_file = "tool_planning_results.txt"
            planner.generate_detailed_results(output_file)
            print(f"Detailed tool planning results written to {output_file}")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

