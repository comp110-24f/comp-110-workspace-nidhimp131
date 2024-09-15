"""Practicing conditionals."""


def less_than_10(num: int) -> bool:
    """Tell us if num < 10."""
    if num < 10:
        return True
    else:
        return False


print(less_than_10(num=2))


# Modified version
# def less_than_10(num: int) -> bool:
#   """Tell us if num < 10."""
#  dub: int = num * 2  # 14
# dub = dub - 1  # 13
# print(dub)
# if num < 10:
#   return True
# else:
#   return False


print(less_than_10(num=2))


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up!"
    else:
        return "Keep sleeping."


print(wake_up(alarm=True))


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter is first character of word."""
    if word[0] == letter[0]:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))


def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if (weather == "rainy") or (weather == "cold"):
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather
