# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/1929407581/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
        
soln =  Solution()
print(soln.strStr(haystack = "mississippi", needle = "issip"))