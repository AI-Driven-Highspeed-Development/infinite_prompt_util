"""
Infinite Prompt Utility - TUI for agent continuation prompts.

Provides a beautiful terminal UI using Rich that allows users to:
- Press Ctrl+C to stop the agent
- Type additional instructions to continue

Usage (agent calls directly):
    python -m utils.infinite_prompt_util.infinite_prompt

Output format:
    STOP              - User pressed Ctrl+C
    CONTINUE:<text>   - User wants to continue, optional instruction after colon
"""

from utils.infinite_prompt_util.infinite_prompt import prompt_for_next_action

__all__ = ["prompt_for_next_action"]
