# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
# 315. Count of Smaller Numbers After Self
class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        result = [0] * n
        
        # (index, value)
        pairs = [(i, nums[i]) for i in range(n)]
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            merged = []
            i = j = 0
            right_count = 0
            
            while i < len(left) and j < len(right):
                if right[j][1] < left[i][1]:
                    # right element is smaller → it goes first
                    merged.append(right[j])
                    right_count += 1
                    j += 1
                else:
                    # left element: count how many smaller elements passed
                    result[left[i][0]] += right_count
                    merged.append(left[i])
                    i += 1
            
            # leftover left side
            while i < len(left):
                result[left[i][0]] += right_count
                merged.append(left[i])
                i += 1
            
            # leftover right side
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        merge_sort(pairs)
        return result