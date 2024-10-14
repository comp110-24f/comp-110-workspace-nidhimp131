"""Lesson 16 - Unit Tests"""


def get_first(input: list[str]) -> str:
    """Return first element."""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Remove first element."""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Return and remove first element."""
    first: str = input[0]
    input.pop(0)
    return first
