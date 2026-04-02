# https://leetcode.com/problems/heaters/description/?envType=problem-list-v2&envId=binary-search
# 475. Heaters
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def check(radius) -> bool:
            # check if the radious i have chosen is a valid point and covers all houses
            heater_idx = 0
            for house in houses:
                # move to the last heater that can cover the current house with the current radius
                while heater_idx + 1 < len(heaters) and heaters[heater_idx] + radius < house:
                    heater_idx += 1
                
                # if the heater can't cover the current house
                if abs(heaters[heater_idx] - house) > radius:
                    return False
            return True
            
        
        #  binary search 
        high_rad = max(houses[-1], heaters[-1])
        low_rad = 0
        ans = 0

        while high_rad >= low_rad:
            middle = (high_rad + low_rad) // 2

            if check(middle):
                ans = middle
                high_rad = middle - 1
            else:
                low_rad = middle + 1
            
        return ans


# time:O((nlogn + klogn))
# space: O(1)