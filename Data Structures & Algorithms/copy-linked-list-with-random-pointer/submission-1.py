"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {} # real nodes --> fake nodes
        if not head:
            return None
        mapping[head] = Node(head.val, None, None)
        ptr = head
        while ptr:
            mapping[ptr] = Node(ptr.val, None, None)
            ptr = ptr.next
        ptr = head
        while ptr:
            mapping[ptr].next = mapping[ptr.next] if ptr.next else None
            mapping[ptr].random = mapping[ptr.random] if ptr.random else None 
            ptr = ptr.next
        return mapping[head]
        