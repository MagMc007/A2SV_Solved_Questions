# https://leetcode.com/problems/find-original-array-from-doubled-array/description/
# 2007. Find Original Array From Doubled Array
from collections import Counter


class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        # the length must be even 
        if len(changed) % 2 != 0:
            return []
        # *repetition is possible*

        # count the elements(all the values may be 1)
        hash = Counter(changed)

        # sort them, that way you can reach the double of an 
        # elemt before it doubles itself
        changed.sort()

        output = []

        for i in changed:
            if hash[i] == 0:
                continue
            elif hash.get(i * 2):
                # in this case decreament the count of both the
                # numbers
                hash[i] -= 1
                hash[2*i] -= 1
                output.append(i)
            else:
                return []
        return output



soln =Solution()
print(soln.findOriginalArray(changed = [1,3,4,2,6,8]))


