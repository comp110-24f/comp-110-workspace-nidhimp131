"""Exercise Five - List Unit Tests: Utility Functions"""

__author__ = "730671459"


def only_evens(input: list[int]) -> list[int]:
    """Returns a list containing only even items."""
    index = 0
    evens: list[int] = []  # Creates an empty list that is modified and returned.
    while index < len(input):
        if input[index] % 2 == 1:  # When item is odd, continue to next item.
            index += 1
        else:
            evens.append(input[index])  # When item is even, add to evens list.
            index += 1
    return evens


def sub(full_list: list[int], num1: int, num2: int) -> list[int]:
    """Returns a subset of inputted list from num1 to num2."""
    subset: list[int] = []  # Creates an empty list that is modified and returned.
    index = num1
    if num1 < 0:  # Index begins at zero if num1 is less than zero.
        index = 0
    while index < num2 and index < len(
        full_list
    ):  # Adds items to list until index reaches num2 or end of list.
        subset.append(full_list[index])
        index += 1
    return subset


def add_at_index(input: list[int], element: int, idx: int) -> None:
    """Given a list, adds an integer at a particular index."""
    if idx < 0 or idx > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)  # Increases the length of the list to fit the new item.
    index = (
        len(input) - 1
    )  # Starts from the end of the list so items before idx remain unchanged.
    while index > idx:  # Moves each item after idx one place to the right
        input[index] = input[index - 1]
        index -= 1
    input[idx] = element  # Adds element at idx
