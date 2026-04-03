# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/description/
# 1373. Maximum Sum BST in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_total_sum = 0
        
        def postorder(node):
            if not node:
                return True, float('inf'), float('-inf'), 0
            
            # chekc children (using call stack)
            left_is_bst, left_min, left_max, left_sum = postorder(node.left)
            right_is_bst, right_min, right_max, right_sum = postorder(node.right)
            
            # check current node is BST
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                current_sum = node.val + left_sum + right_sum
                self.max_total_sum = max(self.max_total_sum, current_sum)
                
                # pass on the min from the right side, max of left 
                return True, min(node.val, left_min), max(node.val, right_max), current_sum
            
            return False, 0, 0, 0 # start fresh on the sum

        postorder(root)
        return self.max_total_sum