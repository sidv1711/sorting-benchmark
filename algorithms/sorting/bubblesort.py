def bubblesort(arr, counter=None):
    if counter is None:
        counter = {"comparisons": 0}

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            counter["comparisons"] += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr