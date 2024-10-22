"""Challenge Question Seven - Test"""

__author__ = "730671459"


from CQs.cq07.find_max import find_and_remove_max  # type: ignore


def test_find_and_remove_max_return_value() -> None:
    """Tests that function returns the correct value."""
    values: list[int] = [2, 4, 7, 1, 3, 8, 1]
    assert find_and_remove_max(values) == 8


def test_find_and_remove_max_mutation() -> None:
    """Tests that function removes each instance of max value."""
    values: list[int] = [2, 4, 6, 8, 8, 1, 3, 8, 2]
    find_and_remove_max(values)
    assert values == [2, 4, 6, 1, 3, 2]


def test_find_and_remove_max_empty_input() -> None:
    """Tests that function returns -1 when input is an empty list."""
    values: list[int] = []
    assert find_and_remove_max(values) == -1
