# https://leetcode.com/problems/first-missing-positive/description/
# 41. First Missing Positive
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()

        marker = 0
        prev = None

        for i in nums:
            # ignore all the non positives
            if i <= 0:
                continue
            
            if i == prev:
                continue

            marker += 1
            prev = i
            
            if i != marker:
                return marker

        return marker + 1

# print(Solution().firstMissingPositive([10]))

# violated the constriant O(n) time and uses O(1) auxiliary space.


class Solution2:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # get rid of the negatives
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 0
        
        # mark those that exist by making them -ve
        # if 0 then make it -ve of the largest possible value
        for j in range(len(nums)):
            val = abs(nums[i])

            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1 
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        
        # check and get the smallest
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0:
                return i
        return len(nums) + 1
    
print(Solution2().firstMissingPositive([1,2,0]))