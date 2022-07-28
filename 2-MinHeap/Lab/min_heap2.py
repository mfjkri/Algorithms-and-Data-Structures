'''
    Implement a minimum binary heap with changing keys
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
    - You may reference from min_heap1.py and make the appropriate adjustments
    - To test your implementation, run `python utils/mh2_test.py`
'''

from typing import Dict, List, Union
from utils.helpers import parent, left, right, HeapItem


class MinHeap:
    def higherPriority(self, index1: int, index2: int) -> Union[bool, None]:
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

    def swap(self, index1: int, index2: int) -> None:
        key1: str = self.heap[index1].key
        key2: str = self.heap[index2].key
        self.positions[key1], self.positions[key2] = self.positions[key2], self.positions[key1]
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def __init__(self, maxsize: int):
        """Initialise heap

        Attributes
        ----------
        heap: type `array`, length = maxsize + 1, begins empty
            -> binary heap representation
        size: type `int` 
            -> number of existing items in heap, begins at 0
        maxsize: type `int` 
            -> max number of items in heap, begins with argument
        positions: type `dict`
            -> stores the positions (indices) of keys in the heap, begins empty

        Arguments
        ----------
        maxsize: type `int`

        Return: None
        """
        self.heap: List[Union[HeapItem, None]] = [None] * (maxsize + 1)
        self.size: int = 0
        self.maxsize: int = maxsize
        self.positions: Dict[str, int] = {}

    def swim(self, index: int) -> None:
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
                self.swap(index, parentIndex)
                index = parentIndex
            else:
                break

    def sink(self, index: int) -> None:
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
                self.swap(index, bigger_child_index)
                # (ensure to update positions attribute accordingly)
                index = bigger_child_index
            else:
                break

    def insert(self, newKey: str, newValue: int) -> None:
        """Insert a new key-value pair into heap, 
        or change key if already exists

        Arguments
        ----------
        newKey: type `string` -> new key to insert
        newValue: type `int` -> new value to insert

        Returns None

        Note: Items in Heap are sorted according to their VALUE 
        """

        # 1. Check if heap is already at max size
        if self.size == self.maxsize:
            # unlike mh1, we cannot exit if maxsize is reached
            # since the "insertion" can be an update to existing item instead
            # return
            self.resize()

        if newKey in self.positions:
            current_index: int = self.positions[newKey]
            self.heap[current_index].value = newValue
            self.swim(current_index)
            self.sink(current_index)
        else:
            # 2. Insert new HeapItem at next unfilled index of heap
            self.heap[self.size + 1] = HeapItem(key=newKey, value=newValue)
            self.positions[newKey] = self.size + 1

            # 3. Swim the inserted HeapItem
            self.swim(self.size + 1)

            # 4. Increment size attribute
            self.size += 1

    def removeMin(self) -> Union[HeapItem, None]:
        """Extracts HeapItem with highest priority value 
        (i.e. lowest value in Min Heap)

        Arguments: None

        Returns HeapItem with highest priority in min heap, or None if heap is empty
        """

        # 0. Return None if heap is empty
        if self.size == 0:
            return None

        # 1. Save item with highest priority (first item in heap)
        popItem: HeapItem = self.heap[1]

        # 2. Swap first and last item in heap
        self.swap(1, self.size)

        # 3. Delete last item (decrement size attribute)
        self.heap[self.size] = None
        self.size -= 1

        # 4. Sink the first item to appropriate position
        self.sink(1)

        return popItem

    def resize(self) -> None:
        self.heap.extend([None] * self.maxsize)
        self.maxsize *= 2
