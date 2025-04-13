# Code Analysis Agent

## Overview
The Code Analysis Agent is a comprehensive tool designed to streamline the process of auditing and analyzing codebases. It provides developers with insights into code quality, security vulnerabilities, maintainability, and dependency management. This repository includes a VS Code extension, "Code Audit Tool Suite," which integrates these features directly into the developer's workflow.

## Features
- **Code Linting**: Ensures adherence to coding standards using tools like ESLint for JavaScript/TypeScript and Flake8 for Python.
- **Security Scanning**: Identifies potential vulnerabilities using Bandit for Python and `npm audit` for JavaScript/TypeScript.
- **Code Readability and Maintainability**: Analyzes code complexity and provides recommendations for improvement.
- **Dependency Analysis**: Checks for outdated or vulnerable dependencies.
- **AI Code Reviewer**: (Optional) Leverages AI to provide feedback on code quality and improvements.
- **Customizable Rulesets**: Allows users to configure rules for linting and scanning.

## Repository Structure
- `analyzer.py`: Core logic for analyzing code files.
- `config.py`: Configuration settings for the analysis tools.
- `main.py`: Entry point for running the analysis.
- `test_analyzer.py`: Unit tests for the analyzer.
- `src/extension.ts`: Source code for the VS Code extension.
- `code-audit-tool-suite-0.1.0.vsix`: Packaged VS Code extension file.

## Using the VS Code Extension
### Installation
1. Download the `.vsix` file from this repository.
2. Open Visual Studio Code.
3. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar.
4. Click on the `...` menu in the Extensions view and select `Install from VSIX...`.
5. Select the `code-audit-tool-suite-0.1.0.vsix` file to install the extension.

### Usage
1. Open a project in Visual Studio Code.
2. Use the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS) to access the following commands:
   - **Run Full Code Audit**: Executes all analysis tools.
   - **Run Linter**: Runs the linter for your project.
   - **Check for Security Issues**: Scans your project for vulnerabilities.
3. View results in the Output panel or the custom sidebar panel (if configured).
4. Check the console for detailed logs and a menu of available commands.

## Development
To modify or extend this repository:
1. Clone the repository.
2. Install dependencies using `npm install` (for the extension) and `pip install -r requirements.txt` (for Python tools).
3. Use `npm run compile` to compile the TypeScript code for the extension.
4. Press `F5` in VS Code to launch a new Extension Development Host.

## Future Plans
- Enhance AI-based code review capabilities.
- Add support for additional programming languages.
- Integrate more advanced security scanning tools.
- Provide detailed reports in multiple formats (e.g., JSON, HTML).

## License
This project is licensed under the MIT License. See the LICENSE file for details.
