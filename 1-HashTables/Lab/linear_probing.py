'''
Problem #2: Implement a Hash Table with Linear Probing
    - You are to implement the following methods:
        -> constructor
        -> insert
        -> search
        -> delete

    - Each method comes with instructions on how to implement them. 
    - The hash function has been implemented for you. You should make use of this to implement your insert and search methods
    - The class HashItem has been implemented for you. Each key value pair should be stored as a HashItem in the hash table
'''

from typing import List, Union


class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({}, {})".format(self.key, self.value)


def hash(key, cap):
    if not isinstance(key, str) or not key[0].isalpha():
        print('key should be a string & first char should be an alphabet')
        return None

    firstLetter = key[0].lower()
    index = ord(firstLetter) - 97
    return index % cap


class LPHashTable:

    def __init__(self, capacity: int):
        """Initialise hash table

        Attributes
        ----------
        table: type `array`, length = capacity
        size: type `int` -> number of existing HashItems in table

        Arguments
        ----------
        capacity: type `int`, starting capacity of the hash table

        Return: None
        """

        self.table: List[Union[HashItem, None]] = [None] * capacity

        self.size = 0
        self.capacity = capacity

    def insert(self, key, value):
        """Insert into hash table

        Arguments
        ----------
        key: type `string`, first character should be an alphabet
        value: type `any`

        Returns True if item has been successfully added to the hash table and False if not
        """

        # If table is full, then resize capacity and rehash all current items
        if self.size == self.capacity:
            old_table: List[Union[HashItem, None]] = self.table

            self.size = 0
            self.capacity *= 2
            self.table: List[Union[HashItem, None]] = [None] * self.capacity

            for current_hash_item in old_table:
                # Only re-hash valid non-deleted items
                if current_hash_item and current_hash_item.key:
                    current_hash_item: HashItem
                    self.insert(
                        key=current_hash_item.key,
                        value=current_hash_item.value
                    )

        # Get home address of key
        index: Union[int, None] = hash(key, self.capacity)

        if index is not None:
            # Find the next available space from home address
            # This includes going back to the start of the table
            while self.table[index] is not None and self.table[index].value:
                index += 1
                index %= self.capacity

            # Once an available space is found (space is guaranteed)
            self.table[index] = HashItem(key=key, value=value)
            # Increment size
            self.size += 1

            return True

    def search(self, key):
        """Search hash table

        Arguments
        ----------
        key: type `string`

        Returns HashItem associated with key in the hash table if there is one, else None
        """
        # Find home adress of key
        index: Union[int, None] = hash(key, self.capacity)

        if index is not None:
            # starting_index is our home address
            starting_index = index

            while self.table[index] and self.table[index].key != key:
                index += 1
                index %= self.capacity

                # Our exit condition:
                #   1) Either we have went one full round hence index == starting_index
                #   2) Or the current space we are at has no valid item (there's a hole)
                if index == starting_index or self.table[index] is None:
                    return None

            # If we get here means loop terminated
            # Meaning we have two conditions guaranteed:
            #   1) The item at the index is a valid item
            #   2) The item at the index has a key that matches ours
            return self.table[index]

        return None

    def delete(self, key):
        """Delete key from hash table

        Arguments
        ----------
        key: type `string`

        Returns True if key has been deleted and False if not
        """

        # Find possible match
        # possible_match is a guaranteed match if it's not None
        possible_match: Union[HashItem, None] = self.search(key)

        if possible_match:
            possible_match.key = ""
            self.size -= 1

            return True

        return False
