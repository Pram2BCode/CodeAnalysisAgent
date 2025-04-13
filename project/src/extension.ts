import * as vscode from 'vscode';

/**
 * Executes the main.py script and logs the output to the VS Code terminal.
 */
function runMainPy() {
  const terminal = vscode.window.createTerminal('Code Analysis');
  terminal.show();
  terminal.sendText('python3 /workspaces/CodeAnalysisAgent/project/main.py');
}

/**
 * Activates the extension and registers the command.
 * @param context - The extension context provided by VS Code.
 */
export function activate(context: vscode.ExtensionContext) {
  const disposable = vscode.commands.registerCommand('codeAudit.runAnalysis', () => {
    runMainPy();
  });

  context.subscriptions.push(disposable);
}

/**
 * Deactivates the extension.
 */
export function deactivate() {
  // Cleanup logic if needed
}