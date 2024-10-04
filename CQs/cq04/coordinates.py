"""Challenge Question Four - Coordinates"""

__author__ = "730671459"


def get_coords(xs: str, ys: str) -> None:
    xindex: int = 0
    while xindex < len(xs):
        yindex: int = 0
        while yindex < len(ys):
            print(f"({xs[xindex]},{ys[yindex]})")
            yindex += 1
        xindex += 1
