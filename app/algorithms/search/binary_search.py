def binary_search(nums: list[int], target: int) -> int | None:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid: int = (start + end) // 2
        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            start = mid + 1

        if target < nums[mid]:
            end = mid - 1

    return None
