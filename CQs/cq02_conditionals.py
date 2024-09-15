"""Conditionals Challenge Question"""

__author__ = "730671459"


def guess_a_number() -> None:
    secret: int = 7
    x: int = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x == secret:  # If guess is correct
        print("You got it!")
    elif x < secret:  # If guess is too low
        print("Your guess was too low! The secret number is " + str(secret))
    else:  # If guess is too high
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
