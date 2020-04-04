"""
要覆盖 2*n 的大矩形，可以先覆盖 2*1 的矩形，再覆盖 2*(n-1) 的矩形；
或者先覆盖 2*2 的矩形，再覆盖 2*(n-2) 的矩形。
f(1)=1 f(2)=2 f(n)=f(n-1)+f(n-2)
"""


class Solution:
    def rectCover(self, number):
        assert number >= 0, "error input!"
        if number <= 2:
            return number
        else:
            a = 1
            b = 2
            result = 0
            for i in range(3, number + 1):
                result = a + b
                a = b
                b = result
            return result


class Solution2:
    def __init__(self):
        self.result = []
        # 前三个元素
        self.result.append(0)
        self.result.append(1)
        self.result.append(2)

    def rectCover(self, number):
        assert number >= 0, "error input!"
        if number >= len(self.result):
            for i in range(len(self.result), number + 1):
                self.result.append(self.result[i - 1] + self.result[i - 2])
        return self.result[number]


class Solution3:

    def rectCover(self, number):
        assert number >= 0, "error input!"
        if number <= 2:
            return number
        else:
            return self.rectCover(number - 1) + self.rectCover(number - 2)
