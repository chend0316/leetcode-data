from .leetcode import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        carry = 0
        dummy = ListNode()
        p = dummy
        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            p.next = ListNode(s % 10)
            carry = s // 10
            p = p.next
        return dummy.next
