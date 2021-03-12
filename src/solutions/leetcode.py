# 力扣 ListNode 存的 val 永远是 int
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
