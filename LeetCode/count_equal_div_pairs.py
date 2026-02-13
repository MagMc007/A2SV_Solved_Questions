# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/
# 2176. Count Equal and Divisible Pairs in an Array
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        output = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j] and (i * j) % k == 0:
                    output += 1
        return output // 2
        