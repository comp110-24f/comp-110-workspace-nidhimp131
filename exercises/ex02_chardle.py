"""Determines the location of individual characters within a five-letter word."""

__author__ = "730671459"


def input_word() -> str:
    """Receives a five-character word as input and checks length."""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:  # If word entered is not 5 characters long.
        print("Error: Word must contain 5 characters.")
        exit()  # Does not allow user to continue.
    return word


def input_letter() -> str:
    """Receives a single character input and checks length."""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:  # If more than one character is entered
        print("Error: Character must be a single character.")
        exit()  # Does not allow user to continue.
    return letter


def contains_char(word: str, letter: str) -> None:
    """Checks if inputted letter is found at each index of the inputted word."""
    print("Searching for " + letter + " in " + word)
    num_matching: int = 0  # Number of matching characters
    if word[0] == letter:  # Checks if letter is found at index 0.
        print(letter + " found at index 0")
        num_matching = num_matching + 1  # Increases number by one.
    if word[1] == letter:
        print(letter + " found at index 1")
        num_matching = num_matching + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        num_matching = num_matching + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        num_matching = num_matching + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        num_matching = num_matching + 1
    if num_matching == 0:  # Prints number of matching characters.
        print("No instances of " + letter + " found in " + word)
    if num_matching != 0:  # Prints number of matching characters.
        print(str(num_matching) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Calls the contains_char function."""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
