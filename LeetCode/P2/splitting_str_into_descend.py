# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/description/
# 1849. Splitting a String Into Descending Consecutive Values
class Solution:
    def splitString(self, s: str) -> bool:
        # state:- just one index and current, root is gonna be i and the rest will
        # be from i+1 to the end
        
        def backtrack(idx, current):
            if idx == len(s):
                # check it current is valid
                for i in range(1, len(current)):
                    if current[i-1] - current[i] != 1:
                        return False
                return len(current) >= 2
            
            for j in range(idx, len(s)):
                val = int(s[idx:j+1])
                current.append(val)
                if backtrack(j+1, current):
                    return True
                
                current.pop()
            return False
        return backtrack(0, [])

