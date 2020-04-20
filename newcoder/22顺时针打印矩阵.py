"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


class Solution:
    def __init__(self):
        self.a = list()

    def out_circle(self, matrix):
        row, column = len(matrix), len(matrix[0])
        if row == 1:
            for i in range(column):
                self.a.append(matrix[0][i])
            return
        elif column == 1:
            for i in range(row):
                self.a.append(matrix[i][0])
            return
        else:
            for i in range(column - 1):
                self.a.append(matrix[0][i])
            for i in range(row):
                self.a.append(matrix[i][column - 1])
            for i in list(range(column - 2, -1, -1)):
                self.a.append(matrix[row - 1][i])
            for i in range(row - 2, 0, -1):
                self.a.append(matrix[i][0])
        if row > 2 and column>2:
            matrix = matrix[1:row - 1]
            new_matrix = list()
            for i in matrix:
                i.pop(0)
                i.pop(-1)
                new_matrix.append(i)
            self.out_circle(new_matrix)

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        self.out_circle(matrix)
        return self.a


s = Solution()
a = s.printMatrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
print(a)
