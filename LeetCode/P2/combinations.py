# https://leetcode.com/problems/combinations/description/
# 77. Combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n+1)]
        com = []

        def backtrack(i, comb):
            if len(comb) == k:
                com.append(comb[:])
                return 

            if i == len(arr):
                return 
            

            comb.append(arr[i])
            backtrack(i + 1, comb)

            comb.pop()
            backtrack(i+1, comb)

        backtrack(0, [])
        return com
           
