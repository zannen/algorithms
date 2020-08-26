import json

import sort_parallel as sp


def subtest(n: int) -> None:
    unsorted_list = json.load(open("random_numbers_%09d_unsorted.json" % n))
    expected = json.load(open("random_numbers_%09d_sorted.json" % n))
    got = sp.sort_parallel(unsorted_list)
    assert got == expected, f"Failed to sort list length {n}"


def test_sort_parallel():
    for n in [
        10000,
        # 100000,
        # 1000000,
        # 10000000,
        # 100000000,
    ]:
        subtest(n)


def test_merge_sorted_lists():
    for lst1, lst2, expected in [
        ([], [], []),
        ([1], [], [1]),
        ([], [2], [2]),
        ([2], [1], [1, 2]),
        ([1, 2, 3, 10], [3, 4, 7], [1, 2, 3, 3, 4, 7, 10]),
    ]:
        got = sp.merge_sorted_lists(lst1, lst2)
        assert got == expected
