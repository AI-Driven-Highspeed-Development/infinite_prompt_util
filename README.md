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

### Basic Usage

```python
from utils.infinite_prompt_util import prompt_for_next_action

response = prompt_for_next_action()

if response.should_stop:
    print("Agent stopped by user")
elif response.should_continue:
    if response.instruction:
        print(f"Continue with: {response.instruction}")
    else:
        print("Continue with no additional instructions")
```

### Loop Mode

```python
from utils.infinite_prompt_util import run_infinite_prompt_loop

def process_instruction(instruction: str | None):
    if instruction:
        print(f"Processing: {instruction}")

# Run until user presses Ctrl+C
instructions = run_infinite_prompt_loop(task_callback=process_instruction)
print(f"Session ended with {len(instructions)} instructions")
```

## API

### `prompt_for_next_action(title, stop_message, continue_message) -> InfinitePromptResponse`

Display a single prompt and return the user's response.

### `run_infinite_prompt_loop(task_callback, title) -> list[str]`

Run a continuous loop until user presses Ctrl+C.

### `InfinitePromptResponse`

- `result`: `PromptResult.STOP` or `PromptResult.CONTINUE`
- `instruction`: Optional string with user's instruction
- `should_stop`: Boolean property
- `should_continue`: Boolean property
