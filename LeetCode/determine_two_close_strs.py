# https://leetcode.com/problems/determine-if-two-strings-are-close/
# 1657. Determine if Two Strings Are Close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        