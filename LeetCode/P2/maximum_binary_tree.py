# https://leetcode.com/problems/maximum-binary-tree/description/
# 654. Maximum Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def divide_and_conquer(arr):
            if not arr:
                return 
            
            root = max(arr)
            idx = arr.index(root)

            left_sub_tree = arr[:idx]
            right_sub_tree = arr[idx+1:]

            # create the node
            root = TreeNode(root)

            root.left = divide_and_conquer(left_sub_tree)

            root.right = divide_and_conquer(right_sub_tree)
            
            return root

        return divide_and_conquer(nums)


# time: O(n**2)
# space: O(n)