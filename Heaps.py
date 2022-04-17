def maxHeapify(array, heap_size, index):
    '''
    Given a tree and an index, move the element 
    in that index to a place conforming to the 
    max heap properties
    Assumption: left and right subtree of the 
    given node are max heaps
    '''
    # indexing would be different for pseudocode
    if index == 0:
        left = 1
        right = 2
    else:
        left = (index * 2) + 1
        right = (index * 2) + 2
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

#array = [8,1,2,9,14,3,7,4,10,16]