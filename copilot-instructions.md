# Copilot Instructions for AI Coding Agents

## Project Overview
This is a minimal Python project focused on simple file I/O and user input. The main script is `files.py`, which collects a user's name and a secret, then opens (but does not write to) `myfile.txt` in append mode.

## Key Files
- `files.py`: Main entry point. Handles user input and file operations.
- `launch.json`: VS Code debug configuration for running the current Python file with the integrated terminal.

## Developer Workflows
- **Run/Debug**: Use the VS Code debugger with the provided `launch.json` configuration (`Python Debugger: Current File`).
- **Manual Run**: Execute `files.py` directly in the terminal:  
  `python files.py`

## Patterns & Conventions
- All user input is collected via `input()` calls.
- File operations use Python's built-in `open()` function. Currently, files are opened in append mode but no data is written.
- Output and error handling are minimal; expand as needed for more complex workflows.

## Integration Points
- No external dependencies or packages are used.
- All data is stored locally in `myfile.txt` (created if not present).

## Example Workflow
1. Run `files.py`.
2. Enter a name and a secret when prompted.
3. The script opens `myfile.txt` in append mode (no data is written yet).

## Recommendations for AI Agents
- If expanding functionality, follow the pattern of using `input()` for user interaction and `open()` for file operations.
- Document any new conventions or workflows in this file for future agents.
- Reference `launch.json` for debugging setup.

---
_If any section is unclear or incomplete, please provide feedback to improve these instructions._
