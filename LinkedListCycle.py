from typing import Optional,List
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        curr = head
        while curr is not None:
            if curr in seen:
                return True
            seen.append(curr)
            curr = curr.next
        return False
    def hasCycle2(self, head: Optional[ListNode]) -> bool: #Optimal , fast and slow pointer algorithm
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
