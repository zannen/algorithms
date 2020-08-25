import timeit

import fibonacci as f


def generate_fib2function(n):
    def wibble():
        return f.fib2(n)
    return wibble


def generate_fib3function(n):
    def wibble():
        return f.fib3(n)
    return wibble


if __name__ == "__main__":

    iterations = 1
    while True:
        t = timeit.timeit(generate_fib2function(40), number=iterations)
        if t < 0.5:
            iterations <<= 1
        else:
            break
    print(
        f"fib#1: iterations = {iterations}, total_time = {t}, time per "
        "iteration = {t/iterations}")

    iterations = 1
    while True:
        t = timeit.timeit(generate_fib3function(40), number=iterations)
        if t < 0.5:
            iterations <<= 1
        else:
            break
    print(
        f"fib#2: iterations = {iterations}, total_time = {t}, time per "
        "iteration = {t/iterations}")
