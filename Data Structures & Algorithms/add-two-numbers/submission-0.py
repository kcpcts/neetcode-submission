# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry = False
        dummy = ListNode()
        solution = dummy
        while p1 and p2:
            current = p1.val + p2.val
            if carry == True:
                current += 1
            if current >= 10:
                current -= 10
                carry = True
            else: carry = False

            dummy.next = ListNode(current,None)
            p1 = p1.next
            p2 = p2.next
            dummy = dummy.next
        while p1:
            current = p1.val
            if carry == True:
                current += 1
            if current >= 10:
                current -= 10
                carry = True
            else: carry = False

            dummy.next = ListNode(current,None)
            p1 = p1.next
            dummy = dummy.next
        while p2:
            current = p2.val
            if carry == True:
                current += 1
            if current >= 10:
                current -= 10
                carry = True
            else: carry = False

            dummy.next = ListNode(current,None)
            p2 = p2.next
            dummy = dummy.next
        
        if carry:
            dummy.next = ListNode(1)
        return solution.next
        
        

                