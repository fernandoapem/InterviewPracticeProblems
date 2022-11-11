# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = list1
        curr2 = list2
        final = ListNode(-1, None)
        head = final
        while (curr is not None) and (curr2 is not None):
            if curr.val > curr2.val:
                final.next = curr2
                final = final.next
                curr2 = curr2.next
            else:
                final.next = curr
                final = final.next
                curr = curr.next
        if curr:
            final.next = curr
        elif curr2:
            final.next = curr2
        return head.next


p = Solution()
list3 = ListNode(4, None)
list2 = ListNode(2, list3)
list1 = ListNode(1, list2)

blist3 = ListNode(4, None)
blist2 = ListNode(3, blist3)
blist1 = ListNode(1, blist2)


print(p.mergeTwoLists(list1, blist1).val)
