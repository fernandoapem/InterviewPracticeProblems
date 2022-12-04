from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.push(curr)
            curr = curr.next
        nhead = ListNode()
        curr = nhead
        for node in nodes:
            curr.next = nodes.pop()
            curr = curr.next
        return nhead