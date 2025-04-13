# Code Audit Tool Suite

## Overview
The Code Audit Tool Suite is a simple VS Code extension that triggers the execution of `main.py` whenever the user presses Ctrl+C+V. This functionality is designed to streamline workflows by allowing quick execution of the main script.

## Features
- **Trigger Script Execution**: Automatically runs `main.py` when Ctrl+C+V is pressed.
- **Custom Keybinding**: The extension binds the command to Ctrl+C+V for ease of use.

## Installation
1. Download the `.vsix` file from this repository.
2. Open Visual Studio Code.
3. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar.
4. Click on the `...` menu in the Extensions view and select `Install from VSIX...`.
5. Select the `code-audit-tool-suite-0.1.0.vsix` file to install the extension.

## Usage
1. Open any project in Visual Studio Code.
2. Press `Ctrl+C+V` (or `Cmd+C+V` on macOS) to trigger the execution of `main.py`.
3. View the output in the terminal.

## Development
1. Clone this repository.
2. Install dependencies using `npm install`.
3. Compile the TypeScript code using `npm run compile`.
4. Press `F5` in VS Code to launch a new Extension Development Host.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
