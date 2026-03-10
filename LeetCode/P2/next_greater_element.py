# https://leetcode.com/problems/next-greater-element-i/description/
# 496. Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # change to monoton inc stack
        mon_stack = []
        hash = {}

        for i in nums2:
            while mon_stack and mon_stack[-1] < i:
                hash[mon_stack.pop()] = i
            
            mon_stack.append(i)
        
        for j in mon_stack:
            hash[j] = -1
        
        ans = []
        for k in nums1:
            ans.append(hash[k])
        
        return ans

