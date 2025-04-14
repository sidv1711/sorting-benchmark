# algorithms/sorting/quicksort.py

def quicksort(arr, counter=None):
    if counter is None:
        counter = {"comparisons": 0}

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left, middle, right = [], [], []

    for x in arr:
        counter["comparisons"] += 1
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quicksort(left, counter) + middle + quicksort(right, counter)