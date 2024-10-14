"""Exercise Four - List Utility Functions"""

__author__ = "730671459"


def all(input: list[int], number: int) -> bool:
    index = 0
    all_ints_match: bool = True
    if len(input) == 0:  # Returns false if list is empty
        all_ints_match = False
    while index < len(input):
        if input[index] == number:  # If number matches list at index, return True.
            index += 1
        else:  # If number does not match list at index, return False.
            all_ints_match = False
            index += 1
    return all_ints_match


def max(input: list[int]) -> int:
    if len(input) == 0:  # Empty list results in an error.
        raise ValueError("max() arg is an empty List")
    index = 1
    max_value: int = input[0]  # Sets the largest value to the first index of the list.
    while index < len(input):  # Compares each item to the current max value.
        if input[index] > max_value:
            max_value = input[index]
            index += 1
        else:
            index += 1
    return max_value


def is_equal(input1: list[int], input2: list[int]) -> bool:
    equality: bool = True
    if len(input1) != len(input2):  # If the lists are different lengths, return False.
        equality = False
    else:
        index = 0
        while index < len(input1):
            if (
                input1[index] != input2[index]
            ):  # If the values at a particular index do not match, return False.
                equality = False
                index += 1
            else:
                index += 1
    return equality


def extend(a: list[int], b: list[int]) -> None:
    index = 0
    while index < len(
        b
    ):  # Cycles through each item of list b and appends it to list a.
        a.append(b[index])
        index += 1
