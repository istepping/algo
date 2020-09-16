"""
1. 确定带有变量的标号:使用长度3或5示例
abccc bc
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is None:
            return 0

        h, n = len(haystack), len(needle)
        for i in range(h - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return -1
