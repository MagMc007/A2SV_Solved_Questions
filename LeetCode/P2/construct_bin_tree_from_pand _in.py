# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        # Root
        mid = inorder.index(root_val)

        # left of the root 
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

        # right of the root
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

# time: O(n**2) index look up and 
# space: O(n**2) because of slicing 