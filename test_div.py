import div

def test_div():
    for a, b in [
    	(0, 1234),
    	(9, 10),
    	(10, 10),
    	(11, 10),
        (1729, 10),
        (5673892567438593, 5465),
    ]:
        d, m = div.div(a, b)
        assert d == int(a / b)
        assert m == a % b
