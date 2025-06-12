def bubble_sort(nums: list[int]) -> None:
    size = len(nums)
    i = 0
    j = 1
    iter = 0

    while iter < size - 1:
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

        i += 1
        j += 1

        if j == (size - iter):
            iter += 1
            i = 0
            j = 1
