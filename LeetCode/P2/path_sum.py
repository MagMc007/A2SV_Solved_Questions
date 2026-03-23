# https://leetcode.com/problems/path-sum-iii/
# 437. Path Sum III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0

        def sum_up_children(root, sum_):
            nonlocal cnt
            nonlocal targetSum

            if root:
                sum_ += root.val

                if sum_ == targetSum:
                    cnt += 1
                else:
                    sum_up_children(root.left, sum_)
                    sum_up_children(root.right, sum_)
     
        def trav(root):
            nonlocal cnt
            nonlocal targetSum

            if root:
                # start it at every node
                sum_up_children(root, 0)  

                trav(root.left)
                trav(root.right)
        trav(root)
        return cnt