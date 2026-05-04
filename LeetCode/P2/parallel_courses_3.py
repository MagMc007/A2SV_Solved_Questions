# https://leetcode.com/problems/parallel-courses-iii/description/
# 2050. Parallel Courses III
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        graph = defaultdict(list)
        indeg = [0] * n
        
        for u, v in relations:
            graph[u - 1].append(v - 1)
            indeg[v - 1] += 1
        
        dp = [0] * n
        
        q = deque()
        
        # initialize
        for i in range(n):
            if indeg[i] == 0:
                dp[i] = time[i]
                q.append(i)   
        
        while q:
            node = q.popleft()
            
            for nei in graph[node]:
                dp[nei] = max(dp[nei], dp[node] + time[nei])
                
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        return max(dp)


# print(Solution().minimumTime(n = 5, relations = [[1,5],[2,5],[3,5],[1,4]], time = [1,2,3,4,5]))