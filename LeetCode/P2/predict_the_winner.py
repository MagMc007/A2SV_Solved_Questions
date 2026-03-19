# https://leetcode.com/problems/predict-the-winner/
# 486. Predict the Winner
class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        def get_max_score(left, right):
            # base case 
            if left == right:
                return nums[left]
        
            choice1 = nums[left] - get_max_score(left+1, right)
            choice2 = nums[right] - get_max_score(left, right-1)
            # print(choice1, choice2)
            return max(choice1, choice2)
        
        return get_max_score(0, len(nums)-1) >= 0


print(Solution().predictTheWinner([1,5,2]))


"""
sort of form a tree at each step we can go left and we can go
at each step we have to consider the maximum score that came 
from theback so and subtract it 
the subtraction is because the score the opponent is decreased 
from what we have

time: 2^n at each step we are increasing the branching by 2
     check 1(2^0) => 2=> 4 .... 2**n
space: O(n)  call stack 
"""