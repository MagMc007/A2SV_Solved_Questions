# https://leetcode.com/problems/minimum-index-of-a-valid-split/description/
# 2780. Minimum Index of a Valid Split
from collections import Counter


class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        freq = Counter(nums)

        # identify the dominant
        dominant = [0, 0]

        for key, value in freq.items():
            if value > dominant[1]:
                dominant[0] = key
                dominant[1] = value

        # we have a left and right array
        # for each splt we have keep count of the dominant and 
        # the other number in the list
        # if nums[0] == dominant[0]:
        #     left_dominant = 1
        #     left_others = 0
        # else:
        #     left_dominant = 0
        #     left_others = 1
        left_dominant = 0
        left_others = 0
        
        for i in range(len(nums)):
            if nums[i] == dominant[0]:
                # the current elemnt is dominant of the left
                left_dominant += 1
            else:
                left_others += 1
            
            # we must check if the dominant number 
            # is dominant in both (greater than len // 2)

            # get the dominant number from the next split
            right_dominant = dominant[1] - left_dominant
        
            is_dominant_in_left = left_dominant > (i + 1) // 2
            is_dominant_in_right = right_dominant > (len(nums) - i - 1) // 2

            if is_dominant_in_left and is_dominant_in_right:
                return i
        # if there is no splitting keeping the rule
        return -1

soln =  Solution()
print(soln.minimumIndex([1,3,3,3,3,7]))




