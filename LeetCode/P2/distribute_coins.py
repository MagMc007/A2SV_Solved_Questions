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
            
            # get the right and left balances
            left_balance = traverse(node.left)
            right_balance = traverse(node.right)
            
            # addition of the balances will be the total move needed
            self.total_moves += abs(left_balance) + abs(right_balance)
            
            return node.val + left_balance + right_balance - 1

        traverse(root)
        return self.total_moves

'''
time: O(n)
space: O(logn)
'''