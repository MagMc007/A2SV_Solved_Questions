# https://leetcode.com/problems/daily-temperatures/description/
# 739. Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # mon decreasing will do it
        ans = [0] * len(temperatures)

        # (idx, num)
        mon_dec = []

        for idx, num in enumerate(temperatures):
            while mon_dec and mon_dec[-1][1] < num:
                left = mon_dec[-1][0]
                ans[left] = idx - left
                mon_dec.pop()
            
            mon_dec.append((idx, num))
        return ans

print(Solution().dailyTemperatures(temperatures = [30,40,50,60]))


