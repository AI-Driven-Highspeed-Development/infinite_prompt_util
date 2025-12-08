"""
Infinite Prompt TUI - Beautiful terminal UI for agent continuation prompts.

This utility provides a TUI that allows users to either:
- Press Ctrl+C to stop the agent
- Type additional instructions to continue

Uses the `rich` library for beautiful terminal output.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.style import Style


class PromptResult(Enum):
    """Result type from the infinite prompt."""
    STOP = "stop"
    CONTINUE = "continue"


@dataclass
class InfinitePromptResponse:
    """Response from the infinite prompt TUI."""
    result: PromptResult
    instruction: str | None = None

    @property
    def should_stop(self) -> bool:
        """Check if the agent should stop."""
        return self.result == PromptResult.STOP

    @property
    def should_continue(self) -> bool:
        """Check if the agent should continue."""
        return self.result == PromptResult.CONTINUE


def prompt_for_next_action(
    title: str = "Agent Checkpoint",
    stop_message: str = "Press Ctrl+C to stop the agent",
    continue_message: str = "Or type instructions below to continue",
) -> InfinitePromptResponse:
    """
    Display a beautiful TUI prompt asking user for next action.

    Args:
        title: Title to display in the panel header
        stop_message: Message explaining how to stop
        continue_message: Message explaining how to continue

    Returns:
        InfinitePromptResponse with result type and optional instruction
    """
    console = Console()

    # Build the prompt panel content
    content = Text()
    content.append("⏸  ", style=Style(color="yellow", bold=True))
    content.append(stop_message, style=Style(color="yellow"))
    content.append("\n")
    content.append("▶  ", style=Style(color="cyan", bold=True))
    content.append(continue_message, style=Style(color="cyan"))

    # Display the panel
    panel = Panel(
        content,
        title=f"[bold magenta]✦ {title} ✦[/bold magenta]",
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

        if instruction.strip():
            return InfinitePromptResponse(
                result=PromptResult.CONTINUE,
                instruction=instruction.strip(),
            )
        else:
            # Empty input - ask again or treat as continue with no instruction
            console.print(
                "[dim]Empty input - continuing with no additional instructions[/dim]"
            )
            return InfinitePromptResponse(
                result=PromptResult.CONTINUE,
                instruction=None,
            )

    except KeyboardInterrupt:
        console.print()
        console.print("[bold red]✋ Agent stopped by user[/bold red]")
        return InfinitePromptResponse(result=PromptResult.STOP)


def run_infinite_prompt_loop(
    task_callback: callable | None = None,
    title: str = "Agent Checkpoint",
) -> list[str]:
    """
    Run a loop that repeatedly prompts for instructions until stopped.

    Args:
        task_callback: Optional callback that receives each instruction.
                      Signature: callback(instruction: str | None) -> None
        title: Title to display in the prompt panel

    Returns:
        List of all instructions provided during the session
    """
    console = Console()
    instructions: list[str] = []

    console.print()
    console.print(
        "[bold bright_blue]═══════════════════════════════════════[/bold bright_blue]"
    )
    console.print(
        "[bold bright_blue]       Infinite Prompt Mode Active      [/bold bright_blue]"
    )
    console.print(
        "[bold bright_blue]═══════════════════════════════════════[/bold bright_blue]"
    )

    while True:
        response = prompt_for_next_action(title=title)

        if response.should_stop:
            break

        if response.instruction:
            instructions.append(response.instruction)

        if task_callback:
            task_callback(response.instruction)

    console.print()
    console.print(f"[dim]Session ended. {len(instructions)} instruction(s) provided.[/dim]")

    return instructions
