'''
    Implement a minimum binary heap
    - You are to implement the following methods:
        -> constructor
        -> sink, swim
        -> insert, getMin

    - Each method comes with instructions on how to implement them. 
    - You are given helper functions from the util folder:
        -> parent: get parent index
        -> left, right: get left & right child index respectively
        -> HeapItem: contains key & value attributes. HeapItems in MinHeap are sorted accoridng to value
    - The higherPriority method has been implemented to help compare two HeapItems in the MinHeap
    - To test your implementation, run `python utils/mh1_test.py`
'''

from typing import List, Union
from utils.helpers import parent, left, right, HeapItem


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


class MinHeap1:
    def higherPriority(self, index1, index2):
        """Compare two indices in heap

        Returns
        ----------
        - None if index1 or index2 are invalid
        - True if value of item at index1 is higher priority (lower in the case of MinHeap) 
        compared to value of item at index 2 & False if not
        """
        if self.heap[index1] is None or self.heap[index2] is None:
            return

        if self.heap[index1].value < self.heap[index2].value:
            return True
        else:
            return False

    def __init__(self, maxsize):
        """Initialise heap

        Attributes
        ----------
        heap: type `array`, length = maxsize + 1 
            -> binary heap representation
        size: type `int` 
            -> number of existing items in heap
        maxsize: type `int` 
            -> max number of items in heap

        Arguments
        ----------
        maxsize: type `int`

        Return: None

        Note: Items should be inserted starting from index 1 for ease of use
        """

        self.heap: List[Union[HeapItem, None]] = [None] * (maxsize + 1)
        self.size: int = 0
        self.maxsize: int = maxsize

    def swim(self, index):
        """Move a HeapItem up the heap

        Arguments
        ----------
        index: type `int` -> starting index of HeapItem to swim

        Returns None
        """

        # while:
        #   - item is not at the top of the heap AND
        while index > 1:
            parentIndex: int = parent(index)

            #   - item's key has higher priority than parent's key
            if self.higherPriority(index, parentIndex):
                # swap with parent
                swap(self.heap, index, parentIndex)
                index = parentIndex
            else:
                break

    def sink(self, index):
        """Move a HeapItem down the heap

        Arguments
        ----------
        index: type `int` -> starting index of HeapItem to sink

        Returns None
        """

        while left(index) < self.maxsize:
            left_child_index: int = left(index)
            right_child_index: int = right(index)

            bigger_child_index = left_child_index
            if self.heap[right_child_index]:
                bigger_child_index: int = bigger_child_index if self.higherPriority(
                    left_child_index, right_child_index) else right_child_index

            # if item's key has lower priority than children's key:
            if self.higherPriority(bigger_child_index, index):
                # swap with children with highest priority
                swap(self.heap, index, bigger_child_index)
                # (ensure to update positions attribute accordingly)
                index = bigger_child_index
            else:
                break

    def insert(self, newKey, newValue):
        """Insert a new key-value pair into heap

        Arguments
        ----------
        newKey: type `string` -> new key to insert
        newValue: type `int` -> new value to insert

        Returns None

        Note: Items in Heap are sorted according to their VALUE 
        """

        # 1. Check if heap is already at max size
        if self.size == self.maxsize:
            return
            self.resize()  # can't actually call this since there is a test for constant size

        # 2. Insert new HeapItem at next unfilled index of heap
        self.heap[self.size + 1] = HeapItem(key=newKey, value=newValue)

        # 3. Swim the inserted HeapItem
        self.swim(self.size + 1)

        # 4. Increment size attribute
        self.size += 1

    def removeMin(self):
        """Extracts HeapItem with highest priority value 
        (i.e. lowest value in Min Heap)

        Arguments: None

        Returns HeapItem with highest priority in min heap, or None if heap is empty
        """

        # 0. Return None if heap is empty
        if self.size == 0:
            return None

        # 1. Save item with highest priority (first item in heap)
        popItem = self.heap[1]

        # 2. Swap first and last item in heap
        swap(self.heap, 1, self.size)

        # 3. Delete last item (decrement size attribute)
        self.heap[self.size] = None
        self.size -= 1

        # 4. Sink the first item to appropriate position
        self.sink(1)

        return popItem

    def resize(self):
        self.heap.extend([None] * self.maxsize)
        self.maxsize *= 2
