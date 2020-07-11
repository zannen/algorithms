import mul

def test_mulPeasant():
    for a, b in [
        (99, 0),
        (1, 1),
        (11, 3),
        (23958233, 5830),
        (67548394032, 54325277),
    ]:
        assert mul.mulPeasant(a, b) == a * b
