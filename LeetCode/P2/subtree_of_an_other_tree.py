# https://leetcode.com/problems/subtree-of-another-tree/description/
# 572. Subtree of Another Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stat = True

        def preorder(root1, root2):
            nonlocal stat
            if root1 and root2:
                if root1.val != root2.val:
                    stat = False
                    return 
                
                # travese left and check
                preorder(root1.left, root2.left)
                
                # traverse right and check
                preorder(root1.right, root2.right)
            else:
                if root1 or root2:
                    stat = False
                    return 
                
        preorder(p, q)
        return stat
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



# time: O(n)
# space: O(n) # being given a LL