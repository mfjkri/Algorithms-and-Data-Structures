'''
    Hash Table with Linear Probing
'''

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __str__(self):
        return "({}, {})".format(self.key, self.value)

class LPHashTable:

    def __init__(self, capacity):
        self.table = [None] * capacity
        self.size = 0

    def hashToIndex(self, key, capacity):
        firstLetter = key[0].lower()
        index = ord(firstLetter) - 97
        return index % capacity
    
    def resizeAndRehash(self):
        currentCap = len(self.table)
        newTable = LPHashTable(currentCap * 2)

        for i in range(currentCap):
            newTable.insert(self.table[i].key, self.table[i].value)

        self.table = newTable.table
        return

    def insert(self, key, value):
        if (self.size == len(self.table)):
            self.resizeAndRehash()

        index = self.hashToIndex(key, len(self.table))

        while self.table[index] != None:
            index += 1
            index = index % len(self.table)

        self.table[index] = HashItem(key, value)
        self.size += 1
    
    def search(self, key):
        index = self.hashToIndex(key, len(self.table))
        start = index

        if self.table[index] == None:
            return None
        
        while (self.table[index].key != key):
            index += 1
            index %= len(self.table)

            if index == start or self.table[index] == None:
                return None
            elif index == start:
                return None
        
        return self.table[index]

    def delete(self, key):
        index = self.hashToIndex(key, len(self.table))
        start = index

        if self.table[start] == None:
            return None
        
        while (self.table[index].key != key):
            index += 1
            index %= len(self.table)

            if index == start:
                print("key doesn't exist, delete failed")
                return

            elif not self.table[index]:
                print("key doesn't exist, delete failed")
                return

        self.table[index] = HashItem("%", None)
        self.size -= 1


# LP HASH TABLE TEST
scores = LPHashTable(5)
scores.insert("Adam", 98)
scores.insert("Alice", 93)
scores.insert("Beth", 100)
scores.insert("Esther", 89)
scores.insert("Ethan", 80)
# scores.insert("Kevin", 56)

# for row in scores.table:
#     if (isinstance(row, HashItem)):
#         print("({}, {})".format(row.key, row.value))


print(scores.search("Adam"))
print(scores.search("Eric"))


# scores.delete("Dan")
# print(scores.search("Derek"))

