def selection_sort(nums: list[int]) -> None:
    size = len(nums)

    def get_min_index(start: int) -> int:
        min_i = start
        for i in range(start + 1, size):
            if nums[i] < nums[min_i]:
                min_i = i

        return min_i

    for start in range(size):
        min_index = get_min_index(start)
        nums[start], nums[min_index] = nums[min_index], nums[start]
