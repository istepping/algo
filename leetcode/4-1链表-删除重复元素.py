class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p is not None and p.next is not None:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
