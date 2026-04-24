# https://leetcode.com/problems/is-graph-bipartite/description/
# 785. Is Graph Bipartite?
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # for bipartite all neighbors have to be colored different
        n = len(graph)

        # colors are 0 and 1
        # start with -1 to mark all univisited
        colors = [-1] * n

        # all needed is one condition to invalidate all 
        def dfs(node):
            res = True
            for nei in graph[node]:
                if colors[nei] == -1:
                    # pain it different from its neighbor
                    colors[nei] = 1 - colors[node]
                    res = res and dfs(nei)

                    if not res:
                        return False
                elif colors[node] == colors[nei]:
                    return False
                
            return True
        res = True

        for i in range(n):
            if colors[i] == -1:
                res = res and dfs(i)

                if not res:
                    return False
        return True