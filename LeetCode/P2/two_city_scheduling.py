# https://codeforces.com/problemset/problem/2112/C
# 1029. Two City Scheduling
class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs.sort(key=lambda x: min(x))
        total = 0

        for i in costs:
            

        return costs

print(Solution().twoCitySchedCost([[10,20],[300,200],[400,50],[30,20]]))