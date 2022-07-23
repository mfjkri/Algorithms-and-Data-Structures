'''
    Hash Table
'''

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __str__(self):
        return "({}, {})".format(self.key, self.value)

class HashTable:

    def __init__(self):
        self.table = [None] * 26

    def hashToIndex(self, key):
        firstLetter = key[0].lower()
        index = ord(firstLetter) - 97
        return index
    
    def insert(self, key, value):
        index = self.hashToIndex(key)
        self.table[index] = HashItem(key, value)
    
    def search(self, key):
        index = self.hashToIndex(key)
        if self.table[index] is not None and self.table[index].key == key:
            return self.table[index]

scores = HashTable()
scores.insert("Adam", 98)
scores.insert("Derek", 56)
scores.insert("Chris", 72)
scores.insert("Ethan", 79)

name = input("name: ")
print(scores.search(name))

