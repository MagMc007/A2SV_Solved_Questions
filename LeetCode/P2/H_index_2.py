# https://leetcode.com/problems/h-index-ii/submissions/1204652403/
# 275. H-Index II
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # bin srch
        n = len(citations)
        left = 0
        right = len(citations) - 1

        while left <= right:
            middle = (left + right) // 2

            if citations[middle] == n - middle:
                return middle
            elif citations[middle] < n - middle: # current citation is less than 
                left = middle + 1
            else:
                right = middle - 1

        return n - left