import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // Display a menu in the console
  console.log("Welcome to the Code Audit Tool Suite!");
  console.log("Available Commands:");
  console.log("1. Run Full Code Audit");
  console.log("2. Run Linter");
  console.log("3. Check for Security Issues");
  console.log("Use the Command Palette (Ctrl+Shift+P or Cmd+Shift+P) to execute these commands.");

  // Register the command for running a full code audit
  const runFullAudit = vscode.commands.registerCommand('codeAudit.runFullAudit', () => {
    console.log("Running Full Code Audit...");
    vscode.window.showInformationMessage('Running Full Code Audit...');
    // Add logic to invoke the full code audit tool
  });

  // Register the command for running the linter
  const runLinter = vscode.commands.registerCommand('codeAudit.runLinter', () => {
    console.log("Running Linter...");
    vscode.window.showInformationMessage('Running Linter...');
    // Add logic to invoke the linter tool
  });

  // Register the command for checking security issues
  const checkSecurityIssues = vscode.commands.registerCommand('codeAudit.checkSecurityIssues', () => {
    console.log("Checking for Security Issues...");
    vscode.window.showInformationMessage('Checking for Security Issues...');
    // Add logic to invoke the security scanning tool
  });

  // Add the commands to the context subscriptions
  context.subscriptions.push(runFullAudit, runLinter, checkSecurityIssues);
}

export function deactivate() {
  console.log("Deactivating Code Audit Tool Suite...");
}