"""
* 题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
* 思路: n级台阶的跳法=1*前n-1个台阶的跳法+1*前n-2个台阶的跳法(因为最后的跳法就两种:跳一个,或跳两个)
"""


class Solution:
    def __init__(self):
        self.result = []
        self.result.append(0)
        self.result.append(1)
        self.result.append(2)

    def jumpFloor(self, number):
        assert number >= 0, "error input!"
        if number >= len(self.result):
            for i in range(len(self.result), number + 1):
                self.result.append(self.result[i - 1] + self.result[i - 2])
        return self.result[number]
