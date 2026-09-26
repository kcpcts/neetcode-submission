# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        
        length = 0
        ptr = head
        while ptr:
            length+=1
            ptr = ptr.next

        if n == length:
            return head.next

        index = length - n
        before = None
        after = None
        ptr = head
        while index > 0:
            if index == 1:
                before = ptr
            ptr = ptr.next
            index -=1
        # before is the one before ptr, need to stitch before -> ptr.next
        before.next = ptr.next # removed ptr from the link

        return head
            