# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39
class Solution:
    def __init__(self):
        self.temp = []
        for i in range(40):
            if i == 0:
                self.temp.append(0)
            elif i == 1:
                self.temp.append(1)
            else:
                self.temp.append(self.temp[-1] + self.temp[-2])

    def Fibonacci(self, n):
        # write code here
        assert 0 <= n <= 39, "error input!"
        return self.temp[n]
