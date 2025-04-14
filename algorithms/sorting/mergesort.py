def mergesort(arr, counter=None):
    if counter is None:
        counter = {"comparisons": 0}

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid], counter)
    right = mergesort(arr[mid:], counter)

    return merge(left, right, counter)

def merge(left, right, counter):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        counter["comparisons"] += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result