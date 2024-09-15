"""Calculates the cost and items needed to throw a tea party."""

__author__ = "730671459"


def main_planner(guests: int) -> None:
    """Prints tea party plan."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Determines the number of tea bags needed for a particular number of guests."""
    return people * 2  # Multiplies number of people by 2.


def treats(people: int) -> int:
    """Determines the number of treats needed based on number of teas."""
    return int(tea_bags(people=people) * 1.5)  # Multiplies number of tea bags by 1.5.


def cost(tea_count: int, treat_count: int) -> float:
    """Determines total cost of tea bags and treats."""
    return (tea_count * 0.50) + (
        treat_count * 0.75
    )  # Multiplies numbers of items by their assigned dollar amounts.


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party?"))
    )  # Asks for a number of guests as input.
