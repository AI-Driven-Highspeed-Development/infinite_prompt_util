---
applyTo: "**/*"
---

# Infinite Prompt Instructions

## Goals
- Ensure AI agents check with the user before stopping.
- Allow users to provide additional instructions to continue the workflow.
- Prevent premature agent termination.

## Rules

1. **Before Stopping**: Before completing your task and stopping, you MUST run the infinite prompt TUI to check if the user wants to continue with additional instructions.

2. **How to Run**: Use the `infinite_prompt_util` to prompt the user:
```python
from utils.infinite_prompt_util import prompt_for_next_action

response = prompt_for_next_action()
if response.should_continue:
    # Process response.instruction if provided
    pass
elif response.should_stop:
    # User pressed Ctrl+C - safe to stop
    pass
```

3. **When to Skip**: You may skip the infinite prompt ONLY when:
   - The user explicitly said "stop", "exit", "quit", or similar termination commands.
   - A critical error occurred that prevents continuation.
   - The user is in discussion-only mode.

4. **User Control**: The user can:
   - Press `Ctrl+C` to stop the agent.
   - Type additional instructions to continue working.
   - Press Enter with empty input to continue with no additional instructions.
