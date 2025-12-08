# infinite_prompt_util

Type: util

A beautiful TUI utility for AI agent continuation prompts using Rich.

## Purpose

This utility provides a terminal UI that allows users to control AI agent execution flow:
- **Press Ctrl+C** to stop the agent
- **Type instructions** to continue with additional context

## Installation

```bash
pip install rich
```

## Usage

Agent runs the script directly and reads the terminal output:

```bash
python -m utils.infinite_prompt_util.infinite_prompt
```

### Output Format

The last line of output will be one of:
- `STOP` - User pressed Ctrl+C
- `CONTINUE:<instruction>` - User wants to continue, instruction after colon (may be empty)

### Example Output

```
┌─────────────────── ✦ Agent Checkpoint ✦ ───────────────────┐
│                                                             │
│  ⏸  Press Ctrl+C to stop the agent                         │
│  ▶  Or type instructions below to continue                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
→ Enter instruction: fix the bug in main.py
CONTINUE:fix the bug in main.py
```
