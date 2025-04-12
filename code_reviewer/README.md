# Comprehensive Technical PRD: Code Review Analysis System

---

## Project Overview

The Code Review Analysis System leverages agents and APIs to analyze Python code files against predefined rules. The system provides detailed JSON reports and annotated code files with recommendations, streamlining the review process using Google Gemini APIs the easy way.

---

## Project Requirements Document: Python Code Review Analysis

| **Requirement ID** | **Description** | **User Story** | **Expected Behavior/Outcome** |
|---------------------|-----------------|----------------|--------------------------------|
| **CR001** | **Naming Conventions** | As a user, I want to ensure consistent, meaningful, and compliant naming practices across all code elements to enhance readability and maintenance. | The system should verify the following: Classes use PascalCase (e.g., `UserManager`, `DataProcessor`), functions and variables use snake_case (e.g., `fetch_data()`, `user_id`), and constants use UPPER_CASE with a maximum length of 10 characters (e.g., `MAX_COUNT`, avoid overly long names like `DEFAULT_TIMEOUT`). All names should be descriptive, unambiguous, and maintain uniformity throughout the codebase. |
| **CR002** | **Secret & Credential Handling** | As a user, I want to ensure sensitive data (e.g., API keys) is stored securely to avoid unauthorized access and data leaks. | The system should confirm that sensitive credentials are never hardcoded (e.g., `API_KEY = 'abc123'` is not acceptable), secrets are loaded from external `.env` files (e.g., `API_KEY = os.getenv('API_KEY')` is recommended), and in cloud deployments, secrets are managed using secret management tools like AWS Secrets Manager or Azure Key Vault. |
| **CR003** | **File & Folder Naming Structure** | As a user, I want to ensure that files and folders follow a logical, readable, and scalable structure for long-term project manageability. | The system should validate that files use lowercase with underscores or dashes (e.g., `data_utils.py`, `user-service/`), directory organization follows logical groupings by feature or domain, and excessively nested folders (more than three levels) are avoided. |
| **CR004** | **Code Formatting & Style** | As a user, I want to ensure uniform code formatting for better team collaboration and readability. | The system should check adherence to standards, such as using automated formatters like `black` or `prettier`, maintaining consistent indentation (Python: 4 spaces; JavaScript/TypeScript: 2 spaces), limiting line lengths to 80–120 characters, removing trailing spaces, and ensuring proper line endings. |
| **CR005** | **Comments & Documentation** | As a user, I want to ensure the code is self-explanatory and sufficiently documented for future maintenance. | The system should verify that function and class docstrings are provided in clear, descriptive language (e.g., Python docstring style: `"""Retrieves a user by ID"""`), inline comments explain complex logic only, redundant or trivial comments are avoided, and documentation aligns with team or industry standards. |
| **CR006** | **Error Handling** | As a user, I want to ensure error scenarios are addressed properly to avoid crashes or unpredictable behavior. | The system should confirm that specific exceptions are caught (e.g., `except ValueError:` is preferred over bare exceptions), bare `except:` blocks are avoided as they can mask issues, errors are logged with contextual details for debugging, and proper use of `try/except/finally` blocks for resource cleanup is implemented. |
| **CR007** | **Dependency Usage** | As a user, I want to ensure that third-party dependencies are necessary, secure, and properly managed. | The system should check that the project includes manifest files like `requirements.txt` or `package.json`, dependency versions are pinned (e.g., `flask==2.2.3`), and unused or unnecessary dependencies are removed to reduce bloat. |
| **CR008** | **Input & Data Validation** | As a user, I want to ensure all external input is validated and sanitized to prevent security risks. | The system should validate that all inputs are checked for correctness, completeness, and format, client-provided data is sanitized to prevent injection attacks, and validation libraries or in-code checks are in place. |
| **CR009** | **Security Practices** | As a user, I want to ensure the code adheres to best practices to minimize vulnerabilities. | The system should confirm that dangerous constructs like `eval()` are avoided on user data (e.g., `eval(user_input)` is unsafe), HTTPS is used for all external API communications, proper CORS configurations and secure headers are applied, and sensitive information like passwords or API tokens are not logged. |
| **CR010** | **Logging & Debugging Practices** | As a user, I want to ensure efficient debugging while keeping sensitive information secure. | The system should check that proper logging levels (e.g., `logging.info()`, `logging.error()`) are used based on the situation, `print()` statements are avoided in production code, and secrets or sensitive data are not written to logs. |

---

## Implementation Details

1. **Input Collection**:
   - User provides the name of the code file to test.
   - System checks the file's existence in the current directory.

2. **Rule-Based Analysis**:
   - Each rule (e.g., naming conventions, security checks) is handled by an independent agent.
   - Agents process the file using LangChain workflows and Google Gemini API for advanced code evaluation.

3. **Output Generation**:
   - JSON Report: Includes details such as rule ID, description, violations, and recommendations.
   - Annotated Code: A modified copy of the original file with comments pointing out violations and fixes.

4. **Automation Workflow**:
   - Agents dynamically allocate tasks based on rule categories.
   - LangChain coordinates tasks, while Gemini API performs the actual analysis.

---

## Output Formats

### JSON Report
```json
{
    "file_name": "sample_code.py",
    "analysis_summary": [
        {
            "rule_id": "CR001",
            "violations": [
                {"line": 12, "issue": "Class name not in PascalCase", "suggestion": "Rename to UserManager"}
            ]
        },
        {
            "rule_id": "CR002",
            "violations": [
                {"line": 45, "issue": "Hardcoded API key", "suggestion": "Use os.getenv('API_KEY')"}
            ]
        }
    ]
}
```
