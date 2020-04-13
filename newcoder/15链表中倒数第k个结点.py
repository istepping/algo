"""
输入一个链表，输出该链表中倒数第k个结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # 链表转到数组中返回数组倒数第k个元素
        a = list()
        if head is None:
            return head
        while head:
            a.append(head)  # 不用head.val
            head = head.next
        if 0 < k <= len(a):
            return a[-k]
        else:
            return None

