import mul

def test_mulPeasant():
    for a, b, expected in [
        (99, 0, 0),
        (1, 1, 1),
        (11, 3, 33),
        (23958233, 5830, 139676498390),
        (67548394032, 54325277, 3669585216693546864),
    ]:
        assert mul.mulPeasant(a, b) == expected
