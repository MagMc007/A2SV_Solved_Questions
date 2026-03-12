# https://leetcode.com/problems/remove-nodes-from-linked-list/description/
# 2487. Remove Nodes From Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # parse to stack => do a monotonic decreasing stack 
        # space will be O(n)

        # but must be optiomal
        if not head and not head.next:  # 0 or 1 elem
            return head
    
        prev = head
        curr = head.next

        while curr:  # as i will need to check for the last element also
            check = head

            # now way to go back so we start from the head
            if curr.val > prev.val:  # now it became greater
                while check.val >= curr.val:
                    check = check.next

                # i will stop on the element that is less than curr
                # no way to acces the prev element so override the 
                # check with curr
                check.next = curr.next
                check.val = curr.val

                prev = curr
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next

        return head

#time O(n^2)
# space O(1)

# way optimal solution would be to reverse the LL and do a 
# increasing stack in that case the space will be O(1) and time will be O(3n)=> O(n)