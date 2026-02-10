# https://leetcode.com/problems/two-sum/description/
# 1. Two Sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
            create a hash map
            key: 
                target minus the elemt at that idx
                value: the index
            
            iterate over the list looking up for the number
            if it is equal to that number, return the idx of the current elt 
            you're at and the idx of that number from the hash
        """
        hash = {}
        for i in range(len(nums)):
            k = target - nums[i]
            hash[k] = i

        for i in range(len(nums)):
            if nums[i] in hash and i != hash[nums[i]]:
                return [i, hash[nums[i]]]
        
soln = Solution()
print(soln.twoSum(nums = [3,3], target = 6))