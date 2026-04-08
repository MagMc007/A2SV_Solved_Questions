# https://leetcode.com/problems/sort-an-numsay/description/
# 912. Sort an numsay
class Solution:
    def merge(self, left_half,right_half) -> List[int]:
        ptr0 = 0
        ptr1 = 0

        ans = []

        while ptr0 < len(left_half) and ptr1 < len(right_half):
            if left_half[ptr0] >= right_half[ptr1]:
                ans.append(right_half[ptr1])
                ptr1 += 1
            else:
                ans.append(left_half[ptr0])
                ptr0 += 1
        
        ans.extend(right_half[ptr1:])
        ans.extend(left_half[ptr0:])

        return ans
    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def divide(left, right, nums):
            if left == right:
                return [nums[left]]
            
            mid = left + (right - left) // 2
            left_half = divide(left, mid, nums)
            right_half = divide(mid + 1, right, nums)

            return self.merge(left_half, right_half)
    
        return divide(0, len(nums)-1, nums)
