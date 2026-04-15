# https://leetcode.com/problems/set-mismatch/description/
# 645. Set Mismatch
from collections import Counter

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        s = sum(nums)
        mx = len(nums)
        needed = (mx * (mx+1)) // 2
        
        # n(n+1)/2
        for i in range(len(nums)):
            if cnt[nums[i]] == 2:
                # means the number is at the wrong place 
                diff = s - needed

                return [nums[i], nums[i] - diff]


print(Solution().findErrorNums([3,2,3,4,6,5]))

# time: O(n)
# space: O(n)

# sorting approach
# counting sort

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        arr = [0] * (len(nums) + 1)

        for i in nums:
            arr[i] += 1

        rep = None
        missed = None

        for i in range(1, len(arr)):  # arr[0] is always 0 and no in permutation
            if arr[i] == 2:
                rep = i

            if arr[i] == 0:
                missed = i

        return [rep, missed]