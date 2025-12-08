"""
Infinite Prompt TUI - Beautiful terminal UI for agent continuation prompts.

This utility provides a TUI that allows users to either:
- Press Ctrl+C to stop the agent
- Type additional instructions to continue

Uses the `rich` library for beautiful terminal output.

Usage:
    python -m utils.infinite_prompt_util.infinite_prompt
"""

from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.style import Style


def prompt_for_next_action() -> None:
    """
    Display a TUI prompt asking user for next action.
    
    Outputs to stdout:
    - "STOP" if user pressed Ctrl+C
    - "CONTINUE:" followed by instruction if user typed something
    - "CONTINUE:" with empty instruction if user pressed Enter
    
    Agent reads the terminal output to determine next action.
    """
    console = Console()

    # Build the prompt panel content
    content = Text()
    content.append("⏸  ", style=Style(color="yellow", bold=True))
    content.append("Press Ctrl+C to stop the agent", style=Style(color="yellow"))
    content.append("\n")
    content.append("▶  ", style=Style(color="cyan", bold=True))
    content.append("Or type instructions below to continue", style=Style(color="cyan"))

    # Display the panel
    panel = Panel(
        content,
        title="[bold magenta]✦ Agent Checkpoint ✦[/bold magenta]",
        border_style="bright_blue",
        padding=(1, 2),
    )
    console.print()
    console.print(panel)

    try:
        # Get user input
        instruction = Prompt.ask(
            "[bold green]→[/bold green] [dim]Enter instruction[/dim]",
            default="",
            show_default=False,
        )

        # Output in parseable format for agent
        print(f"CONTINUE:{instruction.strip()}")

    except KeyboardInterrupt:
        console.print()
        console.print("[bold red]✋ Agent stopped by user[/bold red]")
        print("STOP")


if __name__ == "__main__":
    prompt_for_next_action()
