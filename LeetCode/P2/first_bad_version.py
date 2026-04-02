# https://leetcode.com/problems/first-bad-version/description/?envType=problem-list-v2&envId=binary-search
# 278. First Bad Version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binSrch(left, right):
            if left == right:
                return left
            
            mid = (left+right)//2

            if isBadVersion(mid):  # search towards the left
                return binSrch(left, mid)
            else:
                return binSrch(mid+1, right)
        return binSrch(1, n)
    