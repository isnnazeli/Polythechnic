def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a


numbers = [34, 4, 56, 32, 85, 1, 98]
print(selection_sort(numbers))