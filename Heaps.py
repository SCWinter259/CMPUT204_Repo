def Left(index):
    if index == 0:
        return 1
    else:
        return (index * 2) + 1

def Right(index):
    if index == 0:
        return 2
    else:
        return (index * 2) + 2

def Parent(index):
    if index == 0:
        return None
    elif index % 2 == 1:
        return index // 2
    else:
        return (index // 2) - 1

def maxHeapify(array, heap_size, index):
    '''
    Given a tree and an index, move the element 
    in that index to a place conforming to the 
    max heap properties
    Assumption: left and right subtree of the 
    given node are max heaps
    '''
    # indexing would be different for pseudocode
    left = Left(index)
    right = Right(index)
    max_index = index
    if left < heap_size and array[left] > array[index]:
        max_index = left
    if right < heap_size and array[right] > array[max_index]:
        max_index = right
    if max_index != index:
        array[index], array[max_index] = array[max_index], array[index]
        maxHeapify(array, heap_size, max_index)

def buildMaxHeap(array):
    for i in reversed(range(len(array) // 2)):
        maxHeapify(array, len(array), i)

def heapSort(array):
    buildMaxHeap(array)
    heap_size = len(array)
    for i in reversed(range(1, heap_size)):
        array[0], array[i] = array[i], array[0]
        heap_size = heap_size - 1
        maxHeapify(array, heap_size, 0)

def heapExtractMax(array):
    heap_size = len(array)
    max_element = array[0]
    array[0] = array[heap_size - 1]
    heap_size = heap_size - 1
    if heap_size > 0:
        maxHeapify(array, heap_size, 0)
    return max_element

def heapIncreaseKey(array, index, key):
    '''
    Replace the value of a node with a larger
    value, then move the node to the right place
    '''
    array[index] = key
    while (index > 0) and (array[Parent(index)] < array[index]):
        array[index], array[Parent(index)] = array[Parent(index)], array[index]
        index = Parent(index)

def heapInsert(array, key):
    heap_size = len(array) + 1
    array.append(None)
    heapIncreaseKey(array, heap_size - 1, key)
