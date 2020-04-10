# [题目连接](https://www.nowcoder.com/practice/c61c6999eecb4b8f88a98f66b273a3cc?)
"""
回溯法
构建回溯递归函数:
"""


class Solution:
    def __init__(self):
        self.matrix = None
        self.rows = 0
        self.cols = 0
        self.path = None
        self.next = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.nomark = None

    def hasPath(self, matrix, rows, cols, path):
        self.matrix = matrix  # 一维数组
        self.rows = rows
        self.cols = cols
        self.path = path
        self.nomark = [[1 for j in range(cols)] for i in range(rows)]
        # 遍历matrix,遍历next,进行递归
        for i in range(rows):
            for j in range(cols):
                if self.backtracking(i, j, 0):
                    # 找到一条路径
                    return True
        return False

    def backtracking(self, i, j, pathlen):
        # 完成递归
        if pathlen == len(self.path):
            return True
        # 完成一次搜索
        if 0 <= i < self.rows and 0 <= j < self.cols and self.matrix[i * self.cols + j] == self.path[pathlen] and \
                self.nomark[i][j]:
            self.nomark[i][j] = 0
            for shift in self.next:
                if self.backtracking(i + shift[0], j + shift[1], pathlen + 1):
                    return True
            # 回溯
            self.nomark[i][j] = 1
        return False


# 一个异常
s = Solution()
print(s.hasPath(["a", "b", "c", "e", "s", "f", "c", "s", "a", "d", "e", "e"], 3, 4, "abce"))
