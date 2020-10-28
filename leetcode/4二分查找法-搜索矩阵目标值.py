"""
search-a-2d-matrix
矩阵转换为一维数组: x=n/col_num y=n%col_num
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m <= 0:
            return False
        n = len(matrix[0])
        if n <= 0:
            return False
        start = 0
        end = m * n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid // n][mid % n] < target:
                start = mid
            else:
                end = mid
        if matrix[start // n][start % n] == target or matrix[end // n][end % n] == target:
            return True
        else:
            return False
