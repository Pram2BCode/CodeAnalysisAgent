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
function activate(context) {
    const disposable = vscode.commands.registerCommand('codeAudit.runAnalysis', () => {
        runMainPy();
    });
    context.subscriptions.push(disposable);
}
exports.activate = activate;
/**
 * Deactivates the extension.
 */
function deactivate() {
    // Cleanup logic if needed
}
exports.deactivate = deactivate;
