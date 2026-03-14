# https://leetcode.com/problems/two-city-scheduling/description/
# 1029. Two City Scheduling
class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        differences = []

        for i in range(len(costs)):
            a, b = costs[i]
            differences.append([i, a - b])
        
        differences.sort(key=lambda x: x[1], reverse=True)
        print(differences)

        toB = differences[:len(costs)//2]
        toA = differences[len(costs)//2:]

        total_cost = 0

        # difference too big, better to send to b rather than a
        for j in range(len(costs)//2):
            idxb, _ = toB[j]
            idxa, _ = toA[j]

            total_cost += costs[idxa][0] + costs[idxb][1]
        
        return total_cost

print(Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))