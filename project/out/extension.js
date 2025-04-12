"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const vscode = __importStar(require("vscode"));
function activate(context) {
    // Register the command for running a full code audit
    const runFullAudit = vscode.commands.registerCommand('codeAudit.runFullAudit', () => {
        vscode.window.showInformationMessage('Running Full Code Audit...');
        // Add logic to invoke the full code audit tool
    });
    // Register the command for running the linter
    const runLinter = vscode.commands.registerCommand('codeAudit.runLinter', () => {
        vscode.window.showInformationMessage('Running Linter...');
        // Add logic to invoke the linter tool
    });
    // Register the command for checking security issues
    const checkSecurityIssues = vscode.commands.registerCommand('codeAudit.checkSecurityIssues', () => {
        vscode.window.showInformationMessage('Checking for Security Issues...');
        // Add logic to invoke the security scanning tool
    });
    // Add the commands to the context subscriptions
    context.subscriptions.push(runFullAudit, runLinter, checkSecurityIssues);
}
exports.activate = activate;
function deactivate() {
    // Cleanup logic if needed
}
exports.deactivate = deactivate;
