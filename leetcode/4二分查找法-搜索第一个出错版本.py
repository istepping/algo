# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(n):
    return True


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        思路: 出错向左，没有出错，向右
        """
        left = 0
        right = n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if isBadVersion(mid + 1):
                right = mid
            else:
                left = mid
        if isBadVersion(left + 1):
            return left + 1
        else:
            return right + 1

# 2,1,1
