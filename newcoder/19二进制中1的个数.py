# -*- coding:utf-8 -*-
# [python-编码](https://blog.csdn.net/weixin_42008966/article/details/103062731)
# 按位运算就是通过补码进行运算
class Solution:
    def NumberOf1(self, n):
        return bin(n & 0xffffffff).count("1")


s = Solution()
s.NumberOf1(2)
