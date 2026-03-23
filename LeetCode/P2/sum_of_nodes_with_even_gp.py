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
                if root.val % 2 == 0:
                    get_grand_children(root)

                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return sum_

# ===============================================
# time: O(n) => my function checks only 4 nodes so it is constant time so it won't count
# space: O(logn) or O(n)(if not balanced)


"""
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, parent, grandparent):
            if not node:
                return 0
            
            # If grandparent is even → include this node
            add = node.val if grandparent and grandparent.val % 2 == 0 else 0
            
            return (
                add
                + dfs(node.left, node, parent)
                + dfs(node.right, node, parent)
            )
        
        return dfs(root, None, None)
"""