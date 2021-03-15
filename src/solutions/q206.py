from .leetcode import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        return prev
