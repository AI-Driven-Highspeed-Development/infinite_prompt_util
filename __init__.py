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

# Add path handling to work from the new nested directory structure
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.getcwd()  # Use current working directory as project root
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.infinite_prompt_util.infinite_prompt import prompt_for_next_action

__all__ = ["prompt_for_next_action"]
