# https://leetcode.com/problems/custom-sort-string/
# 791. Custom Sort String
from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # keep count of the elemts in s
        hash_cnt = Counter(s)
        visited = set()

        # iterate over order so that we can have the elemts first
        # instanciate arr of size s
        output = ""

        for i in order:
            if i in hash_cnt:
                output += i * hash_cnt[i]
                visited.add(i)

        # for those not in order
        for j in s:
            if j not in visited:
                output += j

        return output
