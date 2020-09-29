"""
使用二进制和位运算:子集有2^n,0-2^n-1的数字使用二进制表示,1代表存在，0代表不存在.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(0, 2 ** len(nums)):
            temp = []
            for j in range(0, len(nums)):
                if ((i >> j) & 1) == 1:
                    temp.append(nums[j])
            result.append(temp)
        return result
