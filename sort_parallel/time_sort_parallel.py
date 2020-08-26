import json
import timeit

import sort_parallel as sp


def time_sort_parallel(n: int) -> None:
    unsorted_list = json.load(open("random_numbers_%09d_unsorted.json" % n))

    def sort_internal():
        sorted(unsorted_list)

    def sort_parallel():
        sp.sort_parallel(unsorted_list)

    t = timeit.timeit(sort_internal, number=1)
    print(
        "%9.4fs, N=%9d, %9.4fs per 10k. Sort internal"
        % (t, n, 10000.0 * t / n)
    )
    t = timeit.timeit(sort_parallel, number=1)
    print(
        "%9.4fs, N=%9d, %9.4fs per 10k. Sort parallel"
        % (t, n, 10000.0 * t / n)
    )


if __name__ == "__main__":
    for n in [
        10000,
        100000,
        1000000,
        10000000,
        100000000,
    ]:
        time_sort_parallel(n)
