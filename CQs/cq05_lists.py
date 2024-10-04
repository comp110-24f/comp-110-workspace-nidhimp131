"""Mutating functions."""

__author__ = "730671459"


def manual_append(list: list[int], new_value: int) -> None:
    list.append(new_value)


def double(list: list[int]) -> None:
    index = 0
    while index < len(list):
        list[index] = list[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list=list_2)

print(list_1)
print(list_2)
