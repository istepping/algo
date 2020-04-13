"""
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here,从两个链表头
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        if pHead1.val < pHead2.val:
            newHead = ListNode(pHead1.val)
            pHead1 = pHead1.next
        else:
            newHead = ListNode(pHead2.val)
            pHead2 = pHead2.next
        p = newHead
        while pHead1:
            if pHead2 and pHead1.val > pHead2.val:
                p.next = pHead2
                p = pHead2
                pHead2 = pHead2.next
            else:
                p.next = pHead1
                p = pHead1
                pHead1 = pHead1.next
        if pHead2:
            p.next = pHead2
        return newHead


s = Solution()
pHead1 = ListNode(1)
pHead1.next = ListNode(3)
pHead2 = ListNode(2)
p = s.Merge(pHead1, pHead2)
