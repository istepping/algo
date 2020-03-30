# -*- coding:utf-8 -*-
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# 栈不是python的内置包,但是可以使用queue替代使用,可以使用列表[]替代stack
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    # write code here
    def pop(self):
        if len(self.stack2) > 0:
            xx = self.stack2.pop()  # 默认index=-1最后一个元素
        else:
            assert len(self.stack1) > 0, "empty!"
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            xx = self.stack2.pop()
        return xx
