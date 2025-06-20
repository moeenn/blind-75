def merge(a: list[int], b: list[int]) -> list[int]:
    result: list[int] = []
    i = 0
    j = 0

    while True:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

        if i == len(a):
            result += b[j:]
            break

        if j == len(b):
            result += a[i:]
            break

    return result


def merge_sort(nums: list[int]) -> list[int]:
    size = len(nums)

    chunks: list[list[int]] = []
    for n in nums:
        chunks.append([n])

    result = chunks[0]
    for i in range(size - 1):
        result = merge(result, [i])

    return result
