# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/submissions/1532115915/
# 1347. Minimum Number of Steps to Make Two Strings Anagram
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # hash t to a counter
        hash = Counter(t)

        # number of elemts we need to change
        cnt = 0

        # iterate over s and keep count of the elements
        for char in s:
            # you donnot have it in t, then add 1
            if hash.get(char, 0):
                hash[char] -= 1
            else:
                cnt += 1

        return cnt