import os
import random
import time
from typing import Any, List


def timefunc(f, inf: str, *args, **kwargs):
    start = time.monotonic()
    result = f(*args, **kwargs)
    stop = time.monotonic()

    t = stop - start
    n = args[0]
    print("%9.4fs, N=%9d, %9.4fs per 10k. %s" % (t, n, 10000.0 * t / n, inf))
    return result


def generate_random_unsorted_list(n: int) -> List[int]:
    rand_upper_bound = n * 100
    return [random.randrange(rand_upper_bound) for _ in range(n)]


def write_list(n: int, thelist: List[Any], fn: str) -> None:
    with open(fn, "w") as fh:
        fh.write("[")
        fh.write(os.linesep)
        for i in range(len(thelist) - 1):
            fh.write(str(thelist[i]))
            fh.write(",")
            fh.write(os.linesep)
        fh.write(str(thelist[-1]))  # no comma after last
        fh.write(os.linesep)
        fh.write("]")
        fh.write(os.linesep)


def sort_list(n: int, thelist: List[Any]) -> List[Any]:
    return sorted(thelist)


def generate_list(n: int):
    unsorted_list = timefunc(
        generate_random_unsorted_list,
        "generate unsorted list of random numbers",
        n,
    )
    timefunc(
        write_list,
        "write unsorted list to file",
        n,
        unsorted_list,
        "random_numbers_%09d_unsorted.json" % n,
    )
    sorted_list = timefunc(sort_list, "sort list", n, unsorted_list)
    timefunc(
        write_list,
        "write sorted list to file",
        n,
        sorted_list,
        "random_numbers_%09d_sorted.json" % n,
    )


def main():
    for n in [
        10000,
        100000,
        1000000,
        10000000,
        # 100000000,
    ]:
        generate_list(n)
        print()


if __name__ == "__main__":
    main()
