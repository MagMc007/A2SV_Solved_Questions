# https://leetcode.com/problems/construct-smallest-number-from-di-string/description/?envType=problem-list-v2&envId=backtracking
# 2375. Construct Smallest Number From DI String
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        used = [False] * 10
        res = []

        def backtrack(numb):
            # print(numb)
            if res:
                return
            
            # base case
            if len(numb) == len(pattern) + 1:
                res.append("".join(numb))
                return

            for i in range(1, 10):
                if used[i]:
                    continue

                # check if it is in order
                if numb:
                    prev = int(numb[-1])
                    idx = len(numb) - 1
                    # idx vs prev

                    if pattern[idx] == "I" and prev > i:
                        continue
                    
                    if pattern[idx] == "D" and prev < i:
                        continue

                numb.append(str(i))
                used[i] = True
                backtrack(numb)
                numb.pop()
                used[i] = False

        backtrack([])
        return res[0]

Solution().smallestNumber("D")
