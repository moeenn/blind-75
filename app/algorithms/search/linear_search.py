def linear_search(nums: list[int], target: int) -> int | None:
    for index, n in enumerate(nums):
        if n == target:
            return index
