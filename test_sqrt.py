import math

import sqrt as s


def test_sqrt():
    tolerance = 0.1

    test_numbers = [
        0,
        1,
        4,
        9,
        16,
        25,
        36,
        49,
        64,
        81,
        100,
        # ok, now for the difficult ones
        2,
        5,
    ]
    for n in test_numbers:
        got = s.sqrt(n)
        expected = math.sqrt(n)
        if got == expected:
            # exact match. probably a square number.
            continue

        # check with tolerance
        lbound = expected * (1.0 - tolerance)
        ubound = expected * (1.0 + tolerance)
        assert lbound < got and got < ubound, \
            f"Calculating sqrt({n}), failed: {lbound} < {got} < {ubound}"
