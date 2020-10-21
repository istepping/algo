# [查考target出现区间](https://www.lintcode.com/problem/search-for-a-range/description)
## 方法一:先搜索到左边索引，在进行递推判断[5, 7, 7, 8, 8, 10],[3,4]
# 0,5,2-> 2,5,3-> 3,5,4
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        left, right = 0, len(A) - 1
        if len(A) == 0:
            return [-1, -1]
        # 左侧二分逼近
        while left + 1 < right:
            mid = (left + right) // 2
            if A[left] == target:
                print("break1")
                break
            if A[right] == target:
                print("break2")
                break
            if A[mid] < target:
                print("mid1")
                left = mid
            else:
                print("mid2")
                right = mid
                # 此时A[left]=target
        if A[left] == target:
            # 从左向右生长
            print("1")
            right=left
            while right + 1 < len(A) and A[right + 1] == target:
                right += 1
            while left - 1 >= 0 and A[left - 1] == target:
                left -= 1
            return [left, right]
        elif A[right]==target:
            # 从右向左生长
            print("2")
            left=right
            while left - 1 >= 0 and A[left - 1] == target:
                left -= 1
            while right + 1 < len(A) and A[right + 1] == target:
                right += 1
            return [left, right]
        else:
            return [-1,-1]


## 方法二:两次二分查找,先查找左侧索引，再查找右侧索引
if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([-1,0,1,2,2,2,3,3,3,4,4,4,5,5,6,90,92,93,101], 2))
