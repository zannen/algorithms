from typing import Tuple


def div(a: int, b: int) -> Tuple[int, int]:
    """
    Calculate:
    - a / b
    - a % b
    """

    d = 0
    while a >= 0:
        x = 0
        while b << x <= a:
            x += 1
        x -= 1
        if x < 0:
            break
        d += 1 << x
        a -= b << x

    return d, a
