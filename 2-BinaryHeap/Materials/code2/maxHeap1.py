'''
    Max Heap
'''

# HELPER FUNCTIONS
def parent (index):
    return index // 2

def left (index):
    return index * 2

def right (index):
    return index * 2 + 1

def swap (array,index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

class HeapItem: 
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __str__(self):
        return "({}, {})".format(self.key, self.value)

# MaxHeap Class
class MaxHeap:
    def greater(self, index1, index2):
        if self.heap[index1].value > self.heap[index2].value:
            return True
        else:
            return False

    def __init__ (self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [None] * (maxsize + 1)
    
    def swim (self, index):

        while (index != 1 and self.greater(index, parent(index))):
            swap(self.heap, index, parent(index))
            index = parent(index)
        
        return

    def insert(self, newKey, newValue):
        if self.size >= self.maxsize:
            print('size limit reached')
            return

        
        self.size += 1
        self.heap[self.size] = HeapItem(newKey, newValue)
        self.swim(self.size)

    def sink(self, index):
        while (2 * index <= self.size):

        # initialize j to be left child
            j = left(index)

            # compare left and right
            if (j < self.size and self.greater(right(index), j)):
                j = right(index)

            if self.greater(index, j):
                break

            else:
                swap(self.heap, j, index)
                index = j

        return
    
    def getMax(self):

        if self.size == 0:
            return None
        # SAVE MAX ITEM FOR REMOVAL
        maxItem = self.heap[1]

        # SWAP MAX ITEM
        swap(self.heap, 1, self.size)

        # REMOVE ITEM
        self.heap[self.size] = None
        self.size -= 1

        # SINK FIRST ITEM
        self.sink(1)
        return maxItem

# MAIN
pq = MaxHeap(10)
pq.insert("Google", 30)
pq.insert("Amazon", 20)
pq.insert("Apple", 60)
pq.insert("Microsoft", 40)
pq.insert("Netflix", 25)

print("Heap state: [", end = "")
for i in pq.heap:
    print(i, end=", ")
print("]")

print("\nExtracting max until heap is empty")
while (pq.size != 0):
    print(pq.getMax())