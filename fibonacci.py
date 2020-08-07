

# horribly slow recursive implementation
def fib1(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n-1) + fib1(n-2)


# better implementation: build a list
def fib2(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    fibseq = [0, 1]
    while len(fibseq) <= n:
        fibseq.append(fibseq[-1] + fibseq[-2])
    return fibseq[-1]


# best implementation: don't build a list
def fib3(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev = 1
    prevprev = 0
    while n > 1:
        new = prevprev + prev
        prevprev = prev
        prev = new
        n -= 1
    return new
