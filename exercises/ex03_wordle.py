"""Exercise Three - Wordle Game -- TEST"""

__author__ = "730671459"


def input_guess(secret_word_len: int) -> str:
    """Checks that guessed word is five characters long."""
    guess = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:  # If guess doesn't have 5 chars.
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess  # Once guess has 5 chars.


def contains_char(secret_word: str, guessed_char: str) -> bool:
    """Checks if a character is found in the secret word."""
    assert len(guessed_char) == 1
    index = 0  # Starts with first character of word.
    match: bool = False  # Unless match is found, return False.
    while index < len(secret_word):
        if secret_word[index] == guessed_char:
            match = True  # If match is found, return True.
        index += 1  # Moves to next character.
    return match


def emojified(secret_word1: str, guessed_word: str) -> str:
    """Compares guessed word to secret word."""
    assert len(guessed_word) == len(secret_word1)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    emoji: list[str] = []
    while index < len(secret_word1):
        if guessed_word[index] == secret_word1[index]:  # If characters match
            emoji += GREEN_BOX
        elif (
            (contains_char(secret_word=secret_word1, guessed_char=guessed_word[index]))
            and (guessed_word[index] != secret_word1[index - 1])
            and (guessed_word[index] != secret_word1[index - 2])
            and (guessed_word[index] != secret_word1[index - 3])
            and (guessed_word[index] != secret_word1[index - 4])
        ):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        index += 1
    return str(f"{emoji[0]}{emoji[1]}{emoji[2]}{emoji[3]}{emoji[4]}")


def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns_taken = 1
    win_status = False
    while (
        turns_taken <= 6 and not win_status
    ):  # Allows six turns or until game has been won.
        print(f"=== Turn {turns_taken}/6 ===")  # Title
        guess = input_guess(
            secret_word_len=len(secret_word)
        )  # Allows user to guess word.
        print(
            emojified(
                secret_word1=secret_word,
                guessed_word=guess,
            )
        )  # Prints matching characters from word.
        if secret_word == guess:  # If game has been won.
            win_status = True
        turns_taken += 1
    if win_status:  # If game has been won.
        print(f"You won in {turns_taken-1}/6 turns!")
    else:  # If game is not won in six turns.
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")
