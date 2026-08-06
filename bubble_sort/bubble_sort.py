def bubble_sort(unsorted: list) -> None:
    length = len(unsorted) - 1
    for i in range(length):
        for j in range(length - i):
            if j + 1 > length:
                continue
            left = unsorted[j]
            right = unsorted[j + 1]
            if left > right:
                temp = left
                unsorted[j] = unsorted[j + 1]
                unsorted[j + 1] = temp


test = [2, 4, 0, 1]

bubble_sort(test)

print(test)
