# https://leetcode.com/problems/largest-number/description/
# 179. Largest Numberclass Solution:
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        # cast all elements to string
        nums = list(map(str, nums))

        # compare and sort all elements based on the element[0]
        # if first element is the same compare with the 
        # subsequent

        n = len(nums)

        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] < nums[j+1]:
                    if (nums[j].startswith(nums[j+1]) or nums[j+1].startswith(nums[j])) and len(nums[j]) != len(nums[j+1]):
                        con1 = int(nums[j] + nums[j+1])
                        con2= int(nums[j+1] + nums[j])

                        if con1 > con2:
                            

                        
                    else:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

soln = Solution()
print(soln.largestNumber(nums =  [3,30,34,5,9]))