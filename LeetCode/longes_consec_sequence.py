# https://leetcode.com/problems/longest-consecutive-sequence/description/
# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        # required O(n), no sorting
        nums = set(nums)

        # we need to find the start of a sequence
        # then we iteratively check if the number next to it is 
        # in the set: O(1) lookup, continue till the end

        max_len = 1

        for num in nums:
            # record length
            length = 1
            # can the number be a start of a seq
            # check if there is num - 1
            if num - 1 in nums:
                continue
            else:
                # if it reaches here then the number is a start of a 
                # sequence
                # so iterate to the end of the seq
                while num + 1 in nums:
                    length += 1
                    num += 1
            max_len = max(max_len, length)
        return max_len


soln = Solution()
print(soln.longestConsecutive( nums = [100,4,200,1,3,2] ))




        
