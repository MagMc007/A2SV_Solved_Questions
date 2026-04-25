# https://leetcode.com/problems/all-paths-from-source-to-target/description/
# 797. All Paths From Source to Target

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        ans = []

        def dfs(node, arr):
            arr = arr.copy()
            arr.append(node)

            if node == n - 1:
                ans.append(arr)
                return
            
            for nei in graph[node]:
                dfs(nei, arr)

        dfs(0, [])
        return ans

 
print(Solution().allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]]))
# print(Solution().allPathsSourceTarget(graph = [[1,2],[3],[3],[]]))

'''
2 ^ n paths on each n node 
time: O(n*2^n) => O(2^n)
we carry an array of size "path" on each call stack which is n ar max
n call stack
space: O(n * n)
'''

# u can optimize with backtracking
'''
def dfs(node, path):
    path.append(node)

    if node == n - 1:
        ans.append(path.copy())
    else:
        for nei in graph[node]:
            dfs(nei, path)

    path.pop()
'''