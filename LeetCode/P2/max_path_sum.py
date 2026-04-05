# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# 124. Binary Tree Maximum Path Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = float("-inf")

        def dfs(node):
            nonlocal mx
            if not node:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # update max
            mx = max(mx, node.val + left + right)

            return node.val + max(left, right)
        
        dfs(root)
        return mx
