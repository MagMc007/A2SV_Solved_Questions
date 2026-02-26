# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description
# 1493. Longest Subarray of 1's After Deleting One Element
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # we're not deleting we are keeping track
        zero_cnt = 0
        
        # track the left window and the length
        left = 0
        longest = 0

        for right in range(len(nums)):
            # record 0
            if nums[right] == 0:
                zero_cnt += 1
            
            # track zeros
            if zero_cnt <= 1:
                longest = max(longest, right - left) # removed one because we remove 0
                continue

            while zero_cnt > 1:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            
        return longest
        
soln = Solution()
print(soln.longestSubarray(nums = [0,1,1,1,0,1,1,0,1]))


# time O(n)
# space O(1)