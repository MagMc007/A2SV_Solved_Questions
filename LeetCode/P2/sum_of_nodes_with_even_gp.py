# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
# 1315. Sum of Nodes with Even-Valued Grandparent
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        sum_ = 0

        def get_grand_children(root):
            nonlocal sum_
            # get the grand children
            left_child = root.left if root.left else None
            right_child = root.right if root.right else None

            if left_child:
                sum_ += left_child.left.val if left_child.left else 0
                sum_ += left_child.right.val if left_child.right else 0

            if right_child:
                sum_ += right_child.left.val if right_child.left else 0
                sum_ += right_child.right.val if right_child.right else 0

        def traverse(root):
            if root:
                get_grand_children(root)

                traverse(root.left)
                traverse(root.right)
                
        traverse(root)
        return sum_