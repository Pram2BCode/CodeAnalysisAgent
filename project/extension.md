# How to Use the Code Audit Tool Suite Extension

## Overview
The Code Audit Tool Suite is a lightweight VS Code extension that triggers the execution of `main.py` whenever Ctrl+C+V is pressed. This guide provides a step-by-step process to install, configure, and use the extension effectively.

---

## Installation

### Step 1: Download the Extension
1. Locate the `code-audit-tool-suite-0.1.0.vsix` file in this repository.
2. Ensure you have Visual Studio Code installed on your system.

### Step 2: Install the Extension
1. Open Visual Studio Code.
2. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
3. Click on the `...` menu in the Extensions view and select `Install from VSIX...`.
4. Navigate to the location of the `code-audit-tool-suite-0.1.0.vsix` file and select it.
5. Wait for the installation to complete. You should see a confirmation message.

---

## Usage

### Step 1: Activate the Extension
The extension activates automatically when you open a project in Visual Studio Code.

### Step 2: Trigger the Command
1. Press `Ctrl+C+V` (or `Cmd+C+V` on macOS) to execute `main.py`.
2. The output of the script will be displayed in the terminal.

---

## Features

### Keybinding
- The extension binds the execution of `main.py` to the key combination Ctrl+C+V (or Cmd+C+V on macOS).

---

## Development

### Modify the Extension
1. Clone this repository.
2. Install dependencies using `npm install`.
3. Compile the TypeScript code using `npm run compile`.
4. Press `F5` in VS Code to launch a new Extension Development Host.

---

## Troubleshooting

### Common Issues
- **Extension not activating**: Ensure the `.vsix` file is installed correctly.
- **No output in terminal**: Check if the keybinding is working properly.

For further assistance, refer to the README file or contact the repository maintainer.