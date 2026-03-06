# https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# 237. Delete Node in a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # keep moving fwd while assigning the value 
        # of next to curr
        while node and node.next:
            node.val = node.next.val
            # we must track the prev so that we can remove the last
            prev = node
            node = node.next

        
        # now we reach the last node, so we get rid of it
        prev.next = None