# Extension Instructions

## Overview
The Code Audit Tool Suite is a comprehensive VS Code extension designed to help developers audit their code for linting, security issues, maintainability, and dependency analysis. It supports Python, JavaScript, and TypeScript projects.

## Features
- **Linting**: Run ESLint for JavaScript/TypeScript and Flake8 for Python.
- **Security Scanning**: Use Bandit for Python and `npm audit` for JavaScript/TypeScript.
- **Code Readability and Maintainability**: Analyze code complexity and maintainability.
- **Dependency Analysis**: Check for outdated or vulnerable dependencies.
- **AI Code Reviewer**: (Optional) Get AI-based feedback on your code.

## Installation
1. Clone this repository or download the `.vsix` file.
2. Open Visual Studio Code.
3. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
4. Click on the `...` menu in the Extensions view and select `Install from VSIX...`.
5. Select the `.vsix` file to install the extension.

## Usage
### Step 1: Activate the Extension
The extension activates automatically when you open a supported project (Python, JavaScript, or TypeScript).

### Step 2: Run Commands
Use the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS) to access the following commands:
- **Run Full Code Audit**: Runs all tools (linting, security scanning, etc.) in one go.
- **Run Linter**: Runs the linter for your project.
- **Check for Security Issues**: Scans your project for security vulnerabilities.

### Step 3: View Results
- Results are displayed in the Output panel or a custom sidebar panel (if configured).
- Status bar feedback shows the audit status (e.g., "Audit Passed" or number of issues).

## Configuration
You can configure the extension by editing your VS Code settings (`File > Preferences > Settings` or `Cmd+,` on macOS):
- **Enable/Disable Tools**: Choose which tools to run.
- **Rulesets**: Configure rules for linters and scanners.
- **Output Format**: Select between summary or detailed output.

## Development
To modify or extend this extension:
1. Clone this repository.
2. Run `npm install` to install dependencies.
3. Use `npm run compile` to compile the TypeScript code.
4. Press `F5` in VS Code to launch a new Extension Development Host.

## License
This project is licensed under the MIT License. See the LICENSE file for details.