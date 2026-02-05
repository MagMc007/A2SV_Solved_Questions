class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # utilized sum to the biggest to get the missing number
        maxNum = max(nums)
        sumToMax = (maxNum / 2) * (maxNum + 1) # from arithmetic sequence
        missing = sumToMax - sum(nums)

        if missing == 0 and maxNum != len(nums):
            return int(maxNum + 1)
        return int(missing)