# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/description/
# 1247. Minimum Swaps to Make Strings Equal
from collections import Counter

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # join the two strings and get the count
        cnts = Counter(s1 + s1)

        # get the x, y (one is enough, we can get the next from the other)
        cnts1 = Counter(s1)

        # if a char has an odd cnt, the means 
        # it cannot appear in both
        for key, value in cnts.items():
            if value % 2 != 0:
                return False
        
        
        
        return swaps
        

            

        

        
        

        