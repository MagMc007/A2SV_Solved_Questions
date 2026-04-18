# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/description/
# 2426. Number of Pairs Satisfying Inequality
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # A[i] <= A[j] + diff where A[x] = nums1[x] - nums2[x]
        A = [n1 - n2 for n1, n2 in zip(nums1, nums2)]
        self.count = 0
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            # Count valid pairs (i, j) where i is in 'left' and j is in 'right'
            # At this point, 'left' and 'right' are already sorted.
            i = 0
            for j in range(len(right)):
                while i < len(left) and left[i] <= right[j] + diff:
                    i += 1
                self.count += i
            
            return sorted(left + right) # Or use a standard merge loop for true O(n log n)

        merge_sort(A)
        return self.count