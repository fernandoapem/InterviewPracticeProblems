from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            maxCount = 0
            curr = head
            while curr:
                maxCount += 1
                curr = curr.next
            middle = int(maxCount / 2) + 1
            node = head
            count = 1
            while count < middle:
                node = node.next
                count += 1
            return node
        def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        