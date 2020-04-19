"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.stack_min = []
        self.min_index = []

    def push(self, node):
        self.stack.append(node)
        if len(self.stack) == 1:
            self.stack_min.append(node)
            self.min_index.append(0)
        elif node < self.stack_min[-1]:
            self.stack_min.append(node)
            self.min_index.append(len(self.stack) - 1)

    def pop(self):
        if len(self.stack) < 1:
            return
        if len(self.stack) - 1 == self.min_index[-1]:
            self.stack_min.pop(-1)
            self.min_index.pop(-1)
        return self.stack.pop(-1)

    def top(self):
        if len(self.stack) < 1:
            return
        return self.stack[-1]

    def min(self):
        return self.stack_min[-1]
