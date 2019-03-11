from math import copysign as copysign_f


def copysign(x, y) -> int:
    return int(copysign_f(x, y))
