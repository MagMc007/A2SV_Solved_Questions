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
    
# time: O(n^2)
# space: O(logn)

'''
reusing the previous sums would reduce the time complexity greatly
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {0: 1}  # base case
        cnt = 0

        def dfs(node, curr_sum):
            nonlocal cnt
            if not node:
                return

            curr_sum += node.val

            # check how many times (curr_sum - target) occurred
            cnt += prefix.get(curr_sum - targetSum, 0)

            # add current sum to hashmap
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

            # traverse
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            # backtrack
            prefix[curr_sum] -= 1

        dfs(root, 0)
        return cnt

'''