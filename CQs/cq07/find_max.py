"""Challenge Question Seven"""

__author__ = "730671459"


def find_and_remove_max(input: list[int]) -> int:
    """Finds and removes all instances of the largest value in a list of integers."""
    if input == []:  # If list is empty
        return -1
    index = 1
    max: int = input[0]
    while index < len(input):  # Determines max value
        if input[index] > max:
            max = input[index]
            index += 1
        else:
            index += 1
    idx = len(input) - 1
    while idx >= 0:  # Removes each instance of max value
        if input[idx] == max:
            input.pop(idx)
            idx -= 1
        else:
            idx -= 1
    return max  # Returns max value
