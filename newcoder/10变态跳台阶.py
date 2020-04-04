"""
* 题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
* 思路: f(n)=f(n-1)+f(n-2)+...+f(0), f(0)=1,f(1)=1,f(2)=2 f(3)=f(0)+f(1)+f(2)=4
"""


class Solution:
    def __init__(self):
        self.result = []
        self.result.append(1)
        self.result.append(1)

    def jumpFloorII(self, number):
        assert number >= 0, "error input!"
        if number >= len(self.result):
            for i in range(len(self.result), number + 1):
                r = 0
                for j in range(0, i):
                    r += self.result[j]
                self.result.append(r)
        return self.result[number]
