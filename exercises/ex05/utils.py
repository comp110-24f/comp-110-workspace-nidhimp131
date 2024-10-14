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
