

'''
Problem #1: Implement a Hash Table
    - You are to implement the following methods:
        -> constructor
        -> insert
        -> search

    - Each method comes with instructions on how to implement them. 
    - The hash function has been implemented for you. You should make use of this to implement your insert and search methods
    - The class HashItem has been implemented for you. Each key value pair should be stored as a HashItem in the hash table
    - To test your hash table, run `python hash_test.py`
'''

from typing import List, Union, Any


class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({}, {})".format(self.key, self.value)


def hash(key) -> Union[int, None]:
    if not isinstance(key, str) or not key[0].isalpha():
        print('key should be a string & first char should be an alphabet')
        return None

    firstLetter = key[0].lower()
    index = ord(firstLetter) - 97
    return index


class HashTable:

    def __init__(self):
        self.table: List[Union[None, HashItem]] = [None] * 26

    def insert(self, key: str, value: Any) -> bool:
        """Insert into hash table

        Arguments
        ----------
        key: type `string`, first character should be an alphabet
        value: type `any`

        Returns True if item has been successfully added to the hash table and False if not
        """
        index: Union[int, None] = hash(key)

        if index and index >= 0 and index <= 25:
            self.table[index] = HashItem(key=key, value=value)
            return True

        return False

    def search(self, key: str) -> Union[HashItem, None]:
        """Search hash table

        Arguments
        ----------
        key: type `string`

        Returns HashItem associated with key in the hash table if there is one, else None
        """

        index: Union[int, None] = hash(key)

        if index and index >= 0 and index <= 25:
            possible_match: Union[HashItem, None] = self.table[index]

            if possible_match and possible_match.key == key:
                return possible_match

        return None
