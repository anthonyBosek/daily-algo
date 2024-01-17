"""
    380. Insert Delete GetRandom O(1)
    
    Implement the RandomizedSet class:

        • RandomizedSet() Initializes the RandomizedSet object.
        • bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
        • bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
        • int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists
            when this method is called). Each element must have the same probability of being returned.

    You must implement the functions of the class such that each function works in average O(1) time complexity.

"""

import random


class RandomizedSet:
    # ------------------------------------------------------------
    # marksphilip
    # def __init__(self):
    #     self.lst = []
    #     self.idx_map = {}

    # def search(self, val):
    #     return val in self.idx_map

    # def insert(self, val):
    #     if self.search(val):
    #         return False

    #     self.lst.append(val)
    #     self.idx_map[val] = len(self.lst) - 1
    #     return True

    # def remove(self, val):
    #     if not self.search(val):
    #         return False

    #     idx = self.idx_map[val]
    #     self.lst[idx] = self.lst[-1]
    #     self.idx_map[self.lst[-1]] = idx
    #     self.lst.pop()
    #     del self.idx_map[val]
    #     return True

    # def getRandom(self):
    #     return random.choice(self.lst)

    # ------------------------------------------------------------
    # my solution
    # def __init__(self):
    #     self.my_set = set()

    # def insert(self, val: int) -> bool:
    #     if val not in self.my_set:
    #         self.my_set.add(val)
    #         return True
    #     return False

    # def remove(self, val: int) -> bool:
    #     if val in self.my_set:
    #         self.my_set.remove(val)
    #         return True
    #     return False

    # def getRandom(self) -> int:
    #     return random.choice(list(self.my_set))

    # ------------------------------------------------------------
    # tolujimoh
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hashTable:
            self.hashTable[val] = len(self.arr)
            self.arr.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hashTable:
            self.hashTable[self.arr[-1]] = self.hashTable[val]
            self.arr[self.hashTable[val]] = self.arr[-1]

            self.arr.pop()
            self.hashTable.pop(val)

            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
