# MergeSort in ascending order
def merge(left, right):
    result = []
    i, j = 0, 0
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    # if anything is left in the left array
    result = result + left[i:]
    # if anything is left in the right array
    result = result + right[j:]
    return result

def mergeSort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left = mergeSort(array[:mid])
        right = mergeSort(array[mid:])
        return merge(left, right)