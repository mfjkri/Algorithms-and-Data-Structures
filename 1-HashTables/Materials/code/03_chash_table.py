'''
    Hash Table with Chaining
'''

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({}, {})".format(self.key, self.value)

class HashTable:

    def __init__(self):
        self.table = [[] for i in range(26)]

    def hashToIndex(self, key):
        firstLetter = key[0].lower()
        index = ord(firstLetter) - 97
        return index
    
    def insert(self, key, value):
        index = self.hashToIndex(key)
        self.table[index].append(HashItem(key, value))
    
    def search(self, key):
        index = self.hashToIndex(key)
        
        keyList = self.table[index]
        
        for item in keyList:
            if item.key == key:
                return item
        
scores = HashTable()
scores.insert("Derek", 56)
scores.insert("Dylan", 89)

studentName = input('student name: ')

print(scores.hashToIndex("JO"))
print(scores.hashToIndex("IP"))
print(scores.search(studentName))