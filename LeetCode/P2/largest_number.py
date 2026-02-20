# https://leetcode.com/problems/largest-number/description/
# 179. Largest Numberclass Solution:
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)

        # cast them to str and sort 
        # .sort comapres iterables based on the indices not len
        nums = list(map(str, nums))
        nums.sort()

        for i in range(n):
            for j in range(n - i - 1):
                # 3 30 vs 30 3 compare them as strs
                con1 = nums[j] + nums[j+1]
                con2 = nums[j+1] + nums[j]
                
                if con2 > con1:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        # print(nums)
        # when it is 0 0 , we just gotta keep one of it
        nums = str(int("".join(nums)))
        return nums
