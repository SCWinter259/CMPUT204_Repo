import random

def randomPartition(array, first, last):
    '''
    This function will randomize the partition position
    and then use partition like normal
    '''
    index = random.randint(first, last)
    array[index], array[last] = array[last], array[index]
    return partition(array, first, last)

def partition(array, first, last):
    '''
    This function moves the pivot and switch numbers
    '''
    mark_value = array[last]
    # pivot would mark the index of the last 
    # element smaller than mark_value
    pivot = first - 1
    for i in range(first, last):
        if array[i] <= mark_value:
            pivot = pivot + 1
            array[pivot], array[i] = array[i], array[pivot]
    array[pivot + 1], array[last] = array[last], array[pivot + 1]
    # returns the position of the mark_value after exchange
    return pivot + 1

def quickSort(array, first, last):
    '''
    This fucntion sorts the array in-place
    '''
    # first and last are for indexes, not first and last elements
    if first < last:
        # pivot = partition(array, first, last)
        pivot = randomPartition(array, first, last)
        quickSort(array, first, pivot - 1)
        quickSort(array, pivot + 1, last)