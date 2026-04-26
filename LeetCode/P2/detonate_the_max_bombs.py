# https://leetcode.com/problems/detonate-the-maximum-bombs/description/
# 2101. Detonate the Maximum Bombs
from collections import defaultdict


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        # first find the distance b/n points
        # d = ((x1 -x2) ^2 + (y1 - y2)^2) ^0.5 will be the formula for the distance
        N = len(bombs)
        # directed
        graph = defaultdict(list)

        # O(n^2)
        for i in range(N):
            x1, y1, rad1 = bombs[i]
            for j in range(N):
                if i == j:
                    continue

                x2, y2, rad2 = bombs[j]

                d = ((x1-x2)**2 + (y1-y2)**2)

                if d <= rad1*2:  # it can detonate it
                    graph[i].append(j)

        max_detonation = 0
        visited = set()
        
        # count the depth of the graph
        def dfs(i):
            visited.add(i)

            cnt = 1
            for nei in graph[i]:
                if nei not in visited:
                    cnt += dfs(nei)

            return cnt
            
        for i in range(N):
            visited = set()
            max_detonation = max(dfs(i), max_detonation)
        
        return max_detonation
            
'''
so the basic step is to figure out the distance w/c will be the realtion
between the nodes(bombs)

time: O(n^2 + n(n + e)) n-nodes e-edges    complete graph e=n(n-1) = n^2
    O(n^3) finally
space: O(n + (n + e)) => O(n^2)
'''