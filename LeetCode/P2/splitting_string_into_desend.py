# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/?envType=problem-list-v2&envId=backtracking
# 1849. Splitting a String Into Descending Consecutive Values
class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(ind, prev):
            print(prev)
            if ind == len(s):
                # return True
                for i in range(1, len(prev)):
                    if prev[i - 1] - prev[i] != 1:
                        return False

                return len(prev) >= 2

            for j in range(ind, len(s)):
                val = int(s[ind: j + 1])
                prev.append(val)
                if backtrack(j + 1, prev):
                    return True
                prev.pop()

            return False

        return backtrack(0, [])
    
    
Solution().splitString("050043")