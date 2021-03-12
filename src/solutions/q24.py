from .leetcode import ListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            a.next, b.next, pre.next = b.next, a, b
            pre = a
        return dummy.next
