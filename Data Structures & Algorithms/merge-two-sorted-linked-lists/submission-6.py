# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # advance the lesser of the two to maintain sorted order
        #when we reach the end of one, advance all of the rest of the toher
        
        dummy = ListNode()
        sol = dummy
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val < p2.val:
                dummy.next = ListNode(p1.val)
                dummy = dummy.next
                p1 = p1.next
            else:
                dummy.next = ListNode(p2.val)
                dummy = dummy.next
                p2 = p2.next
        while p1:
            dummy.next = ListNode(p1.val)
            dummy = dummy.next
            p1 = p1.next
        while p2:
            dummy.next = ListNode(p2.val)
            dummy = dummy.next
            p2 = p2.next
        return sol.next

        
