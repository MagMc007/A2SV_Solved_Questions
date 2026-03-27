# https://leetcode.com/problems/distribute-coins-in-binary-tree/
# 979. Distribute Coins in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.total_moves = 0

        def traverse(node):
            if not node:
                return 0
            
            left_balance = traverse(node.left)
            right_balance = traverse(node.right)
            
            self.total_moves += abs(left_balance) + abs(right_balance)
            
            return node.val + left_balance + right_balance - 1

        traverse(root)
        return self.total_moves