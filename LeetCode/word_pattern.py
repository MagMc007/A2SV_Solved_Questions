# https://leetcode.com/problems/word-pattern/description/
# 290. Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        # using zip map them together
        # keep in mind that there may be a hash conflict
        mapping = dict(zip(pattern, s))

        # repeated mapping
        if len(mapping) != len(set(s)):
            return False
        
        # they may be of different len
        if len(s) != len(pattern):
            return False

        for i in range(len(s)):
            # check that the map of that letter 
            # is the mapping if not return false
            if mapping[pattern[i]] != s[i]:
                return False
        return True
    
soln = Solution()
print(soln.wordPattern(pattern = "abba", s = "dog cat cat dog"))