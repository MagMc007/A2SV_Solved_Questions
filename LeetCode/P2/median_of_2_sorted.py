# https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=problem-list-v2&envId=binary-search
# 4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()

        if len(arr) % 2 == 0:
            return arr[len(arr)] / 2
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1]) / 2
