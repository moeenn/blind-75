from functools import lru_cache


@lru_cache(maxsize=128)
def factorial(n: int) -> int:
    if n == 0:
        return 1

    return n * factorial(n - 1)


def factorial_tail_optimized(n: int, accum: int = 1) -> int:
    if n == 0:
        return accum

    return factorial_tail_optimized(n - 1, accum * n)
