# https://leetcode.com/problems/employee-importance/description/
# 690. Employee Importance
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # construct the graph first
        graph = defaultdict(list)
        importances = {}

        # use the index as a key or id for employees
        for employee in employees:
            i = employee.id
            importance = employee.importance
            subordinates = employee.subordinates

            importances[i] = importance

            for j in subordinates:
                graph[i].append(j)
        
        # take the id and start dfs from it
        visited = set()
        total_importance = 0

        def dfs(i):
            nonlocal total_importance

            # add the importance and mark it visited
            total_importance += importances[i]
            visited.add(i)

            # go through the neighbors of the current id
            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei)

        dfs(id)
        return total_importance
        
'''
no need for the visited btw, all are unique

time: O(n) n - number of employees on the account of visiting al of them
space:
    -> graph is O(n + e) at worst O(n + n -1) => O(n)
    -> O(n) n- number of employess(just the importance hash and visited)
    => overall O(n)
    '''