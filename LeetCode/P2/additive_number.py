# https://leetcode.com/problems/additive-number/description/?envType=problem-list-v2&envId=backtracking
# 306. Additive Number
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        def backtrack(idx, prev):
            # all numbers in prev starting from the 2nd must be
            # the sum of the prev 2

            if idx == len(num):
                for j in range(2, len(prev)):
                    if prev[j-2] + prev[j-1] != prev[j]:
                        return False
                    
                return len(prev) >= 3

            for i in range(idx, len(num)):
                # cannot have preceding 0
                if num[idx] == '0' and i > idx:
                    break
                
                val = int(num[idx:i+1])
                # pruning
                # val must be equal to expected (the last from prev)
                if len(prev) > 2:
                    expected = prev[-1] + prev[-2]
                    if val < expected:  # too small, add digits to it
                        continue

                    if val > expected:
                        break

                prev.append(val)

                if backtrack(i+1, prev):
                    return True
                
                prev.pop()

            return False
            
        return backtrack(0, [])


print(Solution().isAdditiveNumber("1023"))