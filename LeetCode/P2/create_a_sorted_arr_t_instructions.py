# 1649. Create Sorted Array through Instructions
# https://leetcode.com/problems/create-sorted-array-through-instructions/description/
from bisect import bisect_right, bisect_left


class Solution:
    def createSortedArray(self, instructions: list[int]) -> int:
        cost = 0

        sorted_arr = []

        for i in range(len(instructions)):
            idx1 = bisect_right(sorted_arr, instructions[i])
            idx2 = bisect_left(sorted_arr, instructions[i])

            less = idx2
            greater = i - idx1

            cost += min(less, greater)
            sorted_arr.insert(idx1, instructions[i])
            
        return cost % (7 + 10 ** 9)

# print(Solution().createSortedArray([1,5,6,2]))