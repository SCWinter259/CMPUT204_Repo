from MergeSort import mergeSort
from quickSort import quickSort

array = [3, 5, 2, 10, 4, 8, 9]

# test for merge sort
print(mergeSort(array))

# test for quick sort
quickSort(array, 0, len(array) - 1)
print(array)