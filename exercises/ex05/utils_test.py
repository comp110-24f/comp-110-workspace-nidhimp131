"""Exercise Five - List Unit Tests: Unit Tests"""

__author__ = "730671459"


from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_use_1() -> None:
    """Tests that function returns correct list."""
    input1: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert only_evens(input1) == [2, 4, 6]


def test_only_evens_use_2() -> None:
    """Tests that function returns correct list."""
    input2: list[int] = [2, 4, 6, 3, 5, 7]
    assert only_evens(input2) == [2, 4, 6]


def test_only_evens_edge_case() -> None:
    """Tests that function returns an empty list when no even numbers are present."""
    input3: list[int] = [1, 3, 5, 7]
    assert only_evens(input3) == []


def test_sub_use_1() -> None:
    """Tests that function generates correct subset of inputted list."""
    input1: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(input1, 2, 4) == [3, 4]


def test_sub_use_2() -> None:
    """Tests that correct list is returned when start and end are outside of the list's bounds."""
    input1: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(input1, -2, 23) == [1, 2, 3, 4, 5, 6, 7]


def test_sub_empty_list() -> None:
    """Tests that function returns empty list when start value is greater than length of list."""
    input1: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(input1, 23, 26) == []


def test_add_at_index_use_1() -> None:
    """Tests that function adds value at correct index."""
    input1: list[int] = [1, 2, 3, 4, 5, 6, 7]
    add_at_index(input1, 10, 3)  # Runs the function
    assert input1 == [1, 2, 3, 10, 4, 5, 6, 7]  # Checks that inputted list is modified


def test_add_at_index_use_2() -> None:
    """Tests that function adds value at correct index."""
    input2: list[int] = [1, 5, 2, 67, 12]
    add_at_index(input2, 1, 1)
    assert input2 == [1, 1, 5, 2, 67, 12]


def test_add_at_index_index_out_of_bounds() -> None:
    """Tests that error is raised when index is out of bound for the inputted list."""
    input1: list[int] = [1, 2, 3, 4, 5, 6, 7]
    with pytest.raises(IndexError):
        add_at_index(input1, 10, 13)
