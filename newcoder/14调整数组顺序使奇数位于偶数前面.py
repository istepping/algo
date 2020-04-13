# -*- coding:utf-8 -*-
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""


class Solution:
    def __init__(self):
        self.old = []
        self.even = []

    def reOrderArray(self, array):
        for item in array:
            if item % 2 == 0:
                self.even.append(item)
            else:
                self.old.append(item)
        for item in self.even:
            self.old.append(item)
        return self.old


# write code here
s = Solution()
print(s.reOrderArray([1, 4, 3, 6]))

