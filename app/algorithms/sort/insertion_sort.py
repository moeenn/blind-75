def insertion_sort(nums: list[int]) -> None:
    def swap(a: int, b: int) -> None:
        nums[a], nums[b] = nums[b], nums[a]

    def position_left(key_index: int) -> None:
        if key_index == 0:
            return

        for i in range(key_index - 1, -1, -1):
            if nums[i] > nums[key_index]:
                swap(i, key_index)
                position_left(key_index - 1)

    for key_index in range(1, len(nums)):
        position_left(key_index)
