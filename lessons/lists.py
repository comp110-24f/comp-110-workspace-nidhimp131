"""Basic syntax of lists."""

my_name: str = str()  # constructor
my_name: str = ""  # literal

# Create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor


# Add items to list
my_numbers.append(1.5)
my_numbers.append(1.5)

# Create an already populated list
game_points: list[int] = [102, 86, 94]

# Subscription notation/indexing
game_points[2]
last_game: int = game_points[2]  # Accesses value and saves as a variable

# Modify by index
game_points[1] = 72  # Changes the value at index 1 to 72

# Length of a list
len(game_points)

# Remove items from list
game_points.pop(1)  # Removes the value at index 1 (72)

# Practice


def display(list1: list[int]) -> None:
    index: int = 0
    while index < len(list1):
        print(list1[index])
        index += 1


# display(list1=game_points)
