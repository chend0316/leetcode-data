from .leetcode import ListNode
from typing import List

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self._merge(lists[0], lists[1])
        else:
            a = self.mergeKLists(lists[:len(lists)//2])
            b = self.mergeKLists(lists[len(lists)//2:])
            return self.mergeKLists([a, b])

    def _merge(self, a, b):
        dummy = ListNode()
        p = dummy
        while a or b:
            if not a or (b is not None and b.val < a.val):
                p.next = b
                b = b.next
            else:
                p.next = a
                a = a.next
            p = p.next
        return dummy.next
