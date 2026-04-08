# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/
# 2226. Maximum Candies Allocated to K Children
class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:

        def coversAll(middle):
            covered = 0

            for i in candies:
                covered += i // middle
            # print(middle, covered >= k)
            return covered >= k
    
        left = 1
        right = max(candies)
        ans = 0

        while left <= right:
            # take the middle
            # if it covers look for higher if not look for lower
            mid = (left + right) // 2

            if coversAll(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

print(Solution().maximumCandies([1,2,3,4,10], 5))


'''
time: O(nlogn)
space: O(1)


my mistake was considering the right as the min, 
should have considered elements that can be left behind
'''