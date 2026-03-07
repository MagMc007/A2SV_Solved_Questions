# https://leetcode.com/problems/odd-even-linked-list/description/
# 328. Odd Even Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 3 pointers
        # iterator, locate odd insetion, locate even insetion 
        # keep location of next iter with in the loop

        if not head: # empty
            return 
     
        if not head.next: # 1 elem
            return head
        
        if head.next and not head.next.next: # just 2 elems
            return head

        odd_end = head
        even_end = head.next

        curr = head.next.next  # 3rd elem
        odd = True

        while curr and curr.next:  # to the last
            nxt = curr.next

            if odd:  # currently at odd
                nxt1 = odd_end.next 
                nxt2 = curr.next  # next to odd we have even

                odd_end.next = curr
                curr.next = nxt1
                odd_end = odd_end.next

                even_end.next = nxt2
                even_end = even_end.next

            odd = not odd
            curr = nxt

        # if the last was odd
        if odd:
            nxt1 = odd_end.next

            odd_end.next = curr
            curr.next = nxt1

            even_end.next = None
        
        return head
            

# time: O(n)
# space: O(1)


