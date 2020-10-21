from typing import List


# 二分查找法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # 从候选值中返回结果,left+1=right
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1


# [查考target出现区间](https://www.lintcode.com/problem/search-for-a-range/description)
## 方法一:先搜索到左边索引，在进行递推判断

## 方法二:两次二分查找,先查找左侧索引，再查找右侧索引
