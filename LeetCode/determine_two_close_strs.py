# https://leetcode.com/problems/determine-if-two-strings-are-close/
# 1657. Determine if Two Strings Are Close
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        cnt1 = list(Counter(word1).values())
        cnt2 = list(Counter(word2).values())

        # we must have the same set of letters
        word1 = set(word1)
        word2 = set(word2)

        if word2 != word1:
            return False
        # we must have the same number of counts(the letters may be 
        # different) so that both the opns are possible
        if sorted(cnt1) != sorted(cnt2):
            return False
        
        return True
        
        

        
        
        