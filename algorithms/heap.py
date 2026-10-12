def heapify(a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)


def heap_sort(a):
    n = len(a)

    # build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    # move the biggest to the end, then fix the heap
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

    return a


numbers = [43, 65, 78, 3, 99, 7, 90 ,5]
print(heap_sort(numbers))