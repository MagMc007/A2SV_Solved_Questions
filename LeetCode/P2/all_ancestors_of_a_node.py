# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/
# 2192. All Ancestors of a Node in a Directed Acyclic Graph
from collections import defaultdict, deque

# BFS
# class Solution:
#     def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
#         graph = defaultdict(list)
#         indeg = [0] * n

#         for u,v in edges:
#             graph[u].append(v)
#             indeg[v] += 1
        
#         q = deque()
#         # get those with not indegree
#         for i in range(n):
#             if indeg[i] == 0:
#                 q.append(i)

#         ans = [set() for _ in range(n)]

#         while q:
#             node = q.popleft()

#             for nei in graph[node]:
#                 # node + parents of node are the parents of the current
#                 ans[nei].add(node)
#                 ans[nei].update(ans[node])


#                 indeg[nei] -= 1

#                 if indeg[nei] == 0:
#                     # it is ready to be ancestor
#                     q.append(nei) 

#         return [sorted(list(a)) for a in ans]

# print(Solution().getAncestors(8,[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))

'''
time: O(v + e) = O(n**2)
space: O(n ** 2)
'''