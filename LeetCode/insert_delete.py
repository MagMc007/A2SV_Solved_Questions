# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
# 380. Insert Delete GetRandom O(1)

import random


class RandomizedSet:
    def __init__(self):
        self.set = []
        self.tracker = {}

    def insert(self, val: int) -> bool:
        """
            the value must not be in the set to insert

            to insert I just have to add it to the hashmap and append it
        """
        res = val not in self.tracker
        if res:
            self.tracker[val] = len(self.set)
            self.set.append(val)
        return res

    def remove(self, val: int) -> bool:
        """
            result must be in the set
            replace the result with the last elemnt and 
            get rid of the last elemt with pop O(1)

            the last element may be the one to be removed, so 
            do the popping at the end to handle all possible cases
        """
        res = val in self.tracker
        if res:
            idx = self.tracker[val] 
            last = self.set[-1]
            self.set[idx] = last
            self.set.pop()
            self.tracker[last] = idx
            self.tracker.pop(val)
        return res

    def getRandom(self) -> int:
        return random.choice(self.set)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(1)
# param_2 = obj.remove(2)
# param_1 = obj.insert(2)
# param_3 = obj.getRandom()
# print(param_3)