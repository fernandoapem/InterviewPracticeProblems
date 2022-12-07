from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        nhead = ListNode()
        curr = nhead
        for item in range(0,len(nodes)):
            node = nodes.pop()
            node.next = None
            curr.next = node
            curr = curr.next
        return nhead.next
    def reverse2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev