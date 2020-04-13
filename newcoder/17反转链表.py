"""
输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # 遍历list,添加到新list的头部
        if pHead:
            newHead = ListNode(pHead.val)
            newHead.next = None
            pHead = pHead.next
        else:
            return pHead
        while pHead:
            head = ListNode(pHead.val)
            head.next = newHead
            newHead = head
            pHead = pHead.next
        return newHead


pHead = ListNode(1)
pHead.next = ListNode(2)
s = Solution()
print(s.ReverseList(pHead).val)
