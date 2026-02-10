# https://leetcode.com/problems/valid-anagram/description/
# 242. Valid Anagram
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can compare dicts btw
        # so just hash with couter and compare them
        hash = Counter(s)
        hash2 = Counter(t)
        return hash == hash2