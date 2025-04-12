# Import necessary libraries
import os  # Operating system functionalities, used here for environment variables
from dotenv import load_dotenv  # Library to load environment variables from a .env file

# Load environment variables from the .env file in the current directory
load_dotenv()

# Retrieve the Google API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Gemini model configuration
# GEMINI_MODEL_NAME = "gemini-1.5-pro"  # Specify the Gemini model to use
GEMINI_MODEL_NAME = "gemini-1.5-flash"  # Specify the Gemini model to use

GEMINI_TEMPERATURE = 0  # Set the temperature for response generation (0 for deterministic)

# Define the code review rules based on the README.md
# Each rule is a dictionary containing its ID, description, and expected behavior/outcome
RULES = [
    {
        "id": "CR001",
        "description": "Naming Conventions",
        "details": "Ensure consistent, meaningful, and compliant naming practices. Classes: PascalCase, functions/variables: snake_case, constants: UPPER_CASE (max 10 chars). Names must be descriptive and unambiguous."
    },
    {
        "id": "CR002",
        "description": "Secret & Credential Handling",
        "details": "Ensure sensitive data (e.g., API keys) is stored securely. No hardcoding; load from .env or secret managers."
    },
    {
        "id": "CR003",
        "description": "File & Folder Naming Structure",
        "details": "Ensure logical, readable, and scalable structure. Files: lowercase with underscores/dashes. Logical directory grouping. Avoid nesting > 3 levels."
    },
    {
        "id": "CR004",
        "description": "Code Formatting & Style",
        "details": "Ensure uniform code formatting. Use formatters (black/prettier), consistent indentation (Python: 4 spaces), line length 80-120 chars, no trailing spaces, proper line endings."
    },
    {
        "id": "CR005",
        "description": "Comments & Documentation",
        "details": "Ensure code is self-explanatory and documented. Function/class docstrings required. Inline comments for complex logic only. Avoid redundant comments."
    },
    {
        "id": "CR006",
        "description": "Error Handling",
        "details": "Ensure proper error handling. Catch specific exceptions, avoid bare 'except:', log errors with context, use try/except/finally for cleanup."
    },
    {
        "id": "CR007",
        "description": "Dependency Usage",
        "details": "Ensure dependencies are necessary, secure, and managed. Include manifest (requirements.txt), pin versions, remove unused dependencies."
    },
    {
        "id": "CR008",
        "description": "Input & Data Validation",
        "details": "Ensure external input is validated and sanitized. Check inputs for correctness/completeness/format, sanitize client data, use validation libraries/checks."
    },
    {
        "id": "CR009",
        "description": "Security Practices",
        "details": "Ensure adherence to security best practices. Avoid 'eval()' on user input, use HTTPS, secure CORS/headers, don't log sensitive info."
    },
    {
        "id": "CR010",
        "description": "Logging & Debugging Practices",
        "details": "Ensure efficient debugging and secure logging. Use proper logging levels, avoid 'print()' in production, don't log secrets."
    }
]

# Check if the API key was loaded successfully
if not GOOGLE_API_KEY:
    # Raise an error if the Google API key is not found in the environment variables
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in the .env file.")

