# https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=problem-list-v2&envId=hash-table
# 349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1.intersection(set2))