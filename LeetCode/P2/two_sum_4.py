# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# 653. Two Sum IV - Input is a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, k):
        visited = set()

        def dfs(node):
            if not node:
                return False
            
            if (k - node.val) in visited:
                return True
            
            visited.add(node.val)
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

# time: O(n)
# space: O(n + h) => O(n)