"""
Infinite Prompt Utility - TUI for agent continuation prompts.

Provides a beautiful terminal UI using Rich that allows users to:
- Press Ctrl+C to stop the agent
- Type additional instructions to continue
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.getcwd()
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.infinite_prompt_util.infinite_prompt import (
    PromptResult,
    InfinitePromptResponse,
    prompt_for_next_action,
    run_infinite_prompt_loop,
)

__all__ = [
    "PromptResult",
    "InfinitePromptResponse",
    "prompt_for_next_action",
    "run_infinite_prompt_loop",
]
