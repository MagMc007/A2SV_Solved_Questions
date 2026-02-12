# https://leetcode.com/problems/ransom-note/description/
# 383. Ransom Note

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)

        for i in ransomNote:
            if counts[i] > 0:
                counts[i] -= 1
            else:
                return False
    
        return True