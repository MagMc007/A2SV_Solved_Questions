# https://leetcode.com/problems/reverse-linked-list/description/
# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we keep the prev and make the next point back to it
        if not head:
            return None
        
        prev = None
        
        while head and head.next:
            nxt = head.next

            head.next = prev
            prev = head
            # print(head.val)
            head = nxt  # this means head = head.next

        # now we are on the last value
        head.next = prev
        
        return head
            