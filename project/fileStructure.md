# 📁 File Structure Analysis Agent – Requirements

## 🧠 Objective

Design and implement an **intelligent agent** capable of scanning the file and folder structure of a **user-provided codebase directory**, evaluating it against **best practices**, and generating a **comprehensive report** that outlines structural issues, suggestions for improvement, and optionally fixes.

This agent will be fully integrated into the existing **agentic framework** and should reuse or adapt the current **project stack and architecture**.

---

## 🏗️ Key Features

### ✅ 1. **Directory Structure Scanning**
- Recursively walk through all folders and files.
- Identify code files, config files, data files, logs, tests, etc.
- Map out the hierarchy and categorize contents.

### ✅ 2. **Best Practices Validation**
- Validate:
  - File and folder naming conventions.
  - Directory modularity (e.g., separating `src`, `tests`, `docs`, `configs`).
  - Presence of essential files (`README.md`, `.gitignore`, `requirements.txt` or `package.json`, etc.)
  - Redundancies or deeply nested structures.
  - Test folder placements and naming.
  - Duplication of file types or logic groups.

### ✅ 3. **Improvement Suggestions**
- Provide actionable, structured suggestions for:
  - Renaming or relocating files/folders.
  - Flattening or modularizing hierarchy.
  - Splitting large folders.
  - Creating missing documentation or config files.
- Suggestions should be clear and follow this format:  
  ```python
  some_folder/some_file.py  ///{code}/// Move this file into 'src/' and follow snake_case naming convention ///
