from typing import Generator


def loop(nums: list[int]) -> Generator[int]:
    i = 0

    def inner(data: list[int]) -> Generator[int]:
        if not data:
            return

        yield data[i]
        yield from inner(data[i + 1 :])

    yield from inner(nums[:])
