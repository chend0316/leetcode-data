from .leetcode import ListNode

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        pre_group = dummy
        cur = head

        while cur:
            # input: pre_group, cur
            i = 0
            pre, cur_group = None, cur
            while cur and i < k:
                cur.next, pre, cur = pre, cur, cur.next
                i += 1
            if i == k:
                pre_group.next = pre
                pre_group = cur_group
            else:
                pre, cur = None, pre
                while cur:
                    cur.next, pre, cur = pre, cur, cur.next
                pre_group.next = pre
                break
        
        return dummy.next
