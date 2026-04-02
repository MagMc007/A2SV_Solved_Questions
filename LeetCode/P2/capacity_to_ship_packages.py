# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
# 1011. Capacity To Ship Packages Within D Days
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ans = -1 
        left = max(weights)
        right = sum(weights)

        def check(cap, weights):
            day = 1
            curr = 0

            for w in weights:
                if w + curr > cap:
                    day += 1
                    curr = 0
                else:
                    curr += w

            return day <= days
      
        while left <= right:
            mid = (left + right) // 2
         
            if check(mid, weights):
                ans = mid
                right = mid - 1
            else:
                left = mid+1
    
        return ans
